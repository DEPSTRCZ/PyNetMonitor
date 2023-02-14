# PyNetMonitor
> Tool to long term capture your network speed and uptime into csv file. Built around LibreSpeed-CLI

## 🚧 NOTICE 🚧
> This tool is built around the LibreSpeed-CLI!
> This is only Tool/Script to capture the output of it in interval to csv file
> Uses their latest release depending on the target system.
> The LibreSpeed-CLI is not mine and it is a program developed by LibreSpeed.
> I DO NOT take any credit related to program LibreSpeed-CLI
> This tool is not associated with LibreSpeed Organization!
> Tool is under GPL-3.0 license! (https://raw.githubusercontent.com/DEPSTRCZ/PyNetMonitor/main/LICENSE)

## 🦺 Functions
  > Capture speeds of your network in intervals
  > Check when your network goes down (Also in interval)
  > Capture Download, Upload, Jitter, Ping

## 🚩 Requirements
  > - Python knowledge required!
  > - Python3
  > - Pip
  > Dependencies:
  > - apscheduler
  > - termcolor
  > - ping3


## 📖 How to use
1. Go to: https://github.com/DEPSTRCZ/PyNetMonitor/releases
2. Download Release depending on your OS
3. Extract
4. Open ``PyNetMonitor-run.py`` with your editor
5. Edit the config to values you want.
  > ``SpeedTest`` Enables/Disables SpeedTest Monitor. Example: ``SpeedTest = True`` False to disable.

  > ``SpeedTest_interval`` Interval how often should the SpeedTest Monitor run. In Seconds. Example: ``SpeedTest_interval = 120`` = Every 120 seconds

  > ``host`` Domain/IP you want to ping (Ping Check/Uptime check) Leave empty to disable PingCheck Monitor. Example: ``host = "google.com"``

  > ``host_interval`` Interval how often should the Ping Check/Uptime Check Monitor run. In Seconds. Example: ``host_interval = 15`` = Every 15 seconds
6. Save the file
7. Install the needed dependencies
> ``pip install apscheduler termcolor ping3``
