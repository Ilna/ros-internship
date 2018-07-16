#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
import math
import tf
from geometry_msgs.msg import PointStamped

CONST_LISTENER  = tf.TransformListener()

#edw san parametro 8elei na kanw anafora ston listener(to kanei me & sth c++)
def transformPoint(CONST_LISTENER):
    #we'll create a point in the base_laser frame that we'd like to transform to the base_link frame
    
    #to geometry_msgs.msg.PointStamped laser_point ??
    laser_point = PointStamped()
    laser_point.header.frame_id = 'base_laser'
    
    #we'll just use the most recent transform available for our simple example
    laser_point.header.stamp = rospy.Time(0)
    
    #just an arbitrary point in space
    laser_point.point.x = 1.0
    laser_point.point.y = 0.2
    laser_point.point.z = 0.0
    
try:
    now = rospy.get_rostime() 
        
    base_point = PointStamped()
       
    (trans,rot) = CONST_LISTENER.transformPoint('base_link', laser_point, base_point)
       
    rospy.loginfo("base_laser: (%.2f, %.2f. %.2f) -----> base_link: (%.2f, %.2f, %.2f) at time %.2f",
                    laser_point.point.x, 
                    laser_point.point.y, 
                    laser_point.point.z,
                    base_point.point.x, 
                    base_point.point.y, 
                    base_point.point.z, 
                    base_point.header.stamp.now.secs)
    
except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            
        continue
        
if __name__ == '__main__':
    rospy.init_node('robot_tf_listener')
    r = rospy.Rate(10)
    
    r.sleep()
    
    rospy.spin()
    
       
    
    
    