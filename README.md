# Vive-Monitor
A simple python script to monitor the status of your HTC Vive order on 'findmyorder.com' more to come soon...

Run 'main.py' to generate a conf.json. Fill in the required information before adding script to cron job or windows scheduler.

Requirements:

- Python 2.7
- BeautifulSoup
- Selenium
- PhantomJS

Script is meant to be scheduled by cron or windows scheduler. 

####Example cron job for debian/ubuntu:
```
*/20 * * * * python /home/username/vivemonitor/main.py
```
This will run the job every 20 minutes.

## Refrain from running this script often!
