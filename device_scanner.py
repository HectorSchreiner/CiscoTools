from re import findall
from subprocess import Popen, PIPE

def ping (hosts, ping_count):

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

nodes = [("DSW1", "10.1.4.6"),("DSW2", "10.1.4.10"),("Core Router g0/0/0 ", "10.1.4.5"), ("Core Router g0/0/1", "10.1.4.9"), ("Border Router g0/0/0", "10.5.0.2"), ("Border Router g0/0/1", "10.11.0.1"), ("ASA0", "10.11.0.2"),("Google.com", "8.8.8.8")]

ping(nodes,2)