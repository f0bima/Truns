#!/usr/bin/env python
import rospy
import message_filters
from std_msgs.msg import Float64, Int64


def hasil(tinggi, alas):

    luas_pub = rospy.Publisher('luas_pub', Float64, queue_size=10)

    luas = (alas.data * tinggi.data) / 2

    rate = rospy.Rate(1000)

    # rospy.loginfo(luas)

    luas_pub.publish(luas)

    rate.sleep()


def luas_segitiga():
    rospy.init_node('sub_pub')

    tinggi = message_filters.Subscriber('tinggi_pub', Int64)
    alas = message_filters.Subscriber('alas_pub', Int64)

    ts = message_filters.ApproximateTimeSynchronizer(
        [tinggi, alas], 1, 0.1, allow_headerless=True)
    ts.registerCallback(hasil)
    rospy.spin()


if __name__ == '__main__':
    luas_segitiga()
