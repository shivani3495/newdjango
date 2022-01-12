resource "aws_codebuild_project" "tf-plan" {
  name          = "Django_Build"
  description   = "Plan stage for terraform"
  service_role  = aws_iam_role.tf-codebuild-role.arn

  artifacts {
    type = "CODEPIPELINE"
  }

  environment {
    compute_type                = "BUILD_GENERAL1_SMALL"
    image                       = "aws/codebuild/standard:4.0"
    type                        = "LINUX_CONTAINER"
    image_pull_credentials_type = "CODEBUILD"

 }

 source {
     type   = "CODEPIPELINE"
     buildspec = file("buildspec.yml")           
 }
}

resource "aws_codedeploy_app" "pipeline" {
  compute_platform = "Server"
  name             = "pipeline"
}

resource "aws_codedeploy_deployment_group" "pipeline_gr"{
  app_name              = aws_codedeploy_app.pipeline.name
  deployment_group_name = "pipeline_gr"
  service_role_arn      = aws_iam_role.pipeline_policy.arn

  ec2_tag_set {
    ec2_tag_filter {
      key   = "Name"
      type  = "KEY_AND_VALUE"
      value = "codepipeline"
    }
}
}

resource "aws_codepipeline" "Django_Pipeline" {

    name = "Django_Pipeline"
    role_arn = aws_iam_role.tf-codepipeline-role.arn


    artifact_store {
        type="S3"
        location = aws_s3_bucket.codepipeline_artifacts.id
    }

    stage {
        name = "Source"
        action{
            name = "Source"
            category = "Source"
            owner = "AWS"
            provider = "CodeStarSourceConnection"
            version = "1"
            output_artifacts = ["tf-code"]
            configuration = {
                FullRepositoryId = "shivani3495/newdjango"
                BranchName   = "main"
                ConnectionArn = var.codestar_connector_credentials
                OutputArtifactFormat = "CODE_ZIP"
            }
        }
    }

    stage {
        name ="Build"
        action{
            name = "Build"
            category = "Build"
            provider = "CodeBuild"
            version = "1"
            owner = "AWS"
            input_artifacts = ["tf-code"]
            configuration = {
                ProjectName = "Django_Build"
            }
        }
    }

    stage {
        name ="Deploy"
        action{
            name = "Deploy"
            category = "Deploy"
            provider = "CodeDeploy"
            version = "1"
            owner = "AWS"
            input_artifacts = ["tf-code"]
            configuration = { 
                ApplicationName = "pipeline"
                DeploymentGroupName = "pipeline_gr"
                
            }
        }
    }
}
