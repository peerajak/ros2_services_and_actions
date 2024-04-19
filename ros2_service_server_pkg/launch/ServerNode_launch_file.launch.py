from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_service_server_pkg',
            executable='ServerNode_node',
            output='screen'),
    ])
