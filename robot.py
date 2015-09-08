import mraa
import time

pwma = mraa.Pwm(20)
pwma.period_us(1000)
pwma.enable(True)

pwmb = mraa.Pwm(14)
pwmb.period_us(1000)
pwmb.enable(True)

a1 = mraa.Gpio(33)
a1.dir(mraa.DIR_OUT)
a2 = mraa.Gpio(46)
a2.dir(mraa.DIR_OUT)

b1 = mraa.Gpio(48)
b1.dir(mraa.DIR_OUT)
b2 = mraa.Gpio(36)
b2.dir(mraa.DIR_OUT)


def move(xpa,xpb,xa1,xa2,xb1,xb2,t):
	time.sleep(0.1)
	pwma.write(xpa)
	pwmb.write(xpb)
	a1.write(xa1)
	b1.write(xb1)
	a2.write(xa2)
	b2.write(xb2)
	time.sleep(t)
	a1.write(0)
	b1.write(0)
	a2.write(0)
	b2.write(0)
	pwma.write(0)
	pwma.write(0)
        time.sleep(0.1)



def forward(tide):
	move(1,1,1,0,1,0,tide)

def back(tide):
	move(1,1,0,1,0,1,tide)

def lrotate(tide):
	move(1,1,0,1,1,0,tide)

def rrotate(tide):
	move(1,1,1,0,0,1,tide)

def lturn(tide):
	move(0.5,1,1,0,1,0,tide)

def rturn(tide):
	move(1,0.5,1,0,1,0,tide)
