# Install script for directory: C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/video_stream_opencv

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
    set(CMAKE_INSTALL_CONFIG_NAME "RelWithDebInfo")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/video_stream_opencv" TYPE FILE FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/devel/include/video_stream_opencv/VideoStreamConfig.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/site-packages/video_stream_opencv" TYPE FILE FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/devel/lib/site-packages/video_stream_opencv/__init__.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "C:/opt/ros/noetic/x64/python.exe" -m compileall "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/devel/lib/site-packages/video_stream_opencv/cfg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/site-packages/video_stream_opencv" TYPE DIRECTORY FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/devel/lib/site-packages/video_stream_opencv/cfg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/build/video_stream_opencv/catkin_generated/installspace/video_stream_opencv.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/video_stream_opencv/cmake" TYPE FILE FILES
    "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/build/video_stream_opencv/catkin_generated/installspace/video_stream_opencvConfig.cmake"
    "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/build/video_stream_opencv/catkin_generated/installspace/video_stream_opencvConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/video_stream_opencv" TYPE FILE FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/video_stream_opencv/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/video_stream_opencv" TYPE EXECUTABLE FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/devel/lib/video_stream_opencv/video_stream.exe")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY OPTIONAL FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/devel/lib/video_stream_opencv.lib")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/video_stream_opencv" TYPE SHARED_LIBRARY FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/devel/bin/video_stream_opencv.dll")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/video_stream_opencv" TYPE PROGRAM FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/video_stream_opencv/scripts/test_video_resource.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/video_stream_opencv" TYPE DIRECTORY FILES
    "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/video_stream_opencv/launch"
    "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/video_stream_opencv/test"
    USE_SOURCE_PERMISSIONS)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/video_stream_opencv" TYPE FILE FILES "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/video_stream_opencv/nodelet_plugins.xml")
endif()

