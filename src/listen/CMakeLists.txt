cmake_minimum_required(VERSION 3.0.2)
project(listen)

find_package(catkin REQUIRED COMPONENTS
  std_msgs
  rospy
  # driverless_msgs
)

catkin_python_setup()

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES nodes
   CATKIN_DEPENDS rospy std_msgs # driverless_msgs # These have to be the same dependencies as the ones at the beginning of the file
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS
  nodes/listen.py # Here you declare your scripts, one per line.
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
