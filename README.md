
# RT1-Assignment2-ROS2

## Project Description

This repository contains a ROS 2 package for controlling a mobile robot using odometry data. The main component is a node that subscribes to odometry information and publishes velocity commands to guide the robot. The node uses the robot's position to adjust its angular velocity dynamically, ensuring it stays within a predefined area.

The system periodically evaluates the robot's position along the x-axis and applies corrective angular velocity to prevent it from moving out of bounds.

## Features

- **Odometry-Based Velocity Control**

    The node subscribes to the /odom topic and continuously monitors the robot's position.
    Based on the robot's x-axis position, the node adjusts the angular velocity to steer the robot if it approaches predefined boundaries

- **Velocity Command Publisher**

    The node publishes linear and angular velocity commands to the /cmd_vel topic at regular intervals.

## Prerequisites

1. **ROS 2** Foxy installed.
2. **Python 3.x** (for package installation and testing).
3. **Gazebo**
4. Clone the repo https://github.com/CarmineD8/robot_urdf and switch to branch ros2

## Installation

Clone the repository into your ROS 2 workspace:

```bash
git clone https://github.com/MattiaTinfena/RT1-Assignment2-ROS2.git
```

Build the package:

```bash
colcon build
```

## Execution

Launch gazebo:

```bash
ros2 launch robot_urdf gazebo.launch.py
```
Launch the ROS 2 system with the appropriate launch file:

```bash
ros2 run rt1_assignment2_ros2 UI_node
```

## Improvements

Add any potential improvements or tasks you'd like to see implemented.

Feel free to contribute!