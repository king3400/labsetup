import os
import sys

# Get the hostname and domain name from the command line arguments
if len(sys.argv) != 3:
    print("Usage: python3 set_hostname.py <hostname> <domain>")
    sys.exit(1)

hostname = sys.argv[1]
domain = sys.argv[2]

# Set the new hostname and domain name
os.system(f"sudo hostnamectl set-hostname {hostname}.{domain}")
os.system(f"sudo sed -i 's/^127.0.1.1.*/127.0.1.1\t{hostname}.{domain} {hostname}/' /etc/hosts")

# Restart the networking service
os.system("sudo systemctl restart systemd-networkd")