import cryptography
import paramiko
import warnings
import time

# Suppress all warnings
warnings.filterwarnings("ignore")

print("cryptography version:", cryptography.__version__)
print("paramiko version:", paramiko.__version__)

# List of IP addresses of the PCs you want to disable the network on
pcs = ["192.168.56.1","172.20.6.1"]

# SSH credentials
username = "your_username"
password = "your_password"

# Command to disable the network interface on Windows
disable_network_command = "netsh interface set interface name=\"Wi-Fi\" admin=disable"

def disable_network(ip):
    """
    Connects to a PC via SSH and executes a command to disable the network interface.
    
    Args:
        ip (str): The IP address of the target PC.
    """
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the PC
        print(f"Attempting to connect to {ip}")
        ssh.connect(ip, username=username, password=password, timeout=30)
        print(f"Connected to {ip}")
        
        # Execute the disable network command
        stdin, stdout, stderr = ssh.exec_command(disable_network_command)
        print(f"Network disable command executed on {ip}")
        
        # Output command results
        output = stdout.read().decode()
        errors = stderr.read().decode()
        if output:
            print("Output:", output)
        if errors:
            print("Errors:", errors)
        
        # Close the connection
        ssh.close()
        print(f"Disconnected from {ip}")
    except paramiko.AuthenticationException:
        print(f"Authentication failed for {ip}")
    except paramiko.SSHException as sshException:
        print(f"Unable to establish SSH connection to {ip}: {sshException}")
    except Exception as e:
        print(f"Failed to disable network on {ip}: {e}")

# Loop through each PC and execute the disable network command
for pc in pcs:
    disable_network(pc)
    # Optional: Add a small delay between disabling network on each PC
    time.sleep(1)
