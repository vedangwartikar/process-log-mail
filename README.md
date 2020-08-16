# process-log-mail
__Generate a detailed Log Report of the processes running on the Client and e-mail it to the Server__
- - - -

## Process Log
<div align="center">
    <img src="https://github.com/vedangwartikar/process-log-mail/blob/master/csv.JPG"/>
</div>
<br>
The python script will run on the client-side. It will periodically generate a Log file for all the processes running on the Clients machine. The log file(txt and csv) will contain multiple information such as name of the process, its user, ProcessID, virtual memory usage(MB), etc. This file will be e-mailed to the server for further analytical computations. The script will also plot a graph of the memory consumption of these processes wrt to their PIDs. The process with highest memory consumption is tagged.

### Installation and Execution

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
- You need to let gmail services know that the automation script you are running is secure and safe.
    - Toggle the ON button [here](https://www.google.com/settings/security/lesssecureapps) 
- Finally, execute the main file
```bash
$ python ProcessLog.py
```
#### Show your support

Give a try! ⭐️ it this project helps you.