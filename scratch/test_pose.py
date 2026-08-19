from ultralytics import YOLO

model = YOLO("yolov8n-pose.pt")  # load a pretrained model (recommended for training)
results = model.track(source="C:\\Users\\liamb\\Source\\Project Tony Stark\\YolfCV\\videoplayback (1).mp4", save=True)  # track an object in a video file

Golfer_Track_ID = 1.0

KeyPointNames = [
    "nose", "left_eye", "right_eye", "left_ear", "right_ear",
    "left_shoulder", "right_shoulder", "left_elbow", "right_elbow",
    "left_wrist", "right_wrist", "left_hip", "right_hip",
    "left_knee", "right_knee", "left_ankle", "right_ankle"
]  

for frame_result in results:
    boxes = frame_result.boxes
    if boxes is None or boxes.id is None:
        continue

    ids = boxes.id.tolist()
    if Golfer_Track_ID not in ids:
        continue

    golfer_idx = ids.index(Golfer_Track_ID)
    golfer_keypoints = frame_result.keypoints.xy[golfer_idx]

    keypoints_dict = {name: [round(x,2), round(y,2)] for name, (x,y) in zip(KeyPointNames, golfer_keypoints.tolist())}

    print(keypoints_dict)