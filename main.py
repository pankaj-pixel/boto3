import boto3

aws_managment = boto3.Session(profile_name='boto-3-user')


# client 
ec2_client =aws_managment.client('ec2')
#print("This is client Response : ",dir(ec2_client)) 
 
print() 
all_region = ec2_client.describe_regions()
print(all_region)

# resource
ec2_resource = aws_managment.resource('ec2') 
print(ec2_resource.describe_regions())
#print("This is Resource Response",dir(ec2_resource))