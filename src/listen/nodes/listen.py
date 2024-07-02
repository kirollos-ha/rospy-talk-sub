#!/usr/bin/python3

import rospy

from std_msgs.msg import String

def porco_callback(msg):
    print("MA PORCO" + msg.data)

if __name__=='__main__':
    rospy.init_node('listen')
    chatter_topic = rospy.get_param("/listen/chatter_topic")
    print("listener chatting on " + chatter_topic)

    rospy.Subscriber(chatter_topic, String, porco_callback)
    rospy.spin()

