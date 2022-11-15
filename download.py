# Import subprocess library.
import subprocess

amnt = 10

# Print empty line
print('\n')

# Start bulk downloading at the same time.
subprocess.Popen(["py", "scrapers/google.py", "gtx 1060", str(amnt)])
subprocess.Popen(["py", "scrapers/brave.py", "gtx 1060"])
subprocess.Popen(["py", "scrapers/google.py", "rtx 2080 ti", str(amnt)])
subprocess.Popen(["py", "scrapers/brave.py", "rtx 2080 ti"])
subprocess.Popen(["py", "scrapers/google.py", "rtx 2070", str(amnt)])
subprocess.Popen(["py", "scrapers/brave.py", "rtx 2070"])
subprocess.Popen(["py", "scrapers/google.py", "rtx 3060 ti", str(amnt)])
subprocess.Popen(["py", "scrapers/brave.py", "rtx 3060 ti"])