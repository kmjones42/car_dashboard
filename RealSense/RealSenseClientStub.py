
import grpc
import realsenseservice_pb2
import realsenseservice_pb2_grpc

import pyrealsense2 as rs
import numpy as np
import cv2

with grpc.insecure_channel('[::]:50053') as channel:
    stub = realsenseservice_pb2_grpc.RealSenseStub(channel)

    request_data = realsenseservice_pb2.RequestVideo(left_image=True)

    for current_data in stub.StreamVideo(request_data):
        # print(current_data.frame)
        np_img = np.frombuffer(current_data.frame, dtype=np.uint8)

        img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
        img = img.reshape(480, 640, 3)
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', img)
        k = cv2.waitKey(1)

        if k == ord('q'):
            break
