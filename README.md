# Ookla Speedtest Scheduler
A python 3 script for running Ookla's CLI application in a schedule and logging test results.

### Running The Application

1. Set the FILE_PATH variable for the 'speedtest' executable
2. Set SERVER_ID variable for the server that the test will always run on
3. Run the code: python3 speedtest.py
4. Test results are output to 'results' file

### Notes

Designed to work with the already existing 'Speedtest CLI' found at:
* https://www.speedtest.net/apps/cli

Working and tested with the Windows 1.0.0 version:
* Download: https://bintray.com/ookla/download/download_file?file_path=ookla-speedtest-1.0.0-win64.zip

Ookla Server IDs List:
* https://c.speedtest.net/speedtest-servers-static.php