""" server information collector 
Author     : Utkarsh Srivastava
github     :
created on : 2025-07-23
Description:This python script collects detailed system information including:
            -hostname
            -Ip address
            -Os info &cpu architecture
            -physical & logical cpu cores
            -Total RAM & Disk space
It saves all the details in a clean,timestamped report file(system_info.txt)."""
         
import platform
import socket
import psutil
from datetime import datetime
def get_system_info():
    
 timestamp = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
     
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
os_info = platform.platform()
cpu_architecture = platform.architecture()
physical_cores = psutil.cpu_count(logical=False)
logical_cores = psutil.cpu_count(logical=True)
total_ram = round ( psutil.virtual_memory().total / (1024 ** 3),2)
disk = psutil.disk_usage('/')
total_disk = round(disk.total / (1024 ** 3) , 2) 

with open("system_info.txt", "w") as file:
    file. write(f"hostname: {hostname}\n")
    file.write(f"ip address: {ip_address}\n")
    file.write(f"os info: {os_info}\n")
    file.write(f"cpu architecture: {cpu_architecture}\n")
    file.write(f"physical cores: {physical_cores}\n")
    file.write(f"logical cores:v{logical_cores}\n")
    file.write(f"total ram: {total_ram}gb\n")
    file.write(f"total disk: {total_disk}gn\n")
    
print("system info saved to system_info.txt")  


