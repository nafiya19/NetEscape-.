# scan_ips.py

from scapy.all import sr1, IP, ICMP
import ipaddress

# Define the IP range
ip_range = ipaddress.IPv4Network("192.168.56.0/24")

# Function to check if a host is up
def is_host_up(ip):
    pkt = IP(dst=str(ip))/ICMP()
    resp = sr1(pkt, timeout=1, verbose=0)
    return resp is not None

# Scan the IP range
active_ips = [str(ip) for ip in ip_range if is_host_up(ip)]

# Save the active IPs to a file
with open("active_ips.txt", "w") as f:
    for ip in active_ips:
        f.write(ip + "\n")

print("Active IPs:", active_ips)
