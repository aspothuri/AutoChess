cmake_minimum_required(VERSION 3.27)
project(electrical_code)

set(CMAKE_CXX_STANDARD 14)

include_directories(arduino)

add_executable(electrical_code
        arduino/arduino.ino
        embedding/test.cpp
        embedding/serial.cpp)
