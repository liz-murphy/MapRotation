#!/usr/bin/env python

import roslib;
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy
import math
import numpy as np

topic = 'visualization_marker_array'
publisher = rospy.Publisher(topic, MarkerArray)

rospy.init_node('register')

markerArray = MarkerArray()

origin_x = 57.5278873072;
origin_y = -77.0197364237
angle = -0.120108735567
res = 0.05
width = 1062
height = 1130

trans=np.array([0,0,0])
points=np.array([[65.72,-72.82], [109.8,-67.15], [106.52,-41.90], [103.15, -30.87], [62.47, -35.01]])

count = 0
MARKERS_MAX=10
while not rospy.is_shutdown():

    # ... here I get the data I want to plot into a vector called trans
   #p[0] = 80.59;
   #p[1] = -71;

   for p in points:
       print p
       s = math.sin(angle);
       c = math.cos(angle);

       # This is the point that everything is rotated around
       cx = (width*res)/2+origin_x
       cy = (height*res)/2+origin_y

       print "Center is at" + str(cx) + ", " + str(cy)

       # translate point back to origin:
       tx = p[0] - cx;
       ty = p[1] - cy;

       print "Translated point at " + str(p[0]) + ", " + str(p[1])

       # rotate point
       xnew = tx * c - ty * s;
       ynew = tx * s + ty * c;

       # translate point back:
      # xnew = xnew + cx;
      # ynew = ynew + cy;

       marker = Marker()
       marker.header.frame_id = "/map"
       marker.type = marker.SPHERE
       marker.action = marker.ADD
       marker.scale.x = 0.5
       marker.scale.y = 0.5
       marker.scale.z = 0.5
       marker.color.a = 1.0
       marker.color.r = 1.0
       marker.pose.orientation.w = 1.0
       marker.pose.position.x = xnew
       marker.pose.position.y = ynew
       marker.pose.position.z = 0
       marker.id = count
       # We add the new marker to the MarkerArray, removing the oldest marker from it when necessary
       if(count > MARKERS_MAX):
           markerArray.markers.pop(0)
       else:
           count += 1
       markerArray.markers.append(marker)

        # Publish the MarkerArray
   publisher.publish(markerArray)

   rospy.sleep(0.5)
