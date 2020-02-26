#!/usr/bin/env python

import rospy

from std_msgs.msg import Float64


def luas_segitiga(data):
    L = data.data
    rospy.loginfo("Nilai Luas Segitga (luas_sub.py)= " + str(L))


def luas():
    rospy.init_node('Luas_Segitiga')
    rospy.Subscriber('luas_pub', Float64, luas_segitiga)
    rospy.spin()


if __name__ == '__main__':
    luas()
