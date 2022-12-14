# Install script for directory: /home/vishal/ws_3/src/igvc_2022/igvc_self_drive_sim/igvc_self_drive_gazebo

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/vishal/ws_3/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
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

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/vishal/ws_3/build/igvc_2022/igvc_self_drive_sim/igvc_self_drive_gazebo/catkin_generated/installspace/igvc_self_drive_gazebo.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/igvc_self_drive_gazebo/cmake" TYPE FILE FILES
    "/home/vishal/ws_3/build/igvc_2022/igvc_self_drive_sim/igvc_self_drive_gazebo/catkin_generated/installspace/igvc_self_drive_gazeboConfig.cmake"
    "/home/vishal/ws_3/build/igvc_2022/igvc_self_drive_sim/igvc_self_drive_gazebo/catkin_generated/installspace/igvc_self_drive_gazeboConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/igvc_self_drive_gazebo" TYPE FILE FILES "/home/vishal/ws_3/src/igvc_2022/igvc_self_drive_sim/igvc_self_drive_gazebo/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/igvc_self_drive_gazebo" TYPE DIRECTORY FILES
    "/home/vishal/ws_3/src/igvc_2022/igvc_self_drive_sim/igvc_self_drive_gazebo/launch"
    "/home/vishal/ws_3/src/igvc_2022/igvc_self_drive_sim/igvc_self_drive_gazebo/models"
    "/home/vishal/ws_3/src/igvc_2022/igvc_self_drive_sim/igvc_self_drive_gazebo/worlds"
    REGEX "/[^/]*\\.tar\\.gz$" EXCLUDE)
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/vishal/ws_3/build/igvc_2022/igvc_self_drive_sim/igvc_self_drive_gazebo/tests/cmake_install.cmake")

endif()

