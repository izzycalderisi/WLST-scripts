## START VAR SECTION 
import datetime
import smtplib
import getopt
import socket
import time 
from java.io import FileInputStream
propInputStream = FileInputStream("D:/CSUPSoft/scripts/wlst/domainDetails.properties")
configProps = Properties()
configProps.load(propInputStream)
# in miliseconds
waitTime=900000
#waitTime=100000
waitTime2=10000
#Threshold set to 1.6GB or roughly 80% of our JVM limit 
#THRESHOLD=1900000000 
# Test THRESHOLD set to .5 GB
#THRESHOLD=500000000
#eventually the URL will have to be a flat file which will contain all the entries for each PIA domain on the box
#the script will loop through each value in the flat file and run this code
#url = "t3://10.4.41.222:80"
## START EMAIL PARMS 
host = (socket.gethostname())

#for infinite loop
var = 1
## END EMAIL PARMS 
## END VAR SECTION 



def email(addy,host,tyme,uso,freepcnt2):
        
	
        now = datetime.datetime.now()
        tiempo = str(now)[:16]
        sender = '*******'
	receiver = '*******'




	myemail = """
	To: Weblogic Admins
	Subject:    Notification of Memory Alert for %(jeje)s on %(juju)s 
	 
	PIA domain  %(jeje)s has exceeded a memory threshold of %(limit)s"""   % {'jeje': addy, 'juju': host, 'tiemp': tiempo, 'limit': threshold}  #{"language": "Python", "number": 2}
	
	myemail2 = myemail + '\n\n\n\n\tIssue was detected on host ' + host + ' at ' + tiempo + ' current JVM use is ' + uso + ' MBs' + ',current free heap percentage is ' + freepcnt2
	
	print myemail2
	 
	 
	try:
	   myEmailObject = smtplib.SMTP('*******')
	   myEmailObject.sendmail(sender, receiver, myemail2)        
	   print "Successfully sent email"
	except SMTPException:
	 print 'Error during email attempt \n'


def monitorJVMHeapSize():
        connect(uname, pwd, url)
        now = datetime.datetime.now()
        tiempo = str(now)[:16]
        serverNames = getRunningServerNames()
        domainRuntime()
        for name in serverNames:
            print 'Now checking '+name.getName()+' for '+domainName
		      
            try:
					cd("/ServerRuntimes/"+name.getName()+"/JVMRuntime/"+name.getName())
					heapSize = cmo.getHeapSizeCurrent()
					freepcnt = cmo.getHeapFreePercent()
					humnum = int( heapSize /(1024*1024))
					humnum2 = str(humnum)
					freepcnt2 = str(freepcnt)
					if heapSize > THRESHOLD and freepcnt < 10:
              # do whatever is neccessary, send alerts, send email etc
						print 'WARNING: The HEAPSIZE is Greater than the Threshold'
						print heapSize , 'is the current JVM size '
						print THRESHOLD , 'is the threshold '
						print freepcnt2
						#call email mail(name) 
						email(domainName,host,tiempo,humnum2,freepcnt2)
					else:
						print threshold
						print heapSize
						print THRESHOLD , 'is the threshold '	
						print freepcnt , 'is the free heap %' 
            except WLSTException,e:
              # this typically means the server is not active, just ignore
              # pass
                print "Ignoring exception " + e.getMessage()
                print heapSize , 'is the current JVM size '
                print THRESHOLD , 'is the threshold '
def getRunningServerNames():
        # only returns the currently running servers in the domain
        return domainRuntimeService.getServerRuntimes()
 
 
 # for looping logic would come into play here after monitorJVMHeapSize and email functions are defined


while var == 1 :
        now = datetime.datetime.now()
        tiempo = str(now)[:16]
        print "checking in at " + tiempo + " now sleeping for a 15 mins ... " 
        java.lang.Thread.sleep(waitTime)
 
	for i in 1,2,3,4,5,6,7:
		uname = *****
		pwd = *****
		domainName=configProps.get("domain."+str(i)+".name")
		url = configProps.get("domain."+str(i)+".admin.url")
		jvmx = configProps.get("domain."+str(i)+".jvmx")
		java.lang.Thread.sleep(waitTime2)
		print '\n', domainName , 'is my next domain' + 'its jvm cap is ' , jvmx
		jvmax=float(jvmx)
		type(jvmax)
		#jvmx2=int(jvmx)
		#type(jvmx2)
		#jvmx._class_
		#jvmax._class_
		
		if ( jvmax > 1900000000 ):
		  print jvmx , 'is JVM cap' 
		  print '3 GB JVM'
		  THRESHOLD = 3072000000
		  threshold = "2.9GB"
		  print 'threshold size is ' , THRESHOLD
		else:
		  print jvmx , 'is JVM cap'
		  print '2 GB JVM'
		  THRESHOLD = 1900000000
		  threshold = "1.9GB"
		  print 'threshold size is ' , THRESHOLD
		  
		
		monitorJVMHeapSize()
       
 
 
#if __name__== "main":
#    monitorJVMHeapSize()