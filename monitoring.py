import psutil

# Get the network I/O statistics
net_io = psutil.net_io_counters()

# Print the network I/O statistics
print(f"Bytes sent: {net_io.bytes_sent}")
print(f"Bytes received: {net_io.bytes_recv}")
print(f"Packets sent: {net_io.packets_sent}")
print(f"Packets received: {net_io.packets_recv}")