# MailPersist - Post-exploitation script for OS X persistance 

## ABOUT:
This script creates a new rule in the OS X Mail application to automatically trigger an appleScript payload when an email is recieved using a trigger word in the subject of the email.

For increased stealth, The trigger email will be deleted before it is visible.  The Script Monitor will also be killed imediately after executing the python stager. There should not be any visual indicators. 

## INSTALL:

All dependancies are met on a default installation of OS X.  With that said, you will likely want to use EmPyre to create your AppleScript payload. 
https://github.com/adaptivethreat/EmPyre

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

When pasting the AppleScript payload from Empire, you need to make two modifications:
- Double up the backslash characters
- Remove the final double quote 


