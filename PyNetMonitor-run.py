from apscheduler.schedulers.blocking import BlockingScheduler
from termcolor import cprint
import subprocess
import csv
import os
import ping3
import datetime
import json
ping3.EXCEPTIONS = True
# CONFIG SECTION!
# CONFIG SECTION!
# CONFIG SECTION!
SpeedTest = True # Set to disable change the value to False
SpeedTest_interval = 120 # Interval in which the SpeedTest should be run  [IN SECONDS] (Default 60 = every 1 minute)

host = "google.com" # To disable leave blank
host_interval = 10  # Interval in which the PingCheck should be run  [IN SECONDS] (Default 15 = every 15 seconds)
# END OF CONFIG SECTION!
# END OF CONFIG SECTION!
cprint("╔                ╗","cyan")
cprint("   PyNetMonitor","blue")
cprint("╚                ╝","cyan")
cprint("Tool to long term capture your network speed and uptime into csv file. Built around LibreSpeed-CLI","dark_grey")
cprint("● LibreSpeed Organization: https://github.com/librespeed","dark_grey")
cprint("● LibreSpeed-CLI repo & Source Code: https://github.com/librespeed/speedtest-cli","dark_grey")
cprint("● LibreSpeed-CLI Licence: https://raw.githubusercontent.com/librespeed/speedtest-cli/master/LICENSE","dark_grey")
cprint("● Tool is under GPL-3.0 license! (https://raw.githubusercontent.com/DEPSTRCZ/PyNetMonitor/main/LICENSE)","dark_grey")
cprint("● Tool: © Jiří Edelmann | © DEPSTRCZ","dark_grey")
cprint("● Notice:\n   This tool is built around the LibreSpeed-CLI!\n   Uses their latest release depending on the target system.\n   The LibreSpeed-CLI is not mine and it is a program developed by LibreSpeed.\n   This is only Tool/Script to capture the output of it in interval to csv file.","dark_grey")

cprint("Initializing...","yellow")

headers_speedtest = ["Year","Date","Time","Ping","Jitter","Download","Upload","Server"]
headers_pingcheck = ["Online","Year","Date","Time","Ping","Host","Error"]
scheduler = BlockingScheduler(Standalone=True)

def init(file,headers):
    if not os.path.isfile(file):
        with open(file, "a",newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            csvfile.close()

def writerows(file,content):
    with open(file,"a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(content)
        csvfile.close()

def SpeedTestInterval():
    init("SpeedTest.csv",headers_speedtest)
    dateobject = datetime.datetime.now()
    year = str(dateobject.year)
    date = dateobject.date().strftime("%d.%m")
    time = dateobject.time().strftime("%H:%M")

    run = subprocess.run(["librespeed-cli","--json"],capture_output=True)

    if (run.stderr):
        rows = [year,date,time,"X","X","X","X","Unreachable"]
        return writerows("SpeedTest.csv",rows)
    
    result = json.loads(run.stdout.decode())

    server = result[0]["server"]["url"]
    ping = result[0]["ping"]
    jitter = result[0]["jitter"]
    download = result[0]["download"]
    upload = result[0]["upload"]

    rows = [year,date,time,ping,jitter,download,upload,server]
    writerows("SpeedTest.csv",rows)

def PingCheckInterval():
    init("PingCheck.csv",headers_pingcheck)
    try:
        check = ping3.ping(host, unit="ms")
        check = str(round(check, 2))+"ms"
        online = "True"
        error = "None"
    except ping3.errors.HostUnknown:
        check = 0
        error = "Host Unreachable or Unkown"
        online = "False"
        
    dateobject = datetime.datetime.now()
    year = str(dateobject.year)
    date = dateobject.date().strftime("%d.%m")
    time = dateobject.time().strftime("%H:%M")

    rows = [online,year,date,time,check,host,error]
    writerows("PingCheck.csv",rows)

if SpeedTest_interval < 120:
    cprint("ERROR: SpeedTest_Interval(Config) must be bigger than 120!","red")
    quit()
elif host_interval < 10:
    cprint("ERROR: host_interval(Config) must be bigger than 10!","red")
    quit()
if host == "" and SpeedTest == False:
    cprint("ERROR: Both config options are disabled! Enable atleast one!","red")
    quit()
elif host and SpeedTest == True:
    cprint("Both monitors started!","green")
    init("SpeedTest.csv",headers_speedtest)
    init("PingCheck.csv",headers_pingcheck)
    scheduler.add_job(PingCheckInterval, "interval", seconds=15)
    scheduler.add_job(SpeedTestInterval, "interval", seconds=60)
elif not host == "":
    print("s")
    scheduler.add_job(PingCheckInterval, "interval", seconds=15)
    cprint("PingCheck started!","green")
    init("PingCheck.csv",headers_pingcheck)
elif SpeedTest == False:
    scheduler.add_job(SpeedTestInterval, "interval", seconds=60)
    cprint("SpeedTest monitor started!","greem")
    init("SpeedTest.csv",headers_speedtest)
        
try:
    scheduler.start()
except KeyboardInterrupt:
    scheduler.shutdown(wait=False)