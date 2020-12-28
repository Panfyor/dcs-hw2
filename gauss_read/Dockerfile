FROM python:3
MAINTAINER Vladislav Panferov


ADD read.py .
RUN apt-get clean && apt-get update
RUN apt-get install libgl1-mesa-glx -y
RUN pip install numpy
RUN pip install opencv-python
RUN pip install matplotlib


RUN wget https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png

CMD ["python", "read.py"]
