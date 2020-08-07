# process-log-mail
__Generate a detailed report of the processes running on the Client and periodically e-mail it to the Server__
- - - -

## Process Log
<div align="center">
    <img src="https://github.com/vedangwartikar/process-log-mail/blob/master/processLog.JPG"/>
</div>
<br>
The python script will run at the client-side. It will periodically generate a Log file for all the proceses running on the Clients machine. The log file will contain the name of the process, its user, ProcessID and the virtual memory usage. This file will be e-mailed to the server for further analytical computations. The script will also plot a graph of the memory consumption of these processes wrt to their PIDs. The process with highest memory consumption is tagged.

Required dependencies:
* [psutil](https://pypi.org/project/psutil/) - Process utilites
* [smtplib](https://docs.python.org/2/library/smtplib.html) - SMTP protocol module
* [matplotlib](https://matplotlib.org/) - Data visualization with graphs

Above dependencies can be installed using pip command in the python shell.

Refer to the image GraphicalLog.png for graphical visualization of the memory consumption by the processes running on RAM.

The directory 'LogDir' contains multiple Log files with the date and time specified as their filnames.

These files as well as the graphical image will be periodically mailed to the desired e-mail address.
