# POC Pytorch on AWS Lambda for inference
This is a proof of concept hack to deploy pytorch into lambda.
** Work in progress**

# Build on AWS CodePipeline
1. Folder stucture
```
    <sourcedir>|
               |--<your sourcecode & sub directories>
               |--requirements_lambda.txt
    buildspec.yaml
    docs       |
    <tests>    |
   
```    

2. The buildspec.yml attempts to package pytorch without cuda. But the package size is still large way to large to fit into lambda uncompressed package size of 250 MB. The buildspec_source is work in progress to attempt to build pytorch from source... Its is work in progress 
     

3. Makesure the environment settings uses the current docker image. For instance the current (as of Jun 2018) AMI version that lambda uses is amzn-ami-hvm-2017.03.1.20170812-x86_64-gp2, so the corresponding docker image is  amazonlinux:2017.03.1.20170812

![CodeBuild Enviornment Settings](https://github.com/elangovana/pytorch-lambda-inference/raw/master/docs/images/codebuild_environment.png "Codebuild Environment")




