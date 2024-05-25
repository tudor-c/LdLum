import RPi.GPIO as G
import time

DATA = 4
CLOCK = 17
LATCH = 22
CLEAR = 19
G.setmode(G.BCM)

G.setup(DATA,G.OUT)
G.setup(CLOCK,G.OUT)
G.setup(LATCH,G.OUT)
G.setup(CLEAR,G.OUT)


G.output(CLEAR,1)
G.output(CLOCK,0)

def writeBit(bits):
	bits.reverse()
	for bit in bits:

		G.output(DATA,bit)	
		time.sleep(.01)
		G.output(CLOCK,1)
		time.sleep(.01)
		G.output(CLOCK,0)
		time.sleep(.01)
		G.output(DATA,0)

	G.output(LATCH,1)
	G.output(LATCH,0)

writeBit([1,1,1,1,0,1,0,1])

G.cleanup()
