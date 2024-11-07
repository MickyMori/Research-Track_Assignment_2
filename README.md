Research Track I Second Assignment
=================================

Student: [Michele Moriconi](https://github.com/MickyMori) (S4861803), Professor: [Carmine Tommaso Recchiuto](https://github.com/CarmineD8)
------------------------------------------------------------------------------------------------------------------------------------------

This is the second assignment for the course Research Track 1 held at Genoa's University. The assignment required to create three nodes to make a robot move in the environment and to retrieve some data.

Installing and running
----------------------

The simulator requires a ROS installation, the ROS package [assignment_2_2022](https://github.com/CarmineD8/assignment_2_2022) and the konsole installation.

To get the assignment_2_2022 package click on the link above or use the following command

```bash
$ git clone https://github.com/CarmineD8/assignment_2_2022
```

To install konsole use the command:

```bash
$ sudo apt-get install konsole
```

Before running the program make sure that the python files have the permission to be executed. To do so use the following commands inside the scrips folder:

```bash
$ chmod +x nodeAclient.py
```

```bash
$ chmod +x nodeApublisher.py
```

```bash
$ chmod +x nodeB.py
```

```bash
$ chmod +x nodeC.py
```

To run the program use the command:

```bash
$ roslaunch my_assignment my_assignment.launch
```

Nodes
---------

### nodeAclient.py ###

I divided the first node in two parts. The nodeAclient allows the user to insert the goal position, to cancel the current goal and to set a new goal if the previous one has already been reached. I decided to open this node on a new terminal using Konsole to make it more user friendly.

### nodeApublisher.py ###

The nodeApublisher subscribes to the topic "/odom" to retrieve the robot's position and velocity in cartesian components. The node than uses the custom message PosVelData, that can be found in the msg folder, to publish the data on the topic "/posVelData".

To visualize what the node is publishing use the command:

```bash
$ rostopic echo /posVelData
```

### nodeB.py ###

The nodeB is a service node that keeps track of the number of goals reached and cancelled. This node subscribes to the topic "/reaching_goal/result" to get the data.

The service used by the node is GoalCounter.srv and it can be found inside the srv folder.

To visualize the data use the command:

```bash
$ rosservice call goalCounterService
```

### nodeC.py ###

The nodeC computes the distance of the robot from the goal and the speed of the robot. The node subscribe to the topic "/posVelData" to retrieve the position and velocity of the robot and after computing the distance and speed publishes them in the topic "/robotDistVel" using  the custom message DistAvgVel, that can be found in the msg folder. The node is set to publish the data once per second.

To visualize the data use the command:

```bash
$ rostopic echo /robotDistVel
```

Flowchart
---------

The rectangular blocks rappresent the actions while the rhombuses rappresent the decisions. 

The following flowchart summarizes the key points of the nodeAclient.

![Flowchart Node A Client](/Images/flowchart.png "Flowchart Node A Client")

The following flowchart summarizes the key points of the nodeApublisher.

![Flowchart Node A Publisher](/Images/flowchartPub.png "Flowchart Node A Publisher")

Possible improvements
---------------------

In this section will be desceibed some possible future improvements of the code. 

When nodeC publishes the message while the goal has not been defined the distance increases a little over time, so I could add a treshold to avoid really small changes.

When the robots encounters a wall it turn in a fixed direction and not towards the shortest path. It could be implemented in the algorithm the code to make so that the robot can compute the best direction to turn.
 
