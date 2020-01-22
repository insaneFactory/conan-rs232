cmake_minimum_required(VERSION 3.8)
project(RS_232)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB_RECURSE headers RS-232/rs232.h)
file(GLOB_RECURSE sources RS-232/rs232.c)
add_library(${PROJECT_NAME} ${headers} ${sources})
target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/RS-232)
