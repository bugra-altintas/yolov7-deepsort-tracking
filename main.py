from detection_helpers import *
from tracking_helpers import *
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

tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)


# Track the video
#tracker.track_video(video_path, output="output.avi", skip_frames=0, show_live=True, count_objects=True, verbose=1)
results = tracker.track_video(video_path, output="output.avi", skip_frames=0, show_live=True, count_objects=True, verbose=1)

print(results)


# calculate centers of bounding boxes

# id selection for tracking

# returning the results

############################################################################################################