#! /usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from my_assignment.msg import PosVelData

#publisher that writes the data on the topic /posVelData
publisher = rospy.Publisher("/posVelData", PosVelData, queue_size = 10)

#the callback function uses sub_data, that are the data retrived by the subscriber from the /odom topic, and saves the 
#position and velocity in posVelData and than publishes it.
def callback(sub_data):
	
	posVelData = PosVelData()
	
	posVelData.x = sub_data.pose.pose.position.x
	posVelData.y = sub_data.pose.pose.position.y
	posVelData.vel_x = sub_data.twist.twist.linear.x
	posVelData.vel_y = sub_data.twist.twist.linear.y
	
	publisher.publish(posVelData)


def main():
	#initialize the node
	rospy.init_node('nodeApublisher.py')
	
	#subscribe to the topic /odom
	rospy.Subscriber("/odom", Odometry, callback)
	rospy.spin()
	
if __name__ == '__main__':
    main()
