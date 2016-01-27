#!/usr/bin/python2.7

from time import *
import mraa
import serial
x=0               
def turnup():
	global x
       	if not x:
		x=mraa.Gpio(2)
		x.dir(mraa.DIR_OUT)
	x.write(1)
def turnoff():
	global x
	x.write(0)

def coserial():

	DEVICE = "/dev/ttyS0"
	ser = serial.Serial(DEVICE,9600)
	liste = ['KDE897D4S5Z6','0200D9588A09']
	while(1):
		ser.open()
		odp = ser.read(16)
		if odp:
			print 'RFID Card detected'
			print odp.replace('\n','@')

			"""odp=str(odp)"""
			"""num=odp.split([12])"""
			"""num = num[0]"""
			if '0200D9588A09' in odp:
				print 'Access allowed\n'
				turnup()
				sleep(2)
				turnoff()
			else:
				print 'Access denied\n'
				
			
			
			del odp
			
		ser.close()
		
def main():
	
	coserial()




if __name__ == '__main__':
	
	

	main()




