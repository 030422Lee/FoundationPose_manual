## FoundationPose Execution Guide

This page provides a guide to running the **FoundationPose** model easily and summarizes potential issues that may arise. Hope this helps!

It is assumed that the **[official FoundationPose repository](https://github.com/NVlabs/FoundationPose)** has already been set up, including the Docker configuration and weight files.

## 📂 Required Data for Model-based Execution

To run this model using the **Model-based (CAD model available) approach**, you need to prepare the following five types of data.

![image](https://github.com/user-attachments/assets/847fd22c-90b3-485a-8245-e68b2a9a8b5b)

### 1️⃣ RGB & Depth
- **RGB Image**: Standard RGB images in `.png` format, saved with matching timestamps.
- **Depth Image**: Corresponding depth images with the same timestamps as the RGB images.

#### ⚠️ Important Notes
- I tested with an **800×800** resolution dataset.  
  For reference, When running with **1920×1080** resolution, even an **RTX 3090** experienced memory issues(24GB). 
- The script `data_saver.py` can be used to **subscribe to ROS topics** and save RGB and Depth images in the specified directory.
- The topic names depend on the sensor you are using, and you should adjust the save path accordingly.
- **The RGB and depth images must have identical filenames and timestamps.**
