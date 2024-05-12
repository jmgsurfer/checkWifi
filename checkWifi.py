import socket
#
# Objectives:
# -> Who else is connected locally
# ->Get their IP, MAC address, vendor device name, localhost name
#
# Function getMyLocalIP()
# Get IP addresses mask
# Ping all IP addresses in the range
# List ARP
# Match MAC <> Vendor name
#
# Get the local hostname
local_hostname = socket.gethostname()

# Get a list of IP addresses associated with the hostname
ip_addresses = socket.gethostbyname_ex(local_hostname)[2]

# Exclude IPs starting with "127."
cleaned_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]

# Extract the first IP address (if available) from the filtered list.
first_ip = cleaned_ips[:1]

# If not available, exit
if first_ip == []:
    print("Local ip not available yet. Exiting.")
    exit()

# Print the obtained IP address to the console.
print(first_ip[0])

