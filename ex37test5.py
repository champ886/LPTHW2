import socket

def get_hostname_IP():
    hostname = input("Please enter the hostname or url: ")
    #try:
    print(f"hostname: {hostname}")
    print(f"IP: {socket.gethostbyname(hostname)}")
    #except socket.gaierror as error:
    #    print(f"Invalid hostnmae..error is raised as {error}")



get_hostname_IP()