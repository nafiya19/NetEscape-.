import os
import subprocess

# Command to disable the network interface on Windows
disable_network_command = "netsh interface set interface name=\"Wi-Fi\" admin=disable"

def disable_network():
    try:
        result = subprocess.run(disable_network_command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("Network disabled successfully.")
        else:
            print(f"Failed to disable network: {result.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    disable_network()
