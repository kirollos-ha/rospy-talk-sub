#!/usr/bin/python3

import rospy
from std_msgs.msg import String

if __name__=='__main__':
    rospy.init_node('talk')
    chatter_topic = rospy.get_param("/talk/chatter_topic")
    print("talker chatting on " + chatter_topic)

    pub = rospy.Publisher(chatter_topic, String, queue_size=10)

    rate = rospy.Rate(1)

    try:
        while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            pub.publish(hello_str)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
