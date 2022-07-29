**
This project is an extension of the original one in the  repository OpenDog_v2_modification. a simulation of the same model of the robot in gazebo using ROS noetic and ROS2 foxy.


useful links :


[https://navigation.ros.org/setup_guides/urdf/setup_urdf.html](https://navigation.ros.org/setup_guides/urdf/setup_urdf.html)

https://github.com/ros-simulation/gazebo_ros_pkgs/wiki/ROS-2-Migration:-Spawn-and-delete

**https://medium.com/creating-a-gazebo-simulation-with-ros2-for-your/introduction-8daf6efa12f4**

Steps to run this gazebo file :

1.      First install ROS noetic or ROS2 foxy in your machine

ROS noetic:

[http://wiki.ros.org/noetic/Installation/Ubuntu](http://wiki.ros.org/noetic/Installation/Ubuntu)

ROS2 foxy

[https://docs.ros.org/en/foxy/Installation.html](https://docs.ros.org/en/foxy/Installation.html)

2.      After the creation of the workspace and installing all the tools, install gazebo :

[https://classic.gazebosim.org/tutorials?tut=ros_installing&cat=connect_ros](https://classic.gazebosim.org/tutorials?tut=ros_installing&cat=connect_ros)

[https://docs.ros.org/en/foxy/Tutorials/Intermediate/URDF/Building-a-Visual-Robot-Model-with-URDF-from-Scratch.html](https://docs.ros.org/en/foxy/Tutorials/Intermediate/URDF/Building-a-Visual-Robot-Model-with-URDF-from-Scratch.html)

3.      Git clone the project in the /src folder of the main workspace ( keep the file corresponding to your ROS version).

4.      Compile by typing (in the main workspace folder ) :
			ROS noetic :
```bash
cd ~/catkin_ws

catkin build 

source devel/setup.bash

```

ROS2 Foxy :
	  
```bash
colcon build 
source install/setup.bash
source install/local_setup.bash

``` 

5. type to launch the gazebo file :

Noetic :
```bash
roslaunch full_body gazebo.launch

``` 
to load the controllers, type this command in a new terminal:

```bash
roslaunch full_body controller.launch

``` 
and in a new terminal you can run the python file which has the program of the movement. the file balance_corr.py is doing a balance movement. to run it type :

```bash
rosrun full_publisher balance_corr.py

``` 


Foxy :

```bash
ros2 launch full_gaz1_description gazebo.launch

``` 

the controller is not working well with me because of some issues in the ros_control and gazebo_ros_control packages. although, there's the controller configuration in the files and you can try again with it here are some useful links :
**

https://control.ros.org/master/doc/getting_started/getting_started.html

[https://github.com/ros-controls/gazebo_ros2_control](https://github.com/ros-controls/gazebo_ros2_control)

  

https://www.youtube.com/watch?v=lo1bXm8Aoqc

**


important package to install :

ros-foxy-xacro
ros-foxy-joint-state-publisher-gui


Gazebo files Changement :

while using the fusion 360 plugin to generate gazebo file of the model we have small issues in these files while combiling them using ros noetic. to solve these problems follow these steps :
  

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

  
  
