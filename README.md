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


### 2️⃣ Mask

Once the **RGB and Depth images** are prepared, a **mask** is required. 

- If you intend to use the model in real-time, masks can be obtained through other methods.
- However, in this model, **pose estimation is performed only for the first scene**, and the system switches to **tracking mode** afterward.
- Therefore, you only need to generate a mask for the **first frame**.

#### How to Create a Mask
- You can use your own **segmentation model** to generate masks and save them as shown in the example image.
- Alternatively, you can manually create masks using the `masking.py` script provided in this repository.
![image](https://github.com/user-attachments/assets/9d83059d-fffd-471c-b408-de3b7d3af349)

#### ⚠️ Important Notes
- Ensure that the saved **image path** matches the expected directory structure for the model.

### 3️⃣ CAD Model

You will need a **CAD model** that matches your object of interest.  
However, the key point is that **this model uses meters as the unit** for CAD models.  

#### ⚠️ Important Notes
- If you are using **Blender**, make sure to apply a **1000x scaling** to convert from millimeters to meters.

---

### 4️⃣ cam_K.txt (Camera Intrinsics)

The file **cam_K.txt** should store the intrinsic parameters of the camera being used. If you are using a simulation environment, you can retrieve these parameters by running the following command:

```bash
rostopic echo /camera_info
```

For a real-world setup, you will need to go through a **camera calibration** process to obtain these values.

# Final Steps

Once these steps are completed, all necessary data is prepared. In the `run_demo` script, use `argparse` to specify the required file paths. This step is straightforward. 



https://github.com/user-attachments/assets/ac16a72d-b885-4707-97c7-47e5ce16f003



If you encounter any issues, feel free to reach out. I will assist as much as possible.

Contact: cseklee234@naver.com

