# Install script for directory: C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/homer_robot_face/msg" TYPE FILE FILES
    "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImage.msg"
    "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImageFile.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/homer_robot_face/cmake" TYPE FILE FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/build/homer_robot_face-master/catkin_generated/installspace/homer_robot_face-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/devel/include/homer_robot_face")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/devel/share/roseus/ros/homer_robot_face")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/devel/share/common-lisp/ros/homer_robot_face")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/devel/share/gennodejs/ros/homer_robot_face")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "C:/opt/ros/noetic/x64/python.exe" -m compileall "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/devel/lib/site-packages/homer_robot_face")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/site-packages" TYPE DIRECTORY FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/devel/lib/site-packages/homer_robot_face")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/build/homer_robot_face-master/catkin_generated/installspace/homer_robot_face.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/homer_robot_face/cmake" TYPE FILE FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/build/homer_robot_face-master/catkin_generated/installspace/homer_robot_face-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/homer_robot_face/cmake" TYPE FILE FILES
    "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/build/homer_robot_face-master/catkin_generated/installspace/homer_robot_faceConfig.cmake"
    "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/build/homer_robot_face-master/catkin_generated/installspace/homer_robot_faceConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/homer_robot_face" TYPE FILE FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/homer_robot_face" TYPE EXECUTABLE FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/devel/lib/homer_robot_face/RobotFace.exe")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/homer_robot_face/config" TYPE DIRECTORY FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/config/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/homer_robot_face/images" TYPE DIRECTORY FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/images/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/homer_robot_face" TYPE DIRECTORY FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/include/homer_robot_face/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/homer_robot_face/launch" TYPE DIRECTORY FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/launch/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/homer_robot_face/mesh" TYPE DIRECTORY FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/mesh/")
endif()

