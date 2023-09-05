import os
import subprocess
#subprocess.Popen("whoami", shell=True)
AName = input("Name of the Application: ")
os.system("mkdir "+ AName)
os.system("cd " + AName)
os.system("pwd")
nips = int(input("Number of IPs in Scope: "))
file = open('IP.txt', 'a')
for i in range(0,nips):
    ips = input("Enter the IP: ")
    file.write(ips)
    file.write("\n")
file.close() 
#os.system("mv IP.txt "+ AName)
os.system("nmap -sV -sT -v -Pn -n -T4 -p- -iL IP.txt -oA TCP_"+AName)
os.system("sudo nmap -sV -Pn -n -sU -p 49,53,67,68,69,88,113,118,123,135,137,138,139,143,156,161,162,194,213,220,264,389,444,500,514,520,530,563,1194,1293,1434,1512,1645,1646,1812,3306,3389,5060,5061,5432 -iL IP.txt -oA UDP_"+AName)
os.system("mv TCP_"+AName+" "+AName)
os.system("mv UDP_"+AName+" "+AName)