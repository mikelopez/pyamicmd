Readme for pyamicmd
------------------------------
Small python app based on amiwrapper that sends a command to Asterisk via AMI.

``from pyamicmd import *``


Requirements
-------------
Based on starpy and amiwrapper. See requirements.txt for more details


Settings
---------
Create a local_settings.py file with the following auth variables.
 - PBX = the host (ip or name) of th system
 - AMI_USER = the AMI user account to log in with
 - AMI_PASS = the password for the AMI user
