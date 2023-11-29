from termcolor import colored as color
import subprocess
import os

class Comm:
    def __init__(self):
        self.user = None        # Import user name from os 
        self.password = None    # if there is sudo access required 
        pass

class NetComs(Comm):
    def __init__(self):
        pass

    # Prototype / Temporary function for getting a pcap file
    def getTCPdumpPCAP(self, filename):
        try:
            command = f"sudo -n tcpdump -G 15 -i en1 -w file.pcap"
            out = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
            stdout, stderr = out.communicate()
            # This 
            print(color('TCPdump file created!', 'green'))
            if stderr:
                throw(stderr)
        except:
            print(color('Error: {}'.format(stderr), 'red'))

    def zeekListen(self):
        try:
            command = 'sudo zeek -i en'
            out = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = out.communicate()
            print(color(f'Zeek is listening! {stdout}', 'green'))
        except:
            print(color('Error: {}'.format(stderr), 'red'))
        

    def createDNSLogs(self, filename, o_file=None):
        try:
            # this should not stay hardcoded, this should be updated to 
            # provide a dynamic filepath that will use the python package
            # os to get the user name!
            filepath = os.getcwd()

            # generates .log files from .pcap files
            command = "mkdir logs | zeek -r {}{} Log::default_logdir=logs".format(filepath, filename)
            out = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = out.communicate()
            print(color('DNS log created by Zeek! From filepath: {}'.format(filepath), 'green'))
        except:
            print(color('Error: {}'.format(stderr), 'red'))
        

    def cleanLog(self, filename, zeekcut, newFilename):
        try:
            filepath = os.getcwd()
            # this should not stay hardcoded, try using os to get the user name and the filepath!
            command = 'cat {}/logs/dns.log | {} query | sort | uniq -c | sort -n > {}'.format(filepath, zeekcut, 'clean_dns.log')

            out = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = out.communicate()
            print(color('DNS log processed!', 'green'))
            if stderr:
                throw(stderr)
        except:
            print(color('Error: {}'.format(stderr), 'red'))
    
# 

    def getDNSLogs(self, filename, filepath):
        with open('{}{}'.format(filepath, filename), 'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line)


if __name__ == '__main__':

    # Test Case for Blake
    net = NetComs()
    # net.getTCPdumpPCAP('file')
    net.zeekListen()
    # net.createDNSLogs('file.pcap') # 
    # net.cleanLog('dns.log', '/opt/homebrew/bin/zeek-cut', "clean_dns")
    # net.getDNSLogs('clean_dns.log', '/Users/evan/cnm/server/')

    # Commands to ues:
    # tcpdump -w file.pcap
    # zeek -r /Users/<user>/<file>.pcap
    # less -S <file>.log
    # cat dns.log | /opt/homebrew/bin/zeek-cut query | sort | uniq -c | sort -n
    # cat dns.log | /opt/homebrew/bin/zeek-cut query | sort | uniq -c | sort -n | tail -n 10

    pass