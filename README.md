**

Gazebo files Changement :

  

1.  in the file .gazebo in the URDF folder change the parameters mu1 and mu2 of the base link to a high number like 1500000000000 to increase the friction of the base with the ground so it doesn't move
    
2.  just before the base link you will find a piece of code for the controller like this one :
    
```bash
<gazebo>

 <plugin name="control" filename="libgazebo_ros_control.so"/>

</gazebo>

``` 
  

replace it with this code :

  
```bash
<gazebo>

 <plugin name="gazebo_ros_control" filename="libgazebo_ros_control.so">

 <robotNamespace>/full_gaz1_controller</robotNamespace>

 <robotSimType>gazebo_ros_control/DefaultRobotHWSim</robotSimType>

 <legacyModeNS>true</legacyModeNS>

 </plugin>

</gazebo>
```
  

you can change the name of the plugin from "gazebo_ros_control" to whatever you want but the robotNamespace should be the same as the first line in the controller.yaml file 

  

3.  the same robotNamespace should be in the controller.launch file in the <node name="controller_spawner" after ns 
    
4.  then you have to launch the gazebo.launch file first which will open gazebo simulator with the robot.
    
5.  press RUN in the gazebo simulator 
    
6.  launch the controller file controller.launch
    
7.  now you can find the controller exist in the controller.yaml file in the rostopic list (run the command rostopic list in a new terminal to check) 
    
8.  If the controller command exist in the list you can now publish a value for the position of any joint by a python program or directly in the terminal using rostopic pub 
    

  

create a package to put a python program and move the robot:

  

1.  Go to cd ~/catkin_ws/src
    
2.  catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
    

exemple:

catkin_create_pkg pkg_name std_msgs roscpp rospy 

with pkge_name = the name of the package and std_msgs roscpp rospy are the dependecies 

  

3.  then the pkg is successfully created now we can compile it with these commands :
    
```bash
cd ~/catkin_ws

catkin build 

source devel/setup.bash

```

4.  now you can create a python file with the program in the created pkg 
    

after creating a new file you have to do the compiling commands in step 3 again.

  
  
  
  

ROS2: Foxy 

source :

[https://navigation.ros.org/setup_guides/urdf/setup_urdf.html](https://navigation.ros.org/setup_guides/urdf/setup_urdf.html)

https://github.com/ros-simulation/gazebo_ros_pkgs/wiki/ROS-2-Migration:-Spawn-and-delete

sudo apt install ros-<ros2-distro>-xacro

**