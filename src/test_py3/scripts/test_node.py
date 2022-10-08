#! /home/yi/3rdParties/Anaconda3/envs/ros_env/bin/python
"""
    Python 版本的 HelloVScode，执行在控制台输出 HelloVScode
    实现:
    1.导包
    2.初始化 ROS 节点 
    3.日志输出 HelloWorld
"""
import numpy 
import rospy # 1.导包
from cv_bridge import CvBridge

if __name__ == "__main__":

    rospy.init_node("Hello_Vscode_p")  # 2.初始化 ROS 节点
    rospy.loginfo("Hello VScode, 我是 Python ....")  #3.日志输出 HelloWorld