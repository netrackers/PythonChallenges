import platform
import socket
import os

def computer_name():
    machine_type = platform.machine()
    machine_name = platform.node()
    processor_type = platform.processor()
    system_type = platform.system()
    print('Computer Name: ' + machine_name)
    print('Computer Architecture: ' + machine_type)
    print('Processor Model: '+ processor_type)
    print('Operatinf system family: ' + system_type)

computer_name()
system = os.uname_result(sysname, nodename)
print(system)
