import serial
import os, datetime

cc128 = serial.Serial("/dev/ttyUSB0", 57600, timeout=60)
cc128xml = cc128.readlines(6)
try:
    # Find the temperature
    tmprstart=cc128xml[0].find("<tmpr>")+len("<tmpr>")
    tmprend=cc128xml[0].find("</tmpr>",tmprstart)
    tmpr=float(cc128xml[0][tmprstart:tmprend])
    # Find ch1
    ch1start=cc128xml[0].find("<ch1>")+len("<ch1>")
    ch1end=cc128xml[0].find("</ch1>",ch1start)
    ch1=cc128xml[0][ch1start:ch1end]
    # Find the power in watts
    wattsstart=ch1.find("<watts>")+len("<watts>")
    wattsend=ch1.find("</watts>",wattsstart)
    watts=int(ch1[wattsstart:wattsend])
    now = datetime.datetime.now()
    output = str(now) + "," + str(tmpr) + "," + str(watts) + "\r\n"
    print output
except:
    print cc128xml
logging = open('/var/www/data/cc128.log', 'a')       # Open cc128.log for writing
logging.write(output)                           # Write data
logging.close()                                 # Close the log
