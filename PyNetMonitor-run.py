from apscheduler.schedulers.blocking import BlockingScheduler
from termcolor import cprint
import subprocess
import csv
import os

cprint("╔                ╗","cyan")
cprint("   PyNetMonitor","blue")
cprint("╚                ╝","cyan")
cprint("Tool to long term capture your network speed into csv file. Built around LibreSpeed-CLI","dark_grey")
cprint("● LibreSpeed Organization: https://github.com/librespeed","dark_grey")
cprint("● LibreSpeed-CLI repo & Source Code: https://github.com/librespeed/speedtest-cli","dark_grey")
cprint("● LibreSpeed-CLI Licence: https://github.com/librespeed/speedtest-cli/blob/master/LICENSE","dark_grey")
cprint("● Notice:\n   This tool is built around the LibreSpeed-CLI!\n   Uses their latest release depending on the target system.\n   The LibreSpeed-CLI is not mine and it is a program developed by LibreSpeed.\n   This is only Tool/Script to capture the output of it in interval to csv file.","dark_grey")
cprint("Monitor Started..","green")
fields = ["Year","Date","Time","Ping","Jitter","Download","Upload","Server","Country"]
def SpeedTestInterval():
    if not os.path.isfile("SpeedTest.csv"):
        with open("SpeedTest.csv","a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fields)

    run = subprocess.run(["librespeed-cli","--csv"],capture_output=True)

    result = list(str(run.stdout.decode()).split(","))
    if (run.stderr):
        print("error") 
    
    server = result[3]
    country = result[1][1:]
    ping = result[4]
    jitter = result[5]
    download = result[6]
    upload = result[7]
    year = str(result[0][:4])
    date = f"{result[0][8:10]}.{result[0][5:7]}"
    time = result[0][11:16]

    rows = [year,date,time,ping,jitter,download,upload,server,country]
    with open("SpeedTest.csv","a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(rows)

scheduler = BlockingScheduler()
scheduler.add_job(SpeedTestInterval, "interval", hours=1)
scheduler.start()