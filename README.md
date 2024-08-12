Active Directory Service Access Enumeration Tool
Overview
This tool is designed for enumerating Active Directory (AD) service access using the nxc tool. It helps in checking access for both local and domain users across various services. The services included in the enumeration are:

SMB (Server Message Block)
WINRM (Windows Remote Management)
WMI (Windows Management Instrumentation)
SSH (Secure Shell)
FTP (File Transfer Protocol)
MSSQL (Microsoft SQL Server)
The tool allows you to verify if credentials are valid for accessing these services by running specific nxc commands.

Features
Support for Local and Domain Users: Choose between local user and domain user authentication.
Service Checks: Checks access for SMB, WINRM, WMI, SSH, FTP, and MSSQL services.
Output Handling: Displays relevant output with color coding and handles scenarios where services are not available.
Timeout Management: Automatically skips commands that fail or take too long to respond.
Getting Started
Prerequisites
Python 3.x
nxc tool installed on your system
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/active-directory-service-enumeration.git
Navigate to the Project Directory

bash
Copy code
cd active-directory-service-enumeration
Install Required Packages

Ensure you have Python installed. No additional packages are required for this script.

Usage
Run the Script

bash
Copy code
python ad_service_enum.py
Provide User Input

Enter the IP address of the target system.
Specify whether you are using a local or domain user.
Enter the username and password for authentication.
Review the Output

The script will execute commands for each service and display relevant results. It will show lines with [+] if access is found or indicate if a service is not available.

Example Output
less
Copy code
AD NXC User Service Check
===========================
     ,     ,
    (\____/)
     (_oo_)
       (O)
     __||__    \)
  []/______\[] /
  / \______/ \/
 /    /__\
(\   /____\

Are you using a local user or domain user? (Enter 'local' or 'domain'): local

Enter the IP address: 10.10.154.154

Enter the username: Administrator

Enter the password: P@ssw0rd!

SMB Service
------------
[+] DOMAIN\Administrator:P@ssw0rd!

WINRM Service
-------------
SERVICE NOT AVAILABLE.

...
Contributing
Feel free to submit issues or pull requests. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.
