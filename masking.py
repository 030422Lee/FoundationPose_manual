import cv2
import numpy as np
import os

# ✅ Input image path
image_path = "your_image_path.png"
mask_save_path = "your_mask_save_path.png"

# ✅ Load image
image = cv2.imread(image_path)

# ⚠ Exception handling: Exit if image loading fails
if image is None:
    print(f"❌ Error: Cannot load image {image_path}")
    exit()

# ✅ Initialize mask
mask = np.zeros(image.shape[:2], dtype=np.uint8)  # Initial value: black (0)
drawing = False  # Mouse drag flag
brush_size = 10  # Initial brush size

# ✅ Mouse callback function (drawing feature)
def paint_mask(event, x, y, flags, param):
    global drawing, mask, brush_size
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(mask, (x, y), brush_size, 255, -1)  # Fill
    
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.circle(mask, (x, y), brush_size, 255, -1)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# ✅ Adjust brush size (using mouse wheel)
def change_brush_size(event, x, y, flags, param):
    global brush_size
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            brush_size = min(brush_size + 2, 50)  # Max 50
        else:
            brush_size = max(brush_size - 2, 2)   # Min 2
        print(f"🖌 Brush Size: {brush_size}")

# ✅ Display mask creation window
cv2.namedWindow("Paint Mask", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("Paint Mask", paint_mask)
cv2.imshow("Paint Mask", image)

while True:
    mask_overlay = cv2.addWeighted(image, 0.6, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR), 0.4, 0)
    cv2.imshow("Paint Mask", mask_overlay)
    key = cv2.waitKey(1)
    
    if key == 27:  # ESC key to exit
        break
    elif key == 115:  # 's' key to save
        os.makedirs(os.path.dirname(mask_save_path), exist_ok=True)
        cv2.imwrite(mask_save_path, mask)
        print(f"✅ Mask saved to {mask_save_path}")

cv2.destroyAllWindows()
