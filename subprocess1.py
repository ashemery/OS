__author__ = 'binary'
import subprocess as sp

fh = open('file','w')
sp.call(['ls','-la'], stdout=fh)
fh.close()
sp.call(['ls','-la'], shell=True)

x = sp.check_output(['echo','hello class'])
print (x)

sp.check_output('exit 0', shell=True)

errFile = open('errorFile','w')
sp.check_output('ls nosuchfile; exit 0', shell=True, stderr=errFile)
errFile.close()

child = sp.Popen('gedit')
print (child)

print (child.poll())

terminate = input('do u want to terminate the process? (y/n): ')
if terminate == 'y':
    child.terminate() # can use .kill() too
    print (child.poll())
else:
    print ('child is running')





