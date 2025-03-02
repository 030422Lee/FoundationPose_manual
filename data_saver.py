import rospy
import message_filters
from sensor_msgs.msg import Image
import cv2
import numpy as np
from cv_bridge import CvBridge
import os

# Define save paths for RGB and depth images
rgb_save_path = "/home/lee/FoundationPose/our_data/rgb"
depth_save_path = "/home/lee/FoundationPose/our_data/depth"

# Create directories if they do not exist
os.makedirs(rgb_save_path, exist_ok=True)
os.makedirs(depth_save_path, exist_ok=True)

# Initialize CvBridge for converting ROS images to OpenCV format
bridge = CvBridge()

def callback(rgb_msg, depth_msg):
    """ Callback function to process and save synchronized RGB and depth images """
    try:
        # Convert RGB ROS Image message to OpenCV format (BGR color format)
        rgb_image = bridge.imgmsg_to_cv2(rgb_msg, desired_encoding="bgr8")
        
        # Convert Depth ROS Image message to OpenCV format (Passthrough encoding to retain depth values)
        depth_image = bridge.imgmsg_to_cv2(depth_msg, desired_encoding="passthrough")

        # Generate a timestamp-based filename to ensure unique file names
        timestamp = rgb_msg.header.stamp.to_sec()
        rgb_filename = os.path.join(rgb_save_path, f"{timestamp:.6f}.png")
        depth_filename = os.path.join(depth_save_path, f"{timestamp:.6f}.png")

        # Save images to the specified directories
        cv2.imwrite(rgb_filename, rgb_image)
        cv2.imwrite(depth_filename, depth_image)

        rospy.loginfo(f"Saved RGB: {rgb_filename}, Depth: {depth_filename}")

    except Exception as e:
        rospy.logerr(f"Error processing images: {e}")

def main():
    """ Main function to initialize the ROS node and synchronize image topics """
    rospy.init_node("rgb_depth_saver", anonymous=True)

    # Subscribe to RGB and depth image topics from the camera
    rgb_sub = message_filters.Subscriber("/camera/color/image_raw", Image)
    depth_sub = message_filters.Subscriber("/camera/depth/image_raw", Image)

    # Synchronize the image topics with an ApproximateTimeSynchronizer
    # queue_size: Number of messages to store in the queue before discarding old messages
    # slop: Allowed timestamp difference (in seconds) between the two topics to consider them synchronized
    ts = message_filters.ApproximateTimeSynchronizer([rgb_sub, depth_sub], queue_size=10, slop=0.05)
    ts.registerCallback(callback)

    rospy.spin()  # Keep the node running

if __name__ == "__main__":
    main()
