import subprocess
import json
import csv
import os
run = subprocess.run(["librespeed-cli","--json"],capture_output=True)

result = json.loads(run.stdout.decode())

server = result[0]["server"]["url"]
ping = result[0]["ping"]
jitter = result[0]["jitter"]
download = result[0]["download"]
upload = result[0]["upload"]
# Print the JSON object

fields = ["Date","Time","Ping","Jitter","Download","Upload"]
rows = []
if not os.path.isfile("SpeedTest.csv"):
    with open("SpeedTest.csv","w") as csvfile:
        writer = csv.writer(csvfile)
        for row in writer:
            writer.writerow(fields)
with open("SpeedTest.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        rows.append(row)
rows.append([server,ping,jitter,download,upload])
with open("SpeedTest.csv","w") as csvfile:
    writer = csv.writer(csvfile) # 4. write the header
    writer.writerows(rows)
print(rows)