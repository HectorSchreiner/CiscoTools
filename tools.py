import os
import typer
import paramiko
import json

from connection_handlers import *
from netmiko import ConnectHandler
from enum import Enum
from re import findall
from subprocess import Popen, PIPE

scanner_app = typer.Typer()
connector_app = typer.Typer()
app = typer.Typer() 

app.add_typer(scanner_app, name="scan")
app.add_typer(connector_app, name="connect")

@scanner_app.command()
def all():
    ping_count = 2
    for hostname, host in nodes:
        data = ""
        output= Popen(f"ping {host} -n {ping_count}", stdout=PIPE, encoding="utf-8")

        for line in output.stdout:
            data = data + line
            ping_test = findall("TTL", data)

        if ping_test:
            print(f"{hostname} : Successful Ping")
        else:
            print(f"{hostname} : Failed Ping : ip address {host}")

@connector_app.command()
def connect_to_device(connection_handle: Devices):
    connect = ConnectHandler(**connect_to_device)
    connect.enable()

if __name__ == "__main__":
    app()


