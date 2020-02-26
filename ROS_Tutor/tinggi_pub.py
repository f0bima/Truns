#!/usr/bin/env python
import rospy

from std_msgs.msg import Int64


def nilai_tinggi():
    rospy.init_node('tinggi')
    tinggi_pub = rospy.Publisher('tinggi_pub', Int64, queue_size=10)
    rate = rospy.Rate(1000)

    while not rospy.is_shutdown():
        tinggi = 20

        tinggi_pub.publish(tinggi)
        rate.sleep()


if __name__ == '__main__':
    try:
        nilai_tinggi()
    except rospy.ROSInterruptException:
        pass
