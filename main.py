import boto3

aws_managment = boto3.Session(profile_name='boto-3-user')


# client 
ec2_client =aws_managment.client('ec2')
#print("This is client Response : ",dir(ec2_client)) 
 
print() 
ec2_client.describe_regions()


# resource
ec2_resource = aws_managment.resource('ec2') 
#print("This is Resource Response",dir(ec2_resource))