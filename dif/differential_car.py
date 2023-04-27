#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('differential_car_controller')

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

while not rospy.is_shutdown():
    cmd = Twist()
    cmd.linear.x = 0.5
    cmd.angular.z =
