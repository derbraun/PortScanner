# PortScanner
This Port Scanner was written in Python 3

Tested in Python 3 for Windows

---
This script does the following:
+ Takes the following input from the user via cmdline args or at runtime:
    + Host
    + Ports
    + Protocols
    
+ Allows more than one host to be scanned
    + Reads a range of IPs from the command line
    + Allows specific hosts to be read different ways
        + Subnet
        + Range
        
+ Allows multiple ports be specified
    + Range
    + List of ports separated by a comma

+ Uses the following Protocols
    + TCP
    + UDP
    + ICMP
    
+ Outputs results to both command line and an HTML file

+ Includes a Usage or Help page

---
Commands to Run This Python Script:
+ portscanner.py
    + Will ask for host, port, and protocol
    
    
+ portscanner.py -h
    + Will give you the usage message


+ portscanner.py < host IP > < ports > < protocol >
    + Protocol is optional
    + Default Protocol is TCP
---
Examples:

+ portscanner.py
+ portscanner.py 192.168.186.1 80
+ portscanner.py 127.0.0.1-255 80,443 
+ portscanner.py 192.168.0.0/24 20-30 udp
+ portscanner.py 127.0.0.1-255 1-1000 icmp

*Note: when the icmp protocol is chosen, you still need to specify some ports, even though they are not used*

    