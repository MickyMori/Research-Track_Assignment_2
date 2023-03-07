#! /usr/bin/env python3
import rospy
import math
from my_assignment.msg import DistAvgVel
from my_assignment.msg import PosVelData

"""
..module:: nodeC
	:platform: Unix
	:synopsis: Python module for the publisher

..moduleauthor:: Michele Moriconi

This node is the publisher of the distance and speed of the robot.

Publisher:
	/robotDistVel

Subscriber:
	/posVelData

Parameters:
	/des_pos_x
	/des_pos_y
"""

data = DistAvgVel()

def callback(sub_data):
	"""
	_summary_: Callback function that computes the distance from the goal and the speed of the robot

	Args:
		sub_data : the data received from the topic /posVelData
	"""
	global data
	#get the data relative to the goal position
	goal_x = rospy.get_param("des_pos_x")
	goal_y = rospy.get_param("des_pos_y")
	
	#compute the distance and speed 
	data.distance = math.sqrt(pow((goal_x - sub_data.x), 2) + pow((goal_y - sub_data.y), 2))
	data.speed = math.sqrt(pow(sub_data.vel_x, 2) + pow(sub_data.vel_y, 2))

def main():
	"""
	_summary_: Main function that initializes the node, the publisher and the subscriber
	"""
	global data	
	#initialize the node
	rospy.init_node("nodeC.py")
	#initialize the publisher that publishes distance and speed
	publisher = rospy.Publisher("/robotDistVel", DistAvgVel, queue_size = 10)
	"""Publisher for the distance and speed of the robot
	"""
	#set the rate as once per second
	rate = rospy.Rate(1)
	#subsribe to the posVelData topic to know the position an velocity of the robot
	rospy.Subscriber("/posVelData", PosVelData, callback)
	"""Subscriber for the position and velocity of the robot"""
	
	while True:
		#publish the speed and velocity
		publisher.publish(data)
		#wait a second each time it publishes
		rate.sleep()
	
if __name__ == '__main__':
	main()
