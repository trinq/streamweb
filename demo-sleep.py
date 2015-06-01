import time
 
print "*** Hit CTRL+C to stop ***"
 
## Star loop ##
while True:
        ### Show today's date and time ##
	print "Current date & time " + time.strftime("%c")
 
        #### Delay for 1 seconds ####
        time.sleep(1)