import subprocess
import re
from datetime import datetime
import json

from apscheduler.schedulers.blocking import BlockingScheduler

# File path of the speedtest.exe file
FILE_PATH = 'speedtest.exe'
# Id for the server that you want to use
SERVER_ID = '18769'
# filename for result output
OUTPUT_FILE = 'results'

scheduler = BlockingScheduler()

def speedtest(path, server):
    output = subprocess.getoutput([path, '-s', server])

    latency_ms = re.findall(r'Latency:\ *([0-9]+.[0-9]+) ms', output)
    download_Mbps = re.findall(r'Download:\ *([0-9]+.[0-9]+) Mbps', output)
    download_Kbps = re.findall(r'Download:\ *([0-9]+.[0-9]+) Kbps', output)
    upload_Mbps = re.findall(r'Upload:\ *([0-9]+.[0-9]+) Mbps', output)
    upload_Kbps = re.findall(r'Upload:\ *([0-9]+.[0-9]+) Kbps', output)
    packet_loss = re.findall(r'Packet Loss:\ *([0-9]+.[0-9]+)%', output)

    result = {}

    result['date_time'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    result['latency'] = latency_ms[0]
    if len(download_Mbps) > 0:
        result['download_Mbps'] = download_Mbps[0]
    elif len(download_Kbps) > 0:
        result['download_Kbps'] = download_Kbps[0]
    if len(upload_Mbps) > 0:
        result['upload_Mbps'] = upload_Mbps[0]
    if len(upload_Kbps) > 0:
        result['upload_Kbps'] = upload_Kbps[0]
    result['packet_loss'] = packet_loss[0]

    return result

def run_test():
    results = open(OUTPUT_FILE, "a")
    results.write(json.dumps(speedtest(FILE_PATH, SERVER_ID)) + "\n")
    results.close()

run_test()

# This will run based on the schedule (every hour)
@scheduler.scheduled_job('interval', hours=1)
def timed_job():
    run_test()

scheduler.start()
