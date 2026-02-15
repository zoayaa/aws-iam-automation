import boto3
import csv
from botocore.exceptions import ClientError

# Initialize IAM client Globally
iam_client = boto3.client('iam')

# --------------------------
# Helper functions
# --------------------------

def create_iam_group(group_name):
    try:
        iam_client.create_group(GroupName=group_name)
        print(f"Created Group: {group_name}")
    except iam_client.exceptions.EntityAlreadyExistsException:
        print(f"Group {group_name} already exists.")
    except ClientError as e:
        print(f"Unexpected error creating group {group_name}: {e}")

def create_login_profile(username, password):
    try:
        iam_client.create_login_profile(
            UserName = username,            
            Password = password,          
            PasswordResetRequired = True
        )
        print(f"Login profile created for {username}")
    except iam_client.exceptions.EntityAlreadyExistsException:
        print(f"Login Profile already exists for {username}")
    except ClientError as e:
        print(f"Unexpected error creating login profile for {username}: {e}")

# --------------------------
# Main Logic
# --------------------------

def create_user(username, group_name):
    
    # 1. Ensure the Group exists
    create_iam_group(group_name)

    # 2. Attach Policy to the Group (Mandatory for permissions)
    try:
        # Using an AWS Managed Policy for S3 Read Only access
        policy_arn = 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess' 
        
        iam_client.attach_group_policy(
            GroupName=group_name,
            PolicyArn=policy_arn
        )
        print(f"Policy attached to group: {group_name}")
    except ClientError as e:
        print(f"Error attaching policy: {e}")

    # 3. Create the User
    try:
        iam_client.create_user(UserName=username)
        print(f"Created user: {username}")
    except iam_client.exceptions.EntityAlreadyExistsException:
        print(f"User {username} already exists.")

    # 4. Add User to Group
    try:
        iam_client.add_user_to_group(GroupName=group_name, UserName=username)
        print(f"Added {username} to {group_name}")
    except ClientError as e:
        print(f"Error adding user to group: {e}")

    # 5. Create Login Profile (Console Access)
    create_login_profile(username, 'TempPass123!')

# --------------------------
# Execution
# --------------------------

if __name__ == '__main__':
    try:
        # Ensure employees.csv is in /home/zoya/AWS/
        with open('employees.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user = row['user']
                dept = row['department']
                print(f"\nProcessing: {user} --> {dept}")
                create_user(user, dept)
    except FileNotFoundError:
        print("Error: employees.csv not found. Please create the file in the project folder.")
    except KeyError as e:
        print(f"Error: Missing column in CSV: {e}. Check if headers are 'user,department'.")