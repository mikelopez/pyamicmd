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


Usage
------

.. code-block:: python
	from pyamicmd import *
	cl = AMICommand(host="x.x.x.x", user="admin", pwd="password")
	cl.set_command("dialplan show from-internal")
	cl.command()

Response
---------

.. code-block:: 
	>>> for i in cmd.response:
	...     print i
	... 
	[ Context 'from-internal' created by 'pbx_config' ]
	  Include =>        'from-internal-xfer'                          [pbx_config]
	  Include =>        'bad-number'                                  [pbx_config]
	-= 0 extensions (0 priorities) in 1 context. =-
	>>> 
