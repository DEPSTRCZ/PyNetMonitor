from apscheduler.schedulers.blocking import BlockingScheduler
from termcolor import cprint
import subprocess
import json
import csv
import os

cprint("╔                ╗","cyan")
cprint("   PyNetMonitor","blue")
cprint("╚                ╝","cyan")
cprint("Tool to long term capture your network speed into csv file. Built around LibreSpeed-CLI","dark_grey")
cprint("● LibreSpeed Organization: https://github.com/librespeed","dark_grey")
cprint("● Info:\nThis tool is built around the LibreSpeed-CLI!\nUses their latest release depending on the target system.\nAll ","dark_grey")
cprint("")
def SpeedTestInterval():
    print("1")
fields = ["Year","Date","Time","Ping","Jitter","Download","Upload","Server,Country"]
rows = []
if not os.path.isfile("SpeedTest.csv"):
    with open("SpeedTest.csv","x") as csvfile:
        writer = csv.writer(csvfile)
        for row in writer:
            writer.writerow(fields)

run = subprocess.run(["librespeed-cli","--csv"],capture_output=True)

result = list(str(run.stdout.decode()).split(","))
if (run.stderr): 
    
server = result[3]
country = result[1][1:]
ping = result[4]
jitter = result[5]
download = result[6]
upload = result[7]
year = result[0][:4]
date = f"{result[0][8:10]}.{result[0][5:7]}"
time = result[0][11:16]
# Print the JSON object
print(country)


with open("SpeedTest.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        rows.append(row)
rows.append([year,date,time,ping,jitter,download,upload,server,country])
with open("SpeedTest.csv","w") as csvfile:
    writer = csv.writer(csvfile) # 4. write the header
    writer.writerows(rows)
print(rows)