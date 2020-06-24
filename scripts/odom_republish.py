#!/usr/bin/env python
# license removed for brevity
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/khepri/odom', Odometry, queue_size=10)
pub2 = rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist, queue_size=10)

def talk_and_listen():
    rospy.init_node('odom_republisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    rospy.Subscriber("/jackal_velocity_controller/odom", Odometry, callback)
    rospy.Subscriber("/khepri/jackal_velocity_controller/cmd_vel",Twist, callback2)
    rospy.spin()

def callback(data):
    data.header.frame_id="khepri/odom"
    pub.publish(data)

def callback2(data):
    pub2.publish(data)

if __name__ == '__main__':
    try:
        talk_and_listen()
    except rospy.ROSInterruptException:
        pass

