#! /usr/bin/env python3
import rospy

import actionlib
import actionlib.msg
import assignment_2_2022.msg
from my_assignment.srv import GoalCounter, GoalCounterResponse 

"""
..module:: nodeB
	:platform: Unix
	:synopsis: Python module for the server

..moduleauthor:: Michele Moriconi

This node is the server of the service. It counts the number of goals reached and cancelled.

Service Server:
	/goals

Subscriber:	
	/goal_status
"""

goals_reached = 0
goals_cancelled = 0

def checkGoalResult(data):
	"""_summary_: This function is the callback function of the subscriber. It checks the status of the goal and increases the goals reached or cancelled.

	Args:
		data : data retrived by the subscriber from the /goal_status topic
	"""
	global goals_reached, goals_cancelled
	
	#each time a goal is reached increase goal reached by one
	if data.status.status == 3:
		goals_reached += 1
	#each time  a goal is cancelled increase goal cancelled by one
	elif data.status.status == 2:
		goals_cancelled += 1
	
def goals(request):
	"""_summary_: This function is the callback function of the service. It returns the number of goals reached and cancelled.

	Args:
		request : request sent by the client
	"""
	global goals_reached, goals_cancelled	
	
	goalCounter = GoalCounterResponse()
	
	#set the goals reached and cancelled parameters
	goalCounter.goals_reached = goals_reached
	goalCounter.goals_cancelled = goals_cancelled
	
	return goalCounter

def main():
	"""_summary_: Main function of the node. It initializes the node, the service and the subscriber.
	"""
	global goals_reached, goals_cancelled
	
	rospy.init_node("nodeB.py")
	#create the service
	srv = rospy.Service("goalsCounterService", GoalCounter, goals)
	"""Service for the goals reached and cancelled"""
	#subscriber to PlanningActionResult
	rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, checkGoalResult)
	"""Subscriber for the status of the goal"""

	rospy.spin()
	
if __name__ == '__main__':
	main()	
