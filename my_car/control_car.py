import rospy
from geometry_msgs.msg import Twist

rospy.init_node('my_car_controller')

def move_forward():
    twist = Twist()
    twist.linear.x = 0.7  # move forward at 0.5 m/s
    twist.angular.z = 0.5
    pub.publish(twist)

def move_backward():
    twist = Twist()
    twist.linear.x = -0.5  # move backward at 0.5 m/s
    twist.angular.z = 0.0
    pub.publish(twist)

def turn_left():
    twist = Twist()
    twist.linear.x = 0.0
    twist.angular.z = 1.0  # turn left at 1 rad/s
    pub.publish(twist)

def turn_right():
    twist = Twist()
    twist.linear.x = 0.0
    twist.angular.z = -1.0  # turn right at 1 rad/s
    pub.publish(twist)

if __name__ == '__main__':
    pub = rospy.Publisher('/my_car/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
         move_forward()
         rate.sleep()
         move_backward()
         rate.sleep()
         turn_left()
         rate.sleep()
         turn_right()
         rate.sleep()

