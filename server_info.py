""" server information collector 
Author     : Utkarsh Srivastava
github     :https://github.com/rajsrivastava-23/system-info-collector.git
created on : 2025-07-23
Description:This python script collects detailed system information including:
            -hostname
            -Ip address
            -Os info &cpu architecture
            -physical & logical cpu cores
            -Total RAM & Disk space
It saves all the details in a clean,timestamped report file(system_info.txt)."""
 
import logging        
import platform
import socket
import psutil
from datetime import datetime

logging.basicConfig(filename="system_info.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
def get_system_info():
    
 timestamp = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
 logging.info(f"System information collected at {timestamp}")
     
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
    
    if __name__ =="__main__":
        get_system_info()
        
print("system info saved to system_info.txt")  


