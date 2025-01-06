#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

class OdomVelController(Node):

    def __init__(self):
        super().__init__('odomVelController')

        # Subscribe to the 'odom' topic to receive odometry data
        self.odomData = Odometry()
        self.subscription = self.create_subscription(
            Odometry,
            'odom',
            self.odomCallback,
            10
        )

        # Create a publisher for the 'cmd_vel' topic to send velocity commands
        self.velocityPublisher = self.create_publisher(Twist, 'cmd_vel', 10)

        # Set up a periodic timer to call the publishVelocity method
        self.timerInterval = 0.5
        self.timer = self.create_timer(self.timerInterval, self.publishVelocity)

    def odomCallback(self, msg: Odometry):
        # Store the received odometry data
        self.odomData = msg

    def publishVelocity(self):
        # Create a Twist message for velocity commands
        twistMsg = Twist()
        twistMsg.linear.x = 1.0
        twistMsg.angular.z = 0.0

        # Adjust angular velocity based on the robot's x position
        xPosition = self.odomData.pose.pose.position.x
        if xPosition > 9.0:
            twistMsg.angular.z = 1.4
        elif xPosition < 1.5:
            twistMsg.angular.z = -1.4

        # Publish the velocity command
        self.velocityPublisher.publish(twistMsg)

def main(args=None):
    rclpy.init(args=args)
    node = OdomVelController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
