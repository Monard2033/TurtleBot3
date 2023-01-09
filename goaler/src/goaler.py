#!/usr/bin/env python3

import rospy
import actionlib
import cv2
import numpy as np
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from decimal import *

image = cv2.imread('/home/monard2033/catkin_ws/src/line_of_sight/world.pgm')
imageo = cv2.imread('/home/monard2033/catkin_ws/src/line_of_sight/result.png')

def movebase_client(crt_map):
    print(crt_map[0],crt_map[1])
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = crt_map[0] #0.001 #-2.622 #2.403
    goal.target_pose.pose.position.y = crt_map[1] #crt_map[0] #0.001 #-2.294 #2.294
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
        crt0=Decimal(x)/Decimal(76.43)
        crt1=Decimal(y)/Decimal(83.7)
        crt2=round(crt0,5)
        crt3=round(crt1,5)
        if(crt0>= Decimal(1.13)):
            crt1=Decimal(y)/Decimal(102.4)
        if check_point(crt):
            print("x=",crt2, "y=",crt3)
            return np.array([-crt2,-crt3])
        #varx = Decimal(225//x)
        #vary = Decimal(195//y)
        #print(Decimal(varx),Decimal(vary))
        #crt0=Decimal(x)//76.43 #(76.43)
        #crt1=Decimal(y)//83.7 #(83.7)
        #if(crt0>= Decimal(1.13)):
        #  crt1=Decimal(y)/Decimal(102.4)
        #if(crt0>=Decimal(225)/Decimal(varx)):
        #    crt0= -abs(crt0)
        #if check_point(crt):
        # return np.array([crt0,crt1])
     #exit(0)


if __name__ == '__main__':
    try:
        rospy.init_node('my_goal')
        result = movebase_client(calculate_goal())
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
