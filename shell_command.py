import subprocess

#this command returns the temperature of the CPU in RPi
subprocess.call(["/opt/vc/bin/vcgencmd","measure_temp"])
