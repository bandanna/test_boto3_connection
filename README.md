# Boto3 Connection

There are different ways to work with Boto3. 

## 1. Export the AWS keys in the shell session

Following here:
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html

You can configure aws keys in the same shell session where you'll be using Boto3. 

Example:
```
# These are dummy passwords, don't worry xD
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_DEFAULT_REGION=eu-west-1

# Now run the script
python3 test_boto3_connection.py

```

If your python script works, then congrats!

## 2. Install AWS Cli and configure it

aws-cli is a tool that enables you to integrate with AWS locally. Once this tool is configured, it'll generate credentials and config files that both aws-cli and boto3 can recognize.

#### Installation Links:

On Windows:
https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html

On macOS:
https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html

On Linux:
https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html

#### Configuration:

Once the installation is done, you could configure it but typing in your shell/termina/cmd/powershell:
`aws configure`

Now, in interactive way, answer/fill the fileds, i.e.
```
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: eu-west-1
Default output format [None]: json
```

#### Test
Now you can test if `aws-cli` is working by simply listing the S3 buckets in your account (if you have such permissions).

`aws s3 ls` 

If that works then you're good to go!


#### Test Boto3

Now you can run the script, i.e. `python3 test_boto3_connection.py`