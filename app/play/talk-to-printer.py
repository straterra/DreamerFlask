#!/usr/bin/python

# Written by Thomas York

# PoC for talking to Dreamer printer via IP

import socket
import re
import time
import signal
import sys


TCP_IP = '192.168.10.23'
TCP_PORT = 8899
BUFFER_SIZE = 1024
MESSAGE = "~M601 S1\r\n"


def signal_handler(signal, frame):
    close_dreamer_connection(s)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def get_percentage(part, whole):
    return 100 * float(part)/float(whole)


def get_dreamer_message_list(socket):
    message = []
    line = ""
    while True:
        part = socket.recv(1)
        line += part
        if line.endswith('\r\n') == True:
            message.append(line)
            if line == 'ok\r\n':
                break
            line = ""

    return message


def get_dreamer_message_string(socket):
    message = ""
    line = ""
    while True:
        part = socket.recv(1)
        line += part
        if line.endswith('\r\n') == True:
            message += line
            if line == 'ok\r\n':
                break
            line = ""

    return message


def start_dreamer_connection(ipv4,tcpport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ipv4, tcpport))
    s.send("~M601 S1\r\n")
    data = get_dreamer_message_string(s)
    if 'Control Success.' not in data:
        s.close
        raise Exception('Printer did not return success to control command M601')
    return s


def get_dreamer_progress(socket):
    s.send("~M27\r\n")
    data = get_dreamer_message_string(s)
    match = re.search(r'.*SD\s*printing\s*byte\s*(\d*)\/(\d*).*', data, re.DOTALL)
    if match.group(1) is not None:
        completed = float(match.group(1))
        total = float(match.group(2))
        percentage = round(get_percentage(completed,total),2)
        return percentage
    else:
        return -1


def close_dreamer_connection(socket):
    s.send("~M602\r\n")
    data = get_dreamer_message_string(s)
    s.close()


def progressBar(value, endvalue, bar_length=20):
    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))
    sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()

s = start_dreamer_connection(TCP_IP, TCP_PORT)
percentage = 0
while percentage < 100:
    percentage = get_dreamer_progress(s)
    progressBar(percentage, 100)
    time.sleep(1)

close_dreamer_connection(s)

print "Print complete!"
