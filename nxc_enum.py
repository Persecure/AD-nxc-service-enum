import subprocess
import shlex

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"

# Function to print banner title with ASCII art
def print_banner(title):
    banner_art = """
     ,     ,
    (\\____/)
     (_oo_)
       (O)
     __||__    \\)
  []/______\\[] /
  / \\______/ \\/
 /    /__\\
(\\   /____\\
"""
    print(RED + banner_art + RESET)
    print(CYAN + "=" * (len(title) + 12))
    print(CYAN + "= " + BOLD + title + RESET + CYAN + " =")
    print(CYAN + " ($) " + BOLD + "by Persecure" + RESET + CYAN + " ($) ")
    print(CYAN + "=" * (len(title) + 12) + RESET)
    print()  # Newline for separation

# Function to print colored user prompts
def prompt_user(text):
    return input(MAGENTA + text + RESET).strip()

# Print banner title
print_banner("AD NXC User Service Check")

# Get input from the user
print()  # Line space before first input
user_type = prompt_user("Are you using a local user or domain user? (Enter 'local' or 'domain'): ").lower()
print()  # Line space after first input
ip_address = prompt_user("Enter the IP address: ")
print()  # Line space after second input
username = prompt_user("Enter the username: ")
print()  # Line space after third input
password = prompt_user("Enter the password: ")
print()  # Line space after fourth input

# Determine the flag based on user type
local_auth_flag = "--local-auth" if user_type == "local" else ""

# Define commands and their corresponding services
commands = {
    "smb": f"nxc smb {ip_address} -u {username} -p '{shlex.quote(password)}' {local_auth_flag}",
    "winrm": f"nxc winrm {ip_address} -u {username} -p '{shlex.quote(password)}' {local_auth_flag}",
    "wmi": f"nxc wmi {ip_address} -u {username} -p '{shlex.quote(password)}' {local_auth_flag}",
    "ssh": f"nxc ssh {ip_address} -u {username} -p '{shlex.quote(password)}' {local_auth_flag}",
    "ftp": f"nxc ftp {ip_address} -u {username} -p '{shlex.quote(password)}' {local_auth_flag}",
    "mssql": f"nxc mssql {ip_address} -u {username} -p '{shlex.quote(password)}' {local_auth_flag}"
}

# Function to execute a command and print specific lines with a timeout
def run_command(service, command, timeout=5):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=timeout)
        output = result.stdout
        
        # Split output into lines and filter lines containing '[+]'
        lines = output.splitlines()
        relevant_lines = [line for line in lines if "[+]" in line]
        
        if relevant_lines:
            for line in relevant_lines:
                print(GREEN + line + RESET)  # Green text for relevant lines
        else:
            print(f"{RED}{service.upper()} SERVICE NOT AVAILABLE.{RESET}")  # Red text for no output
            
    except subprocess.TimeoutExpired:
        print(f"{YELLOW}Command '{command}' timed out after {timeout} seconds. Skipping to next command.{RESET}")  # Yellow text for timeout
    except Exception as e:
        print(f"{RED}Error running command '{command}': {e}{RESET}")  # Red text for errors

    print()  # Line space after command output

# Run each command
for service, command in commands.items():
    run_command(service, command, timeout=5)
