import os
import subprocess
procId = subprocess.Popen('adb shell', stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
stdout, stderr = procId.communicate('dumpsys location\nexit\n')
output_string = stdout.decode('utf-8')
output_string = output_string.strip()
results = output_string.split('\n')
coordinates = results[46].split(' ')[6]
print ("GPS Coordinates: " +coordinates)

procId = subprocess.Popen('adb shell', stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
stdout, stderr = procId.communicate('dumpsys telephony.registry\nexit\n')
result = stdout.split('\n')
networkname = result[23].split(' ')[8]
networkstrength = result[24].split(' ')
print ("Networkname is : " +networkname)
print networkstrength[2],networkstrength[3],networkstrength[4],networkstrength[5],networkstrength[6],networkstrength[7],networkstrength[8],networkstrength[9],networkstrength[10],networkstrength[11]
