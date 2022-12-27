from detection_helpers import *
from tracking_helpers import *
from printing_helpers import *
from bridge_wrapper import *
from PIL import Image
import sys

if len(sys.argv) < 3:
    print("Usage: python main.py <model_path> <video_path>")
    exit(1)

model_path = sys.argv[1]
video_path = sys.argv[2]

# Load the model
detector = Detector(classes=[0])

detector.load_model(model_path,)

print("Detector loaded.")

tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)

print("Starting tracking...")
# Track the video
results, frame_data = tracker.track_video(video_path, output="/Users/bugra/Desktop/deepsort/yolov7-deepsort-tracking/IO_data/output/output.avi", skip_frames=0, show_live=False, count_objects=True, verbose=1)



