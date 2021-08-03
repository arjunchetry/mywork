import psutil


for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object.
        processName = proc.name()
        processID = proc.pid
        print(processName , ' ::: ', processID)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

print("Using Dictionary ")

listOfProcessNames = list()
# Iterate over all running processes
for proc in psutil.process_iter():
   # Get process detail as dictionary
   pInfoDict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])
   # Append dict of process detail in list
   listOfProcessNames.append(pInfoDict)

