cd catkin_ws/
source devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml
roslaunch turtlebot3_gazebo turtlebot3_world.launch

ROS Config Installation
sudo apt install ros-noetic-desktop-full

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt install curl # if you haven't already installed curl

curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt install ros-noetic-desktop-full

sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy   ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc   ros-noetic-rgbd-launch ros-noetic-rosserial-arduino   ros-noetic-rosserial-python ros-noetic-rosserial-client   ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server   ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro   ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz   ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers

sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

TurtleBot3 Config Installation
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
sudo apt-get install python3-catkin-tools
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src/
cd ~/catkin_ws && catkin_make
alias cm='cd ~/catkin_ws && catkin_make'

