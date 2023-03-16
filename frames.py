import cv2
import os

def extract_frames(video_path, output_dir, num_frames=16):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get the total number of frames in the video
    num_frames_total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate the step size for the sliding window based on the desired number of frames
    step_size = max(num_frames_total // num_frames, 1)

    # Initialize the current frame number and the frame counter
    frame_num = 0
    count = 0

    # Loop through the video frames and extract a frame every step_size frames
    while True:
        # Read the current frame
        ret, frame = cap.read()

        # If we've reached the end of the video, break out of the loop
        if not ret:
            break

        # If the current frame number is a multiple of the step size, save the frame
        if frame_num % step_size == 0:
            # Construct the output filename
            output_path = os.path.join(output_dir, f'frame_{count:04d}.jpg')

            # Save the frame to disk
            cv2.imwrite(output_path, frame)

            # Increment the frame counter
            count += 1

        # Increment the current frame number
        frame_num += 1

    # Release the video file
    cap.release()

    # Return the total number of frames extracted
    return count

# Define the input and output directories
input_dir = '/home/surya/PycharmProjects/video_classification/news'
output_dir = '/home/surya/PycharmProjects/video_classification/news_frames'



# Number of frames to extract from each video
num_frames = 16

# Loop through all video files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.mp4') or filename.endswith('.avi'):
        # Path to input and output files
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, os.path.splitext(filename)[0])

        # Create the output directory if it doesn't exist
        if not os.path.exists(output_file):
            os.makedirs(output_file)

        # Extract frames from the video file
        extract_frames(input_file, output_file, num_frames)

        print(f'{num_frames} frames extracted from {input_file} and saved to {output_file}')