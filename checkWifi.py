import socket
import platform
import os
import subprocess
#
# Objectives:
# -> Who else is connected locally
# ->Get their IP, MAC address, vendor device name, localhost name
#

# 1- Function getMyLocalIP()
# 2- Get IP addresses mask
# Ping all IP addresses in the range
# List ARP
# Match MAC <> Vendor name
#
#
# 1- Function getMyLocalIP()
def getMyLocalIP():
    # Get the local hostname
    local_hostname = socket.gethostname()
    
    # Get a list of IP addresses associated with the hostname
    ip_addresses = socket.gethostbyname_ex(local_hostname)[2]

    # Exclude IPs starting with "127." and also NordVPN local IP "192.168.56.1" 
    cleaned_ips = [ip for ip in ip_addresses if not (ip.startswith("127.") or ip=="192.168.56.1")]

    # Extract the first IP address (if available) from the filtered list.
    first_ip = cleaned_ips[:1]
    
    # If not available, exit
    if first_ip == []:
        local_ip = "Not available"
    
    # Print the obtained IP address to the console.
    else:
        local_ip = first_ip[0]

    return local_ip

# 2- Function getMaskFromIP(ip)
def getMaskFromIP(ip):
    return '.'.join(ip.split('.')[0:3])

# 3- Function ping(host)
def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0

Local_IP = getMyLocalIP()
if Local_IP == "Not available":
    print("Local IP not available yet. Exiting.")
    exit()

local_mask = getMaskFromIP(Local_IP)

print("Local IP: ", Local_IP)
print("Mask: ", local_mask)

### WORK IN PROGRESS ###
# Iterate PING from Mask.1 to Mask.254
#for i in range(1,255):
#    temp_host = local_mask + "." + str(i)
#    ping(temp_host)
### WORK IN PROGRESS ###

