cmake_minimum_required(VERSION 3.5)

project(glfw-example VERSION 0.1 LANGUAGES C)

set(CMAKE_C_STANDARD 23)
set(CMAKE_C_STANDARD_REQUIRED ON)

find_package(glfw3 3.4 REQUIRED)

add_executable(glfw_example src/main.c)
target_link_libraries(glfw_example PRIVATE glfw)
