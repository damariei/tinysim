#!/usr/bin/python

__author__ = 'damariei'

import os
import curses
import curses.textpad
from world import World
from utils import *


#Constants
height = 40
width = 120
WORLD_FILE='world1.tinyworld'


def worldExists():
	return os.path.exists(WORLD_FILE)


# Main Program Entry Point
def main(stdscr):
	
	# Header Window
	headerWin = curses.newwin(4, width, 0, 0)
	headerWin.border()
	headerWin.refresh()

	# Info Window
	infoWin = curses.newwin(height-3, width/4, 3, 0)
	infoWin.border()
	infoWin.refresh()
	
	# Playing Field Window
	fieldWin = curses.newwin(height-3, width/4*3+1, 3, width/4-1)
	fieldWin.border()
	fieldWin.refresh()
	
	# Command Window
	comWin = curses.newwin(3, width, height-3, 0)
	comWin.border()
	comWin.addstr(1, 1, ">")
	comWin.nodelay(1)
	comWin.move(1,3)
	comWin.refresh()

	inbuf = InputBuffer()
	
	# Game Loop
	while True:

		# Process Input
		charin = comWin.getch()
		if charin>=ord('a') and charin<=ord('z'):
			comWin.addstr(1,inbuf.count()+3,chr(charin))
			inbuf.add(charin)
		elif charin==10 or inbuf.count()>(width-5):
			for i in range(3,inbuf.count()+3):
				comWin.addstr(1,i,' ')
			headerWin.addstr(1,1,inbuf.getandclear())
			headerWin.refresh()
			comWin.move(1,3)
			comWin.refresh()
		


os.system('printf \"\\e[8;'+str(height)+';'+str(width)+';t\"')
os.system('clear')
raw_input('TinySim v0.1, Press Enter to Begin...')

# World Loading
world = ''

# Remove existing world if user decides to
if worldExists():
	continue_answer = raw_input('\nContinue previous world ([Y]/n)?')

	if continue_answer.lower()=='n':
		os.remove(WORLD_FILE)

# Load/Create world now
if worldExists():
	world = World(WORLD_FILE)
else:
	world = World('')


# Start Game Thread
curses.wrapper(main)