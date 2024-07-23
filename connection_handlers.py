from enum import Enum

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

BorderRouter = {
    "host": "10.5.0.2",
    "username": "Brucewayne",
    "password": "op10muserPrime!",
    "secret": "$cisco!!CON*",
    "device_type": "cisco_ios",
}

class Devices(Enum):
    BorderRouter = BorderRouter,

