import cv2
import numpy as np
from tqdm import tqdm


video_path = "output.avi"

cap = cv2.VideoCapture(video_path)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

block_size = 40

binary_data = b""

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

for _ in tqdm(range(total_frames)):
    ret, frame = cap.read()
    if not ret:
        break
    
    block_matrix = np.zeros((frame_height, frame_width), dtype=np.uint8)
    for i in range(frame_width // block_size):
        block = frame[:, i*block_size:(i+1)*block_size]
        if np.mean(block) > 127.5:
            binary_data += b"1"
            block_matrix[:, i*block_size:(i+1)*block_size] = 255
        else:
            binary_data += b"0"
    
cv2.destroyAllWindows()
cap.release()

output_path = "output.rar"
with open(output_path, "wb") as f:
    f.write(binary_data)

print(f"Binary data written to {output_path}.")
