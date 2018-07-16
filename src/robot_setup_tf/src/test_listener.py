#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
import math
import tf
from geometry_msgs.msg import PointStamped, Point, Pose, Quaternion, Twist, Vector3


if __name__ == '__main__':
    rospy.init_node('turtle_tf_listener')

    listener = tf.TransformListener()
    
    #listener.waitForTransform('base_link', 'base_laser', rospy.Time(0),rospy.Duration(4.0))
    
    #we'll create a point in the base_laser frame that we'd like to transform to the base_link frame
    laser_point = PointStamped()
    laser_point.header.frame_id = 'base_laser'
    
    #we'll just use the most recent transform available for our simple example
    laser_point.header.stamp = rospy.Time(0)
    
    #just an arbitrary point in space
    laser_point.point.x = 3.0
    laser_point.point.y = 0.0
    laser_point.point.z = 0.0
    
    now = rospy.get_rostime()
    
    #we'll transform a point once every second
    rate = rospy.Rate(1.0)
    
    while not rospy.is_shutdown():
        
        base_point = PointStamped()
        base_point.header.frame_id = 'base_link'
        base_point.header.stamp = rospy.Time(0)
    
        try:
            #(trans,rot) = listener.lookupTransform('laser_point', 'base_link', now)
            base_point = listener.transformPoint("base_link",laser_point)
            rospy.loginfo("base_laser: (%.2f, %.2f. %.2f) -----> base_link: (%.2f, %.2f, %.2f)",
                     laser_point.point.x, 
                     laser_point.point.y, 
                     laser_point.point.z,
                     base_point.point.x, 
                     base_point.point.y, 
                     base_point.point.z )
            
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                continue
        

        #angular = 4 * math.atan2(trans[1], trans[0])
        #linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        #cmd = geometry_msgs.msg.Twist()
        #cmd.linear.x = linear
        #cmd.angular.z = angular
        #turtle_vel.publish(cmd)

    rate.sleep()