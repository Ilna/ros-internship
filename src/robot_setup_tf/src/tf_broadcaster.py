#!/usr/bin/env python
import roslib
roslib.load_manifest('robot_setup_tf')
import rospy

import tf
from geometry_msgs.msg import PoseStamped, Point, Pose, Quaternion, Twist, Vector3


if __name__ == '__main__':
    rospy.init_node('robot_tf_publisher')
    rate = rospy.Rate(100.0)#edw gia kapoio logo h cpp 8elei apo panw to rate enw sto arxeio ths python einai apo katw
    
    br = tf.TransformBroadcaster()
    
    while not rospy.is_shutdown():#apo edw kai katw den eimai sigourh akoma 
        t = rospy.Time.now()
        
        #br.sendTransform((3.0, 0.0, 0.0), tf.transformations.quaternion_from_euler(0, 0, 0), t, 'laser_point', 'base_link')
        br.sendTransform((0.1, 0.0, 0.2), tf.transformations.quaternion_from_euler(0, 0, 0), t, 'base_laser', 'base_link')
        
        rate.sleep()
    
    
    