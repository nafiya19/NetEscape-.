# shutdown_pcs.py

import subprocess
import time

# Read the list of active IP addresses from the file
with open("active_ips.txt", "r") as f:
    pcs = [line.strip() for line in f]

# Shutdown command
def shutdown_pc(ip):
    command = f"shutdown /s /f /t 0 /m \\\\{ip}"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Shutdown command sent to {ip}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to send shutdown command to {ip}: {e}")

# Send shutdown commands to all active PCs
for ip in pcs:
    shutdown_pc(ip)
    time.sleep(1)  # Optional: delay between commands
