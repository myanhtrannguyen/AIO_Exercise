import numpy as np
from google.colab.patches import cv2_imshow
import cv2

bg1_image = cv2.imread('GreenBackground.jpg.webp', 1)
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread('Object.jpg.webp', 1)
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread('NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image, (678, 381))

def compute_difference (bg_img, input_img):
  difference_single_channel = cv2.absdiff(bg_img, input_img)
  cv2_imshow(difference_single_channel)
  return difference_single_channel

def compute_binary_mask (difference_single_channel):
  _, binary_mask = cv2.threshold(difference_single_channel, 127, 255, cv2.THRESH_BINARY)
  cv2_imshow(binary_mask)
  return binary_mask

def replace_background (bg1_image, bg2_image, ob_image):
  difference_single_channel = compute_difference(bg1_image, ob_image)
  binary_mask = compute_binary_mask(difference_single_channel)
  output = np.where(binary_mask == 255, ob_image, bg2_image)
  return output

replace_background(bg1_image, bg2_image, ob_image)
