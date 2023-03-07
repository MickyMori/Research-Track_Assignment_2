#! /usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from my_assignment.msg import PosVelData

"""
..module:: nodeApublisher
	:platform: Unix
	:synopsis: Python module for the publisher

..moduleauthor:: Michele Moriconi

This node is the publisher of the position and velocity of the robot.

Publisher:
	/posVelData

Subscriber:
	/odom
"""

#publisher that writes the data on the topic /posVelData
publisher = rospy.Publisher("/posVelData", PosVelData, queue_size = 10)
"""Publisher for the position and velocity of the robot"""

#the callback function uses sub_data, that are the data retrived by the subscriber from the /odom topic, and saves the 
#position and velocity in posVelData and than publishes it.
def callback(sub_data):
	"""_summary_: This function is the callback function of the subscriber. It saves the position and velocity of the robot in a variable and then publishes it.

	Args:
		sub_data : data retrived by the subscriber from the /odom topic
	"""
	
	posVelData = PosVelData()
	
	posVelData.x = sub_data.pose.pose.position.x
	posVelData.y = sub_data.pose.pose.position.y
	posVelData.vel_x = sub_data.twist.twist.linear.x
	posVelData.vel_y = sub_data.twist.twist.linear.y
	
	publisher.publish(posVelData)


def main():
	"""_summary_: Main function of the node. It initializes the node and the subscriber.
	"""
	#initialize the node
	rospy.init_node('nodeApublisher.py')
	
	#subscribe to the topic /odom
	rospy.Subscriber("/odom", Odometry, callback)
	"""Subscriber for the position and velocity of the robot"""
	rospy.spin()
	
if __name__ == '__main__':
    main()
