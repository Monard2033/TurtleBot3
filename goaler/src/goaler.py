#!/usr/bin/env python3

import rospy
import actionlib
import cv2
import numpy as np
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from decimal import *
#from field_of_view import *

image = cv2.imread('/home/monard2033/catkin_ws/src/goaler/src/world.pgm')
imageo = cv2.imread('/home/monard2033/catkin_ws/src/goaler/src/result.png')
def movebase_client(crt_map):
    print(crt_map[0],crt_map[1])
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = crt_map[0] #0.001 #-2.622 #2.403
    goal.target_pose.pose.position.y = crt_map[1] #0.001 #-2.294 #2.294
    goal.target_pose.pose.orientation.z = 1.0
    goal.target_pose.pose.orientation.w = -4.3

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()
        
def check_point(p1):
    if (imageo[p1[0],p1[1],0] == 254 and imageo[p1[0],p1[1],1] == 254 and imageo[p1[0],p1[1],2] == 254):
            return True
    return False

def calculate_goal():
    height, width, channels = image.shape
    for x in range(0,width):
     for y in range(0,height):
        crt = np.array([x, y])
        crt0=Decimal(x)/Decimal(94.81)
        crt1=Decimal(y)/Decimal(89.3)
        if(crt0>=Decimal(1.00) or crt0<=Decimal(-1.30)):
            crt1=Decimal(y)/Decimal(108.4)
        if(crt1>=Decimal(1.91) or crt1<=Decimal(-2.00)): 
            crt0=Decimal(x)/Decimal(126)
        if check_point(crt):
            crt2=round(crt0,5)
            crt3=round(crt1,5)
            print("x=",crt0, "y=",crt1)
            return np.array([crt2,crt3])


if __name__ == '__main__':
    try:
        rospy.init_node('my_goal')
        result = movebase_client(calculate_goal())
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
