#! /usr/bin/env python3
import rospy

import actionlib
import actionlib.msg
import assignment_2_2022.msg

"""
..module:: nodeAclient
	:platform: Unix
	:synopsis: Python module for the client

..moduleauthor:: Michele Moriconi

This node is the client of the action server. It allows the user to set a goal and to cancel it. The user can also set a new goal if the previous one has already been reached.

Action Client:
	/reaching_goal
"""

#function to set the goal
def set_goal():
	"""
	_summary_: This function allows the user to set a goal and it makes sure that the user inputs a number for the x and y coordinates.


	Returns:
		A goal with the x and y coordinates set by the user.
	"""
	#define the goal variable
	goal = assignment_2_2022.msg.PlanningGoal()
	
	print("Select a x and y coordinate:")
	#keep asking for the x coordinate if the user inputs an invalid char
	while(1):
		try:
			x = float(input("x: "))
       			# code to be executed when num is successfully casted to int
			break
		except ValueError:
			print("Invalid input, please enter a number.")
        		
        #keep asking for the y coordinate if the user inputs an invalid char	
	while(1):
		try:
			y = float(input("y: "))
       			# code to be executed when num is successfully casted to int
			break
		except ValueError:
			print("Invalid input, please enter a number.")
        
        #modify the goal variable using x and y
	goal.target_pose.pose.position.x = x
	goal.target_pose.pose.position.y = y
        
	return goal

def main():
	"""
	_summary_: Main function of the node. It initializes the node, creates the action client, waits for the server and sends the goal. It also allows the user to cancel the goal if the previous one has not yet been reached or to set a new one if the previos one has been reached.
	"""
	#initialize the node
	rospy.init_node("nodeAclient.py")
	#crate action client
	client = actionlib.SimpleActionClient('/reaching_goal', assignment_2_2022.msg.PlanningAction)
	#wait for server
	client.wait_for_server()
	#send the goal returned by set_goal()
	client.send_goal(set_goal())
	
	while(1):
		#let the user choose to cancel the goal or to set a new one
		key_pressed = input("Press c to cancel the goal or n for setting a new goal ")
		#this if statement make sure that the goal is not yet been reached when the user tries to cancel it
		if key_pressed == "c" and client.get_state() != actionlib.GoalStatus.SUCCEEDED:
			client.cancel_goal()
			client.send_goal(set_goal())
		elif key_pressed == "c":
			print("The goal has not been canceled because it has already been reached!")
			client.send_goal(set_goal())
		#this statement makes  sure that the previous goal has already been reached when the user tries to set a new one
		elif key_pressed == "n" and client.get_state() == actionlib.GoalStatus.SUCCEEDED:
			client.send_goal(set_goal())
		elif key_pressed == "n":
			print("A new goal can't be selected because the old one has not been reached yet!") 
		else:
			print("Invalid input!") 
	
if __name__ == '__main__':
    main()
	
