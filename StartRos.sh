cd catkin_ws/
source devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml
roslaunch turtlebot3_gazebo turtlebot3_world.launch

