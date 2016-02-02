#!/usr/bin/python2.7

from time import *
import mraa
import serial
x=0               
def turnuptheled():
	global x
       	if not x:
		x=mraa.Gpio(2)
		x.dir(mraa.DIR_OUT)
	x.write(1)
def turnofftheled():
	global x
	x.write(0)

def coserial():

	DEVICE = "/dev/ttyS0"
	ser = serial.Serial(DEVICE,9600)
	liste ='0200D9588A09'
	while(1):
		ser.open()
		odp = ser.read(16)
		if odp:
			print 'RFID Card detected'
			odp.replace('\n','0')
			odp=odp[1:13]
			print odp
			if '0200D9588A09' == odp:
				print 'Access allowed'
				turnuptheled()
				sleep(2)
				turnofftheled()
			else:
				print 'Access denied\n'
			print '\n'			
			del odp
		ser.close()
		
def main():	
	coserial()

if __name__ == '__main__':
	main()



yoloooooooo
