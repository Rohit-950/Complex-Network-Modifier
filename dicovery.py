import scapy.all as scapy

# Define the IP range to scan
ip_range = "192.168.0.110/24"

# Send an ARP request to the IP range
arp_request = scapy.ARP(pdst=ip_range)
broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
arp_request_broadcast = broadcast/arp_request

try:
    # Send the ARP request and get the responses
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
except scapy.Scapy_Exception as e:
    print(f"Error sending ARP request: {e}")
    exit(1)

# Create a list of devices
devices = []

# Iterate over the responses and extract the device information
for answer in answered_list:
    device_ip = answer[1].psrc
    device_mac = answer[1].hwsrc
    devices.append((device_ip, device_mac))

# Print the list of devices
if devices:
    print("Devices found:")
    for device in devices:
        print(f"IP: {device[0]}, MAC: {device[1]}")
else:
    print("No devices found. Check your network configuration and try again.")