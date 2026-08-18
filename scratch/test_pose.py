from ultralytics import YOLO

model = YOLO("yolov8n-pose.pt")  # load a pretrained model (recommended for training)
results = model.track(source="C:\\Users\\liamb\\Source\\Project Tony Stark\\YolfCV\\videoplayback (1).mp4", save=True)  # track an object in a video file
for frame_result in results:
    boxes = frame_result.boxes
    if boxes is None or len(boxes) == 0:
        continue
    areas = (boxes.xywh[:, 2] * boxes.xywh[:, 3])
    largest_idx = areas.argmax()

    golfer_keypoints = frame_result.keypoints[largest_idx]
    print(f"Detected {len(boxes)} people, using index {largest_idx}")
    print(golfer_keypoints.shape)