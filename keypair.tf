# Creating a new key
resource "aws_key_pair" "key-pair" {

# Name of the key 
key_name = "tfkeypair"

# Adding the SSH authorized key
public_key = file("publickey.pub")
}

