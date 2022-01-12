
terraform {
    backend "s3" {
        bucket = "buckettfpipeline"
        encrypt = true
        key = "terraform.tfstate"
        region = "ap-south-1"
        access_key = "AKIAJREE64MWXF5C7CFQ"
        secret_key = "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"
        
        
    }
}

