
# import daemon
from concurrent import futures

import grpc
import realsenseservice_pb2
import realsenseservice_pb2_grpc

import pyrealsense2 as rs
import numpy as np
import cv2


class RealSense():
    def __init__(self):
        print("Setting up RealSense")
        config = rs.config()
        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        self.pipeline = rs.pipeline()
        try:         
            self.pipeline.start(config)
        except RuntimeError:
            raise ConnectionError

    def get_frame(self):
        print("Sending frames")
        while True:
            print("First frame")
            frame = self.pipeline.wait_for_frames().get_color_frame()
            print("second frame")
            if not frame:
                print("Continuing")
                continue

            color_image = np.asanyarray(frame.get_data())
            img = cv2.imencode('.jpg', color_image)[1]
            yield realsenseservice_pb2.RealSenseVideoFrame(frame=img.tobytes())


class RealSenseServer(realsenseservice_pb2_grpc.RealSenseServicer):

    def StreamVideo(self, request, context):
        try:
            realsense = RealSense()
        except ConnectionError:
            context.abort(grpc.StatusCode.UNAVAILABLE, "Could not connect to RealSense camera.")
        

        return realsense.get_frame()


def serve_realsense_data():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    realsenseservice_pb2_grpc.add_RealSenseServicer_to_server(RealSenseServer(), server)

    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve_realsense_data()

# with daemon.DaemonContext():
#     serve_realsense_data()
