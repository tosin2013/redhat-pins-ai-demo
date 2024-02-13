!git clone https://github.com/bdherouville/redhat-edge-ai-industrial-demo.git
!git clone https://github.com/ultralytics/yolov5  # clone
!cd yolov5 && sed -i s/'opencv-python>'/'opencv-python-headless>'/g requirements.txt
!pip uninstall -y opencv-python opencv-python-headless
!cd yolov5 && pip install -r requirements.txt  # install