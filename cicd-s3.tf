resource "aws_s3_bucket" "codepipeline_artifacts" {
  bucket = "buckettfpipeline-artifacts"
  acl    = "private"
}