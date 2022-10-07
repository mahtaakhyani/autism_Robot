# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "homer_robot_face: 2 messages, 0 services")

set(MSG_I_FLAGS "-Ihomer_robot_face:C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg;-Isensor_msgs:C:/opt/ros/noetic/x64/share/sensor_msgs/cmake/../msg;-Igeometry_msgs:C:/opt/ros/noetic/x64/share/geometry_msgs/cmake/../msg;-Istd_msgs:C:/opt/ros/noetic/x64/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(homer_robot_face_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImage.msg" NAME_WE)
add_custom_target(_homer_robot_face_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "homer_robot_face" "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImage.msg" "sensor_msgs/Image:std_msgs/Header"
)

get_filename_component(_filename "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImageFile.msg" NAME_WE)
add_custom_target(_homer_robot_face_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "homer_robot_face" "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImageFile.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(homer_robot_face
  "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImage.msg"
  "${MSG_I_FLAGS}"
  "C:/opt/ros/noetic/x64/share/sensor_msgs/cmake/../msg/Image.msg;C:/opt/ros/noetic/x64/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/homer_robot_face
)
_generate_msg_cpp(homer_robot_face
  "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImageFile.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/homer_robot_face
)

### Generating Services

### Generating Module File
_generate_module_cpp(homer_robot_face
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/homer_robot_face
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(homer_robot_face_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(homer_robot_face_generate_messages homer_robot_face_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImage.msg" NAME_WE)
add_dependencies(homer_robot_face_generate_messages_cpp _homer_robot_face_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImageFile.msg" NAME_WE)
add_dependencies(homer_robot_face_generate_messages_cpp _homer_robot_face_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(homer_robot_face_gencpp)
add_dependencies(homer_robot_face_gencpp homer_robot_face_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS homer_robot_face_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(homer_robot_face
  "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImage.msg"
  "${MSG_I_FLAGS}"
  "C:/opt/ros/noetic/x64/share/sensor_msgs/cmake/../msg/Image.msg;C:/opt/ros/noetic/x64/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/homer_robot_face
)
_generate_msg_eus(homer_robot_face
  "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImageFile.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/homer_robot_face
)

### Generating Services

### Generating Module File
_generate_module_eus(homer_robot_face
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/homer_robot_face
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(homer_robot_face_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(homer_robot_face_generate_messages homer_robot_face_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImage.msg" NAME_WE)
add_dependencies(homer_robot_face_generate_messages_eus _homer_robot_face_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImageFile.msg" NAME_WE)
add_dependencies(homer_robot_face_generate_messages_eus _homer_robot_face_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(homer_robot_face_geneus)
add_dependencies(homer_robot_face_geneus homer_robot_face_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS homer_robot_face_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(homer_robot_face
  "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImage.msg"
  "${MSG_I_FLAGS}"
  "C:/opt/ros/noetic/x64/share/sensor_msgs/cmake/../msg/Image.msg;C:/opt/ros/noetic/x64/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/homer_robot_face
)
_generate_msg_lisp(homer_robot_face
  "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImageFile.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/homer_robot_face
)

### Generating Services

### Generating Module File
_generate_module_lisp(homer_robot_face
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/homer_robot_face
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(homer_robot_face_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(homer_robot_face_generate_messages homer_robot_face_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImage.msg" NAME_WE)
add_dependencies(homer_robot_face_generate_messages_lisp _homer_robot_face_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImageFile.msg" NAME_WE)
add_dependencies(homer_robot_face_generate_messages_lisp _homer_robot_face_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(homer_robot_face_genlisp)
add_dependencies(homer_robot_face_genlisp homer_robot_face_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS homer_robot_face_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(homer_robot_face
  "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImage.msg"
  "${MSG_I_FLAGS}"
  "C:/opt/ros/noetic/x64/share/sensor_msgs/cmake/../msg/Image.msg;C:/opt/ros/noetic/x64/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/homer_robot_face
)
_generate_msg_nodejs(homer_robot_face
  "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImageFile.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/homer_robot_face
)

### Generating Services

### Generating Module File
_generate_module_nodejs(homer_robot_face
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/homer_robot_face
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(homer_robot_face_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(homer_robot_face_generate_messages homer_robot_face_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImage.msg" NAME_WE)
add_dependencies(homer_robot_face_generate_messages_nodejs _homer_robot_face_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImageFile.msg" NAME_WE)
add_dependencies(homer_robot_face_generate_messages_nodejs _homer_robot_face_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(homer_robot_face_gennodejs)
add_dependencies(homer_robot_face_gennodejs homer_robot_face_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS homer_robot_face_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(homer_robot_face
  "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImage.msg"
  "${MSG_I_FLAGS}"
  "C:/opt/ros/noetic/x64/share/sensor_msgs/cmake/../msg/Image.msg;C:/opt/ros/noetic/x64/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/homer_robot_face
)
_generate_msg_py(homer_robot_face
  "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImageFile.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/homer_robot_face
)

### Generating Services

### Generating Module File
_generate_module_py(homer_robot_face
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/homer_robot_face
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(homer_robot_face_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(homer_robot_face_generate_messages homer_robot_face_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImage.msg" NAME_WE)
add_dependencies(homer_robot_face_generate_messages_py _homer_robot_face_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/Users/mahta/OneDrive/Documents/GitHub/autism_Robot/src/homer_robot_face-master/msg/DisplayImageFile.msg" NAME_WE)
add_dependencies(homer_robot_face_generate_messages_py _homer_robot_face_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(homer_robot_face_genpy)
add_dependencies(homer_robot_face_genpy homer_robot_face_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS homer_robot_face_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/homer_robot_face)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/homer_robot_face
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(homer_robot_face_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/homer_robot_face)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/homer_robot_face
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET sensor_msgs_generate_messages_eus)
  add_dependencies(homer_robot_face_generate_messages_eus sensor_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/homer_robot_face)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/homer_robot_face
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET sensor_msgs_generate_messages_lisp)
  add_dependencies(homer_robot_face_generate_messages_lisp sensor_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/homer_robot_face)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/homer_robot_face
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET sensor_msgs_generate_messages_nodejs)
  add_dependencies(homer_robot_face_generate_messages_nodejs sensor_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/homer_robot_face)
  install(CODE "execute_process(COMMAND \"C:/opt/ros/noetic/x64/python.exe\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/homer_robot_face\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/homer_robot_face
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(homer_robot_face_generate_messages_py sensor_msgs_generate_messages_py)
endif()
