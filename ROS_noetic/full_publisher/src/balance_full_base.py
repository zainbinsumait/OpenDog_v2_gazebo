#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import math

rospy.init_node('publisher_theo')
#Front_right
pub1H=rospy.Publisher('/full_gaz_base_controller/FRH_position_controller/command',Float64,queue_size=1)
pub1U=rospy.Publisher('/full_gaz_base_controller/FRU_position_controller/command',Float64,queue_size=1)
pub1L=rospy.Publisher('/full_gaz_base_controller/FRL_position_controller/command',Float64,queue_size=1)
pub1 = [pub1H, pub1U,pub1L]
#back_left
pub2H=rospy.Publisher('/full_gaz_base_controller/BLH_position_controller/command',Float64,queue_size=1)
pub2U=rospy.Publisher('/full_gaz_base_controller/BLU_position_controller/command',Float64,queue_size=1)
pub2L=rospy.Publisher('/full_gaz_base_controller/BLL_position_controller/command',Float64,queue_size=1)

pub2 = [pub2H, pub2U,pub2L]
#front_left
pub3H=rospy.Publisher('/full_gaz_base_controller/FLH_position_controller/command',Float64,queue_size=1)
pub3U=rospy.Publisher('/full_gaz_base_controller/FLU_position_controller/command',Float64,queue_size=1)
pub3L=rospy.Publisher('/full_gaz_base_controller/FLL_position_controller/command',Float64,queue_size=1)

pub3 = [pub3H, pub3U,pub3L]
#back_right
pub4H=rospy.Publisher('/full_gaz_base_controller/BRH_position_controller/command',Float64,queue_size=1)
pub4U=rospy.Publisher('/full_gaz_base_controller/BRU_position_controller/command',Float64,queue_size=1)
pub4L=rospy.Publisher('/full_gaz_base_controller/BRL_position_controller/command',Float64,queue_size=1)

pub4 = [pub4H, pub4U,pub4L]

pub = [pub1U,pub1L,pub2U,pub2L,pub3U,pub3L,pub4U,pub4L]
hip_pub = [pub1H,pub2H,pub3H,pub4H]

rate=rospy.Rate(2)
H1=Float64()
U1=Float64()
L1=Float64()

H2=Float64()
U2=Float64()
L2=Float64()

H3=Float64()        
U3=Float64()
L3=Float64()

H4=Float64()
U4=Float64()
L4=Float64()
joints = [U1,L1,U2,L2,U3,L3,U4,L4]
hip_joints = [H1,H2,H3,H4]
while not rospy.is_shutdown():
    for x in range(2):
        joints[x+x].data = 50*math.pi/180
        joints[x+x+1].data = -100.466*math.pi/180
    for x in range(2):
        joints[4+x+x].data = -50*math.pi/180
        joints[x+x+5].data = 100.466*math.pi/180
    for x in range(4):
        print(joints[x], x)
        pub[x].publish(joints[x])
        pub[x+4].publish(joints[x+4])
        hip_pub[x].publish(0.2)
    rate.sleep()
    for x in range(2):
        joints[x+x].data = 20*math.pi/180
        joints[x+x+1].data = -40*math.pi/180
    for x in range(2):
        joints[4+x+x].data = -20*math.pi/180
        joints[x+x+5].data = 40*math.pi/180
    for i in range(10):
        for x in range(4):
            print(joints[x], x)
            pub[x].publish(joints[x])
            hip_pub[x].publish(0.2)
        rate.sleep()
        for x in range(4):
            print(joints[x], x)
            pub[x].publish(0.0)
            pub[x+4].publish(joints[x+4])
            hip_pub[x].publish(0.2)
        rate.sleep()
        for x in range(4):
            print(joints[x], x)
            pub[x+4].publish(0.0)
            hip_pub[x].publish(0.2)
        rate.sleep()
