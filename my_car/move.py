import rospy
from geometry_msgs.msg import Twist

def move():
    # Initialize the ROS node
    rospy.init_node('my_car_controller', anonymous=True)

    # Create a publisher to send velocity commands to the car
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    # Set the rate of the loop
    rate = rospy.Rate(10) # 10 Hz

    # Move the car forward for 5 seconds
    for i in range(5000):
        # Create a Twist message to represent the velocity command
        vel_cmd = Twist()
        vel_cmd.linear.x = 0.9 # Move at 0.5 m/s
        vel_cmd.angular.z = 0.0 # No rotation

        # Publish the velocity command
        pub.publish(vel_cmd)

        # Sleep for a short period of time to maintain the loop rate
        rate.sleep()

    # Stop the car
    vel_cmd = Twist()
    vel_cmd.linear.x = 0.0 # Stop moving
    vel_cmd.angular.z = 0.0 # No rotation
    pub.publish(vel_cmd)

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass