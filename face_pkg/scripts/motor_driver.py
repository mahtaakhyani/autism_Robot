#!/usr/bin/python
from logging import root
import rospy
import RPi.GPIO as gpio
import time


class RobotMover():
	def __init__(self):
		self.in1 = 16
		self.in2 = 18
		self.in3 = 24
		self.in4 = 26
		self.in5 = 23
		self.in6 = 13
		self.in7 = 33


		gpio.setmode(gpio.BOARD)
		gpio.setup(self.in1, gpio.OUT)
		gpio.setup(self.in2, gpio.OUT)
		gpio.setup(self.in3, gpio.OUT)
		gpio.setup(self.in4, gpio.OUT)
		gpio.setup(self.in5, gpio.OUT)
		gpio.setup(self.in6, gpio.OUT)

		self.fPWM = 100
		self.pwm = gpio.PWM(self.in7, self.fPWM)
		self.duty = 50

		

	def __del__(self):
        	gpio.cleanup()

	def set_move(self, in1_set , in2_set, in3_set, in4_set, in5_set, in6_set):
		gpio.output(self.in1, in1_set)
		gpio.output(self.in2, in2_set)
		gpio.output(self.in3, in3_set)
		gpio.output(self.in4, in4_set)
		gpio.output(self.in5, in5_set)
		gpio.output(self.in6, in6_set)
		
	def forward(self):
				self.set_move(1,0,1,0,0,0)

	def reverse(self):
                self.set_move(0,1,0,1,0,0)

	def right(self):
                self.set_move(0,1,1,0,0,0)

	def left(self):
                self.set_move(1,0,0,1,0,0)

	def stop(self):
				self.set_move(0,0,0,0,0,0)

	def headright(self):
				self.set_move(0,0,0,0,0,1)

	def headleft(self):
				self.set_move(0,0,0,0,1,0)
				
	def headstop(self):
				self.pwm.stop()
				self.set_move(0,0,0,0,0,0)

	

	def set_cmd_vel(self, linear_speed, angular_speed):
		print('Sending published commands to robot')
		if linear_speed > 0:
			self.forward()
			
		elif linear_speed < 0:
			self.reverse()
		else:
			self.stop()

		if angular_speed > 0:
			self.right()

		if angular_speed < 0:
			self.left()

	def set_head_cmd_vel(self, roatation):
		self.pwm.start(self.duty)
		if roatation < 0 :
			self.headleft()

		elif roatation > 0 :
			self.headright()

		else:
			self.headstop()
