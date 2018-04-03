import os
import subprocess
procId = subprocess.Popen('adb shell', stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
stdout, stderr = procId.communicate('dumpsys location\nexit\n')
output_string = stdout.decode('utf-8')
output_string = output_string.strip()
results = output_string.split('\n')
coordinates = results[35].split(' ')[6]
print ("GPS Coordinates: " +coordinates)
