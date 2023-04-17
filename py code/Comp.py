import cv2
import numpy as np
from tqdm import tqdm


file_path = input()

with open(file_path, "rb") as f:
    binary_data = f.read()

frame_rate = 30  
frame_width = 1280  
frame_height = 720  

fourcc = cv2.VideoWriter_fourcc(*"XVID")
video_writer = cv2.VideoWriter("output.avi", fourcc, frame_rate, (frame_width, frame_height))

frame_count = 0
for byte in tqdm(binary_data):
    binary_string = bin(byte)[2:].zfill(8)

    block_size = 1
    block_matrix = np.zeros((frame_height, frame_width), dtype=np.uint8)
    for i, bit in enumerate(binary_string):
        x = i * block_size
        y = 0
        if bit == "1":
            block_matrix[y:y+block_size, x:x+block_size] = 255
            
    for i in range(3):
        video_writer.write(block_matrix)
        frame_count += 1

video_writer.release()

output_path = "output.avi"
with open(output_path, "wb") as f:
    f.write(binary_data)

print(f"Video created with {frame_count} frames.")
