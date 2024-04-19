from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_service_server_custom_srv_pkg',
            executable='movement_server_node',
            output='screen'),
    ])