# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ntut-mit/catkin_ws/src/urg_c

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ntut-mit/catkin_ws/build_isolated/urg_c

# Include any dependencies generated for this target.
include CMakeFiles/angle_convert_test.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/angle_convert_test.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/angle_convert_test.dir/flags.make

CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.o: CMakeFiles/angle_convert_test.dir/flags.make
CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.o: /home/ntut-mit/catkin_ws/src/urg_c/current/samples/angle_convert_test.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ntut-mit/catkin_ws/build_isolated/urg_c/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.o   -c /home/ntut-mit/catkin_ws/src/urg_c/current/samples/angle_convert_test.c

CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ntut-mit/catkin_ws/src/urg_c/current/samples/angle_convert_test.c > CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.i

CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ntut-mit/catkin_ws/src/urg_c/current/samples/angle_convert_test.c -o CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.s

CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.o.requires:

.PHONY : CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.o.requires

CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.o.provides: CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.o.requires
	$(MAKE) -f CMakeFiles/angle_convert_test.dir/build.make CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.o.provides.build
.PHONY : CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.o.provides

CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.o.provides.build: CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.o


# Object files for target angle_convert_test
angle_convert_test_OBJECTS = \
"CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.o"

# External object files for target angle_convert_test
angle_convert_test_EXTERNAL_OBJECTS =

/home/ntut-mit/catkin_ws/devel_isolated/urg_c/lib/urg_c/angle_convert_test: CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.o
/home/ntut-mit/catkin_ws/devel_isolated/urg_c/lib/urg_c/angle_convert_test: CMakeFiles/angle_convert_test.dir/build.make
/home/ntut-mit/catkin_ws/devel_isolated/urg_c/lib/urg_c/angle_convert_test: /home/ntut-mit/catkin_ws/devel_isolated/urg_c/lib/libopen_urg_sensor.so
/home/ntut-mit/catkin_ws/devel_isolated/urg_c/lib/urg_c/angle_convert_test: /home/ntut-mit/catkin_ws/devel_isolated/urg_c/lib/libliburg_c.so
/home/ntut-mit/catkin_ws/devel_isolated/urg_c/lib/urg_c/angle_convert_test: CMakeFiles/angle_convert_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ntut-mit/catkin_ws/build_isolated/urg_c/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable /home/ntut-mit/catkin_ws/devel_isolated/urg_c/lib/urg_c/angle_convert_test"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/angle_convert_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/angle_convert_test.dir/build: /home/ntut-mit/catkin_ws/devel_isolated/urg_c/lib/urg_c/angle_convert_test

.PHONY : CMakeFiles/angle_convert_test.dir/build

CMakeFiles/angle_convert_test.dir/requires: CMakeFiles/angle_convert_test.dir/current/samples/angle_convert_test.c.o.requires

.PHONY : CMakeFiles/angle_convert_test.dir/requires

CMakeFiles/angle_convert_test.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/angle_convert_test.dir/cmake_clean.cmake
.PHONY : CMakeFiles/angle_convert_test.dir/clean

CMakeFiles/angle_convert_test.dir/depend:
	cd /home/ntut-mit/catkin_ws/build_isolated/urg_c && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ntut-mit/catkin_ws/src/urg_c /home/ntut-mit/catkin_ws/src/urg_c /home/ntut-mit/catkin_ws/build_isolated/urg_c /home/ntut-mit/catkin_ws/build_isolated/urg_c /home/ntut-mit/catkin_ws/build_isolated/urg_c/CMakeFiles/angle_convert_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/angle_convert_test.dir/depend

