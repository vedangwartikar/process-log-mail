import psutil
import os
import sys
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
#from email.MIMEImage import MIMEImage
from email import encoders
import pandas as pd
from collections import defaultdict

#Server-Client email details
from details import *

def process():
	log_dir = "Log"
	if not os.path.exists(log_dir):
		try:
			os.mkdir(log_dir)
		except:
			pass
	separator = '-' * 80
	ct = ""
	currtime = str(time.ctime())
	for i in currtime:
		if i == ':':
			i = '.'
		ct += i
	
	log_path = os.path.join(log_dir, "Process Log at %s.log" %ct)
	fd = open(log_path, 'x')
	fd.write(separator + "\n")
	fd.write("Process Log at "+time.ctime()+"\n")
	fd.write(separator + "\n")
	processlist = []
	pid = []
	vms = []
	name = []

	#df = pd.read_csv('LogData.csv')


	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs = ['pid','name','username'])
			pinfo['vms'] = proc.memory_info().vms / (1024*1024)
			processlist.append(pinfo)
			pid.append(pinfo['pid'])
			vms.append(pinfo['vms'])
			name.append(pinfo['name'])

		except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass

	maxmem = max(vms)
	for element in range(len(name)):
		if vms[element] == maxmem:
			maxname = name[element]
			maxpid = pid[element]
			#maxindex = element
			break

	import matplotlib.pyplot as plt
	plt.plot(pid, vms, 'ro')
	plt.ylabel('Memory usage in MB')
	plt.xlabel('Process ID')
	plt.title("Memory consumption of processes wrt their PIDs")
	plt.annotate(maxname, (maxpid, maxmem))
	plt.savefig('GraphicalLog.png')
	img_path = 'GraphicalLog.png'

	for element in processlist:
		fd.write("%s\n"%element)

	dfDict = defaultdict(list)
	for element in processlist:
		for each in element:
			dfDict[each].append(element[each])
	
	df = pd.DataFrame(dfDict)
	df.to_csv('LogData.csv')
	
	print("Process log succesfully created at ", ct)
	return log_path, img_path

def maillog(emailid, attachpath, img_path):
	fromaddr = fromEmailId
	toaddr = emailid

	msg = MIMEMultipart()

	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Process Log"

	try:
		body = "Process Log details for Acer Predator G3-571"
		msg.attach(MIMEText(body, 'plain'))

# ======================== Attaching Log File ========================

		logFileName = "ProcessLog.log"
	
		logAttachment = open(attachpath, "rb")

		log = MIMEBase('application', 'octet-stream')

		log.set_payload((logAttachment).read())

		encoders.encode_base64(log)

		log.add_header('Content-Disposition', "attachement; filename = %s" %logFileName)

		msg.attach(log)

# ======================== Attaching CSV File ========================

		csvFileName = "LogData.csv"
	
		csvAttachment = open('LogData.csv', "rb")

		csv = MIMEBase('application', 'octet-stream')

		csv.set_payload((csvAttachment).read())

		encoders.encode_base64(csv)

		csv.add_header('Content-Disposition', "attachement; filename = %s" %csvFileName)

		msg.attach(csv)


# ======================== Sending Mail content over SMTP ========================

		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login(fromaddr, fromPassword)
		text = msg.as_string()
		start = time.time()
		s.sendmail(fromaddr, toaddr, text)
		end  = time.time()
		print("Time to send mail:  ", round(end-start, 2), "seconds")
		s.quit()
	except Exception as err:
		print("Error: ", err)

def main():
	print("Process Log mail sender: ")
	attachpath, img_path = process()
	maillog(toEmailId, attachpath, img_path)

if __name__ == '__main__':
	main()	
