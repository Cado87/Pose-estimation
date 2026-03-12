from ultralytics import YOLO
import tkinter as tk
from tkinter import filedialog
import argparse
import os
import sys  # Import sys for exiting the script

# Parse command-line arguments
parser = argparse.ArgumentParser(description="YOLO Tracking Script")
parser.add_argument("--source", type=str, choices=["webcam", "video"], required=True,
                    help="Choose the source: 'webcam' for webcam or 'video' for a video file")
parser.add_argument("--model", type=str, required=True,
                    help="Path to the YOLO model file (e.g., yolov8m, yolo11n, yolo11n-seg, yolo11n-pose')")
parser.add_argument("--conf", type=float, default=0.25,
                    help="Confidence threshold for detections (0.0-1.0, default: 0.25)")
args = parser.parse_args()


# Construct the full model path
model_path = os.path.join("models", f"{args.model}.pt")

# Load the specified model
try:
    model = YOLO(model_path)
    print(f"Model '{model_path}' loaded successfully.")
except Exception as e:
    print(f"Error loading model '{model_path}': {e}")
    sys.exit(1)


if args.source == "webcam":
    results = model.track(source=0, conf=args.conf, show=True)
elif args.source == "video":
    # Ask the user for the video file path using a file dialog
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    video_path = filedialog.askopenfilename(title="Select the video file", filetypes=[("Video files", "*.mp4;*.avi;*.mov")])

    if video_path:
        results = model.track(video_path, conf=args.conf, show=True)  # Tracking with default tracker
    else:
        print("No video file selected. Exiting.")

else:
    print("Invalid source. Please choose 'webcam' or 'video'.")
    sys.exit(1)
