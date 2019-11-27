# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "marvelmind: 1 messages, 0 services")

set(MSG_I_FLAGS "-Imarvelmind:/home/ntut-mit/catkin_ws/src/autolabor/src/driver/location/marvelmind/msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(marvelmind_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ntut-mit/catkin_ws/src/autolabor/src/driver/location/marvelmind/msg/beacon_pos.msg" NAME_WE)
add_custom_target(_marvelmind_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "marvelmind" "/home/ntut-mit/catkin_ws/src/autolabor/src/driver/location/marvelmind/msg/beacon_pos.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(marvelmind
  "/home/ntut-mit/catkin_ws/src/autolabor/src/driver/location/marvelmind/msg/beacon_pos.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/marvelmind
)

### Generating Services

### Generating Module File
_generate_module_cpp(marvelmind
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/marvelmind
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(marvelmind_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(marvelmind_generate_messages marvelmind_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ntut-mit/catkin_ws/src/autolabor/src/driver/location/marvelmind/msg/beacon_pos.msg" NAME_WE)
add_dependencies(marvelmind_generate_messages_cpp _marvelmind_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(marvelmind_gencpp)
add_dependencies(marvelmind_gencpp marvelmind_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS marvelmind_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(marvelmind
  "/home/ntut-mit/catkin_ws/src/autolabor/src/driver/location/marvelmind/msg/beacon_pos.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/marvelmind
)

### Generating Services

### Generating Module File
_generate_module_eus(marvelmind
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/marvelmind
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(marvelmind_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(marvelmind_generate_messages marvelmind_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ntut-mit/catkin_ws/src/autolabor/src/driver/location/marvelmind/msg/beacon_pos.msg" NAME_WE)
add_dependencies(marvelmind_generate_messages_eus _marvelmind_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(marvelmind_geneus)
add_dependencies(marvelmind_geneus marvelmind_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS marvelmind_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(marvelmind
  "/home/ntut-mit/catkin_ws/src/autolabor/src/driver/location/marvelmind/msg/beacon_pos.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/marvelmind
)

### Generating Services

### Generating Module File
_generate_module_lisp(marvelmind
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/marvelmind
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(marvelmind_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(marvelmind_generate_messages marvelmind_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ntut-mit/catkin_ws/src/autolabor/src/driver/location/marvelmind/msg/beacon_pos.msg" NAME_WE)
add_dependencies(marvelmind_generate_messages_lisp _marvelmind_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(marvelmind_genlisp)
add_dependencies(marvelmind_genlisp marvelmind_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS marvelmind_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(marvelmind
  "/home/ntut-mit/catkin_ws/src/autolabor/src/driver/location/marvelmind/msg/beacon_pos.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/marvelmind
)

### Generating Services

### Generating Module File
_generate_module_nodejs(marvelmind
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/marvelmind
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(marvelmind_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(marvelmind_generate_messages marvelmind_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ntut-mit/catkin_ws/src/autolabor/src/driver/location/marvelmind/msg/beacon_pos.msg" NAME_WE)
add_dependencies(marvelmind_generate_messages_nodejs _marvelmind_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(marvelmind_gennodejs)
add_dependencies(marvelmind_gennodejs marvelmind_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS marvelmind_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(marvelmind
  "/home/ntut-mit/catkin_ws/src/autolabor/src/driver/location/marvelmind/msg/beacon_pos.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/marvelmind
)

### Generating Services

### Generating Module File
_generate_module_py(marvelmind
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/marvelmind
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(marvelmind_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(marvelmind_generate_messages marvelmind_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ntut-mit/catkin_ws/src/autolabor/src/driver/location/marvelmind/msg/beacon_pos.msg" NAME_WE)
add_dependencies(marvelmind_generate_messages_py _marvelmind_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(marvelmind_genpy)
add_dependencies(marvelmind_genpy marvelmind_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS marvelmind_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/marvelmind)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/marvelmind
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/marvelmind)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/marvelmind
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/marvelmind)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/marvelmind
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/marvelmind)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/marvelmind
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/marvelmind)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/marvelmind\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/marvelmind
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
