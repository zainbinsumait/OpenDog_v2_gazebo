#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

rospy.init_node('publisher_theo')
#Front_right
pub1H=rospy.Publisher('/full_gaz1_controller/FRH_position_controller/command',Float64,queue_size=1)
pub1U=rospy.Publisher('/full_gaz1_controller/FRU_position_controller/command',Float64,queue_size=1)
pub1L=rospy.Publisher('/full_gaz1_controller/FRL_position_controller/command',Float64,queue_size=1)

#back_left
pub2H=rospy.Publisher('/full_gaz1_controller/BLH_position_controller/command',Float64,queue_size=1)
pub2U=rospy.Publisher('/full_gaz1_controller/BLU_position_controller/command',Float64,queue_size=1)
pub2L=rospy.Publisher('/full_gaz1_controller/BLL_position_controller/command',Float64,queue_size=1)

#front_left
pub3H=rospy.Publisher('/full_gaz1_controller/FLH_position_controller/command',Float64,queue_size=1)
pub3U=rospy.Publisher('/full_gaz1_controller/FLU_position_controller/command',Float64,queue_size=1)
pub3L=rospy.Publisher('/full_gaz1_controller/FLL_position_controller/command',Float64,queue_size=1)

#back_right
pub4H=rospy.Publisher('/full_gaz1_controller/BRH_position_controller/command',Float64,queue_size=1)
pub4U=rospy.Publisher('/full_gaz1_controller/BRU_position_controller/command',Float64,queue_size=1)
pub4L=rospy.Publisher('/full_gaz1_controller/BRL_position_controller/command',Float64,queue_size=1)

pub = [pub1H,pub1U,pub1L,pub2H,pub2U,pub2L,pub3H,pub3U,pub3L,pub4H,pub4U,pub4L]

rate=rospy.Rate(0.5)
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
joints = [H1,U1,L1,H2,U2,L2,H3,U3,L3,H4,U4,L4]

while not rospy.is_shutdown():
    for x in range(12):
        print(joints[x])
        joints[x].data = 1.7
        print(joints[x], x)
        pub[x].publish(joints[x])
        rate.sleep()
        joints[x].data = 0
        print(joints[x])
        pub[x].publish(joints[x])
        rate.sleep()
