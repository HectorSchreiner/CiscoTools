import os
import typer
import paramiko
import json

from enum import Enum
from re import findall
from subprocess import Popen, PIPE


app = typer.Typer() 
nodes = [
    ("DSW1", "10.1.4.6"),
    ("DSW2", "10.1.4.10"),
    ("Core Router g0/0/0 ", "10.1.4.5"), 
    ("Core Router g0/0/1", "10.1.4.9"), 
    ("Border Router g0/0/0", "10.5.0.2"), 
    ("Border Router g0/0/1", "10.11.0.1"), 
    ("ASA0", "10.11.0.2"),
    ("Google.com", "8.8.8.8")
]

@app.command()
def device_scanner(ping: bool = False):
    if ping == True:
        scan_hosts(nodes, 1)

@app.command()
def borderrouter(borderRouter: bool = False):
    login_command = "enable \n"
    if borderRouter == True:
        run_command_on_device("10.5.0.2", "Brucewayne", "op10muserPrime!", "$cisco!PRIV*" )
    
    
def scan_hosts(hosts, ping_count):
    for hostname, host in hosts:
        data = ""
        output= Popen(f"ping {host} -n {ping_count}", stdout=PIPE, encoding="utf-8")

        for line in output.stdout:
            data = data + line
            ping_test = findall("TTL", data)

        if ping_test:
            print(f"{hostname} : Successful Ping")
        else:
            print(f"{hostname} : Failed Ping : ip address {host}")

def run_command_on_device(ip, username, password, enable_password, command):
    ssh = paramiko.SSHClient()

    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username, password, look_for_keys=False)
    #run command
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("enable")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(enable_password)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    output = ssh_stdout.readlines()

    ssh.close()
    return output

app()


