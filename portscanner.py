#   Assignment 3
#
#   This port scanner was written by: Daniel Brown
#
#   This script was written for Python 3
#
#   GitHub: https://github.com/derbraun/PortScanner


import socket
import sys
import subprocess
import re

def printUsage():
    """This function prints out the usage message for this script"""
    print("-" * 60)
    print("Usage: \n You may run this script two ways")
    print(" 1. portscanner.py \n 2. portscanner.py <host> <ports> {optional:protocol}")
    print("-" * 60)

    print("Accepted hosts: \n You need to give me the ip addresses")
    print(" I will accept the following: \n an IP (10.1.1.1) \n a subnet (10.1.1.0/24) \n a range (10.1.1.1-255)")
    print("-" * 60)

    print("Accepted ports: \n I will accept the following: \n a single port (25)")
    print("a starting port and an ending port separated by a dash (1-25)")
    print("a string of selected ports separated by a comma (22,25)")
    print("-" * 60)

    print("Accepted protocols: \n I will accept the following: \n TCP , UDP , ICMP")
    print(" If no argument is given, the scanner will choose TCP as default")
    print(" If ICMP is given, the port numbers will be ignored")
    print("-" * 60)

    return


def scan(currentHost, p, htmlFile):
    if proto == "tcp":
        # Scan the port using TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((currentHost, p))
        if result == 0:
            print("Port {}:      Open".format(p))
            htmlFile.write("<p> Port ")
            htmlFile.write(str(p))
            htmlFile.write(":      Open </p>")
        sock.close()

    elif proto == "udp":
        # Scan the port using UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        result = sock.connect_ex((currentHost, p))
        if result == 0:
            print("Port {}:      Open".format(p))
            htmlFile.write("<p> Port ")
            htmlFile.write(str(p))
            htmlFile.write(":      Open </p>")
        sock.close()

    return


arguments = len(sys.argv) - 1
host = None
port = None
proto = "tcp"
portList = []


if arguments >= 2:
    host = sys.argv[1]
    port = sys.argv[2]

    if arguments == 3:
        proto = sys.argv[3]

elif arguments == 0:
    host = input("Enter a remote host to scan: ")
    port = input("Enter a range of ports to scan")

else:
    printUsage()
    exit()

# Open HTML file
htmlFile = open("Scan Report.html", "w")
html_header = """<html>
<head></head>
<body>
<h1> Scanning Report </h1>
<hr>
"""

html_footer = """
</body>
</html>"""

htmlFile.write(html_header)

# set default start and end port values
start = port
end = port

# Separate starting and ending ports
if "-" in port:
    start, end = port.split("-")

elif "," in port:
    portList = port.split(",")

try:

    # Split up the ip address
    sub1, sub2, sub3, sub4 = host.split(".")

    # Beginning and ending of subnet
    sBegin = sub4
    sEnd = sub4

    # Splitting ranges
    if "/" in host:
        sBegin, sEnd = sub4.split("/")

    elif "-" in host:
        sBegin, sEnd = sub4.split("-")

    # For each host
    for h in range(int(sBegin), int(sEnd) + 1):

        currentHost = sub1 + "." + sub2 + "." + sub3 + "." + str(h)

        if proto == "icmp":
            # ping the host
            ping = subprocess.Popen(["ping", currentHost],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)

            out, error = ping.communicate()
            output = out.decode("utf-8")
            print(output)
            htmlFile.write("<h3> Ping on IP(s) ")
            htmlFile.write(host)
            htmlFile.write(" successful </h3>")
            htmlFile.write(output)

        elif not portList:
            # For each port on current host
            for p in range(int(start), int(end) + 1):
                scan(currentHost, p, htmlFile)

        else:
            for p in portList:
                scan(currentHost, int(p), htmlFile)

    # Finish the report
    htmlFile.write(html_footer)
    htmlFile.close()

except KeyboardInterrupt:
    print("Process stopped. Exiting.")
    htmlFile.write("<h3> Error: </h3>")
    htmlFile.write("<p>Keyboard Interrupt given. Program quit</p>")
    htmlFile.write(html_footer)
    htmlFile.close()
    sys.exit(1)

except socket.gaierror:
    print("Hostname could not be resolved. Exiting.")
    htmlFile.write("<h3> Error: </h3>")
    htmlFile.write("<p>Hostname could not be resolved. Program quit</p>")
    htmlFile.write(html_footer)
    htmlFile.close()
    sys.exit(2)

except socket.error:
    print("Couldn't connect to server")
    htmlFile.write("<h3> Error: </h3>")
    htmlFile.write("<p>Couldn't connect to server. Program quit</p>")
    htmlFile.write(html_footer)
    htmlFile.close()
    sys.exit(3)






