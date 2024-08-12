# Active Directory Service Access Enumeration Tool

## Overview

This tool is designed for enumerating Active Directory (AD) service access using the `nxc` tool. It helps in checking access for both local and domain users across various services. The services included in the enumeration are:

- **SMB (Server Message Block)**
- **WINRM (Windows Remote Management)**
- **WMI (Windows Management Instrumentation)**
- **SSH (Secure Shell)**
- **FTP (File Transfer Protocol)**
- **MSSQL (Microsoft SQL Server)**

The tool allows you to verify if credentials are valid for accessing these services by running specific `nxc` commands.

## Features

- **Support for Local and Domain Users**: Choose between local user and domain user authentication.
- **Service Checks**: Checks access for SMB, WINRM, WMI, SSH, FTP, and MSSQL services.
- **Output Handling**: Displays relevant output with color coding and handles scenarios where services are not available.
- **Timeout Management**: Automatically skips commands that fail or take too long to respond.
