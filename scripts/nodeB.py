#! /usr/bin/env python3
import rospy

import actionlib
import actionlib.msg
import assignment_2_2022.msg
from my_assignment.srv import GoalCounter, GoalCounterResponse 

goals_reached = 0
goals_cancelled = 0

def checkGoalResult(data):
	global goals_reached, goals_cancelled
	
	#each time a goal is reached increase goal reached by one
	if data.status.status == 3:
		goals_reached += 1
	#each time  a goal is cancelled increase goal cancelled by one
	elif data.status.status == 2:
		goals_cancelled += 1
	
def goals(request):
	global goals_reached, goals_cancelled	
	
	goalCounter = GoalCounterResponse()
	
	#set the goals reached and cancelled parameters
	goalCounter.goals_reached = goals_reached
	goalCounter.goals_cancelled = goals_cancelled
	
	return goalCounter

def main():
	global goals_reached, goals_cancelled
	
	rospy.init_node("nodeB.py")
	#create the service
	srv = rospy.Service("goalsCounterService", GoalCounter, goals)
	#subscriber to PlanningActionResult
	rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, checkGoalResult)

	rospy.spin()
	
if __name__ == '__main__':
	main()	
