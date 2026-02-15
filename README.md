# AWS IAM User Onboarding Automation
- A Python automation solution using Boto3 to streamline AWS IAM identity provisioning. This script converts CSV-based HR data into a secure, functional AWS environment.

## Key Features
- **Idempotent Design:** Handles existing users/groups gracefully without crashing.
- **Automated Grouping:** Assigns users to IAM groups based on their department.
- **Architectural Best Practices:** Implements Group-Based Access Control (GBAC) for better scalability.
- **Security-First:** Enforces mandatory password resets on first login.
- **Automated Permissions:** Automatically attaches AmazonS3ReadOnlyAccess to new groups.

## Tech Stack
- Python 3.12
- AWS SDK for Python (Boto3)
- AWS IAM

## Project Structure
- UsersOnboard.py: Main execution script.
- employees.csv: Data source (columns: user, department).
- .env: (Hidden) Secure storage for AWS Access Keys.

## Validation
- Successfully provisioned users and groups in the AWS Console and attached policies to the groups.

### Identity Provisioning
- All users from the CSV were successfully created with the correct naming conventions.
  
  <img width="1919" height="872" alt="image" src="https://github.com/user-attachments/assets/e44a1ea6-d2e2-4cab-8818-3a776125043b" />

### Group Membership
- Verified that each user has been correctly assigned to their respective departmental group.
  
  <img width="1919" height="868" alt="image" src="https://github.com/user-attachments/assets/cd0480e5-b133-4d2a-bcbe-2105b7c2bc60" />


### Policy Attachment (Permissions)
- Confirmed that the AmazonS3ReadOnlyAccess policy is attached to the group level, granting users immediate access to required resources.
  
  <img width="1901" height="866" alt="image" src="https://github.com/user-attachments/assets/b145df31-0f23-4b1f-8cbb-06ce5328e200" />


