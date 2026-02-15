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
- src: <img width="1919" height="860" alt="image" src="https://github.com/user-attachments/assets/222cf998-55e5-47c4-8030-895b11b6503e" />

### Group Membership
- Verified that each user has been correctly assigned to their respective departmental group.
- src: <img width="1919" height="870" alt="image" src="https://github.com/user-attachments/assets/963374f7-4619-4c8f-a191-e0d643108c22" />

### Policy Attachment (Permissions)
- Confirmed that the AmazonS3ReadOnlyAccess policy is attached to the group level, granting users immediate access to required resources.
- src: <img width="1915" height="866" alt="image" src="https://github.com/user-attachments/assets/075f6b0e-2754-4a8e-8bf7-8f6a69bdf6f9" />


