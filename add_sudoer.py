import os
import sys

# Get the username from the command line argument
if len(sys.argv) != 2:
    print("Usage: python3 add_sudoer.py <username>")
    sys.exit(1)

username = sys.argv[1]

# Add the user to the sudo group
os.system(f"sudo usermod -aG sudo {username}")