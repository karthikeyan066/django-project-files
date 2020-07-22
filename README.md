# django-project-files
To deploy the django project Elastic beanstalk(EBCLI) , i followed this AWS Elastic Beanstalk document below:
(https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)

1)Installed awsebcli in window

2)Created key-pair in EC2
*file formate->pem(for openSSH)
3)Created Instance(created in cmd itself using commands. eb init)
*Region->ap-south-1 : Asia Pacific (Mumbai)
*created application by command as eb init -p python-3.6 application name.
choosed python 3.7 Amazon linux 2 for the platform
created the environment command as eb create


and error occured as
[Instance: i-0ff064e14ed5d7c2c] Command failed on instance. An unexpected error has occurred [ErrorCode: 0000000001].
Environment health has transitioned from Degraded to Severe. Command failed on all instances. ELB health is failing or not available for all instances.
