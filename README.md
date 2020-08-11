# process-log-mail
__Generate a detailed report of the processes running on the Client and periodically e-mail it to the Server__
- - - -

## Process Log
<div align="center">
    <img src="https://github.com/vedangwartikar/process-log-mail/blob/master/csv.JPG"/>
</div>
<br>
The python script will run at the client-side. It will periodically generate a Log file for all the proceses running on the Clients machine. The log file will contain the name of the process, its user, ProcessID and the virtual memory usage. This file will be e-mailed to the server for further analytical computations. The script will also plot a graph of the memory consumption of these processes wrt to their PIDs. The process with highest memory consumption is tagged.

### Installation

You will need to:

- Install [Python 3](https://www.python.org/downloads/)
- Clone this repo onto your local machine
```bash
$ git clone https://github.com/vedangwartikar/process-log-mail
```
- Go into the project directory and install the requied libraries from the requirements.txt file
```bash
$ pip install -r requirements.txt
```
- Open the file details.json and edit the following fields:
    - fromEmailId - Enter the email-id you want to send the Process Log from
    - fromPassword - Enter the password of email-id you want to send the Process Log from
    - toEmailId - Enter the email-id you want to send the Process Log to
<br>
- Incase you're getting stuck due to access issues while sending the emails, all you need to do is enable less secure apps for the email you are trying to send the email from. Toggle the ON button [here](https://myaccount.google.com/lesssecureapps)
