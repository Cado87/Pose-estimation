# yolo_ultralytics
YOLO pose stimation
Sources: https://docs.ultralytics.com/tasks/pose

Conda environment
web: https://docs.ultralytics.com/guides/conda-quickstart/#prerequisites

If first time, create a new Conda environment. Open your terminal and run the following command:
conda create --name ultralytics-env python=3.11 -y

Activate the new environment:
conda activate ultralytics-env

To see environments created:
conda env list

Execute scripts using python.exe

Script Pose_estimation_yolo.py will download a model to models folder and open a window to start tracking


There is the possibility of input parameters:
python Pose_estimation_yolo.py --source video --model yolo11n --tracker parameters --conf 0.5

--source: webcam or video
--model: yolo11n, yolo11n-seg, yolo11n-pose, etc
--tracker: default, parameters, bytetrack or botsort
--conf: confidence threshold for detections (0.0-1.0, default: 0.25)

Run pose stimation:
python Pose_estimation_yolo.py --source webcam --model yolo11n-pose