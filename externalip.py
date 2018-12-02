import socket
import subprocess
 # function to scan network and display IPs of conected devices
def scan_network():
    scanner = PortScanner()
    myIP = subprocess.check_output(['hostname -I'], shell=True)
    myIP = str(myIP, 'utf-8').split('.')
    print(myIP[:3])
    scannedData = scanner.scan(hosts = '.'.join(myIP[:3]) + '.1/24', arguments = '-sP')
     # printing all the IP addresses of connected devices
    for hostnames in scannedData['scan']:
        print(hostnames)
        
scan_network()
