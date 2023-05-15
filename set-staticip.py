import os

# Set the static IP address range for enp0s8
static_ip = "192.168.83.10"
netmask = "24"
gateway = "192.168.83.1"
dns = "8.8.8.8"

# Replace with the desired hostname and domain name
hostname = "ubuntunode1"
domain = "testlab.com"

username = "cambridge"

# Create a new configuration file
config_file = open("/etc/netplan/01-network-manager-all.yaml", "w")

# Write the YAML configuration to the file
config_file.write(f"""
network:
  version: 2
  renderer: networkd
  ethernets:
    ens33:
      dhcp4: yes
    ens38:
      addresses: [{static_ip}/{netmask}]
      gateway4: {gateway}
      nameservers:
        addresses: [{dns}]
""")

# Close the file
config_file.close()

# Apply the new configuration
os.system("sudo netplan apply")



# Set the new hostname and domain name
os.system(f"sudo hostnamectl set-hostname {hostname}")
os.system(f"sudo sed -i 's/^127.0.1.1.*/127.0.1.1\t{hostname}.{domain} {hostname}/' /etc/hosts")

# Restart the networking service
os.system("sudo systemctl restart systemd-networkd")

# adding user cambridge to sudoer 
os.system(f"sudo usermod -aG sudo {username}")
