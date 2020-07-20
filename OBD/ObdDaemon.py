
# import daemon
from concurrent import futures
import time
import obd

import grpc
import obdservice_pb2
import obdservice_pb2_grpc

keys = ['RPM', 'SPEED']
cmds = {key: getattr(obd.commands,key) for key in keys}


class Obd(obdservice_pb2_grpc.ObdServicer):
    def __init__(self):
        print("Setting up listener")
        self.connection = self.connect_obd()
        print("Connected")
        self.keys = []

    def StreamObd(self, request, context):
        print("Got a connection")
        if request.speed:
            self.keys.append("SPEED")
        if request.rpm:
            self.keys.append("RPM") 
        self.cmds = {key: getattr(obd.commands,key) for key in keys}

        return self.query_obd_data()

    def connect_obd(self):
        connection = obd.OBD()

        if not connection.is_connected():
            print("Could not connect to OBD, exiting.")
            exit(1);

        return connection

    def query_obd_data(self):
        while True:
            for key, cmd in self.cmds.items():
                if key == 'SPEED':
                    speed = str(connection.query(cmd).value)
                if key == 'RPM':
                    rpm = str(connection.query(cmd).value)

        yield route_guide_pb2.ObdData(currentspeed=speed, currentrpm=rpm)


def serve_obd_data():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    obdservice_pb2_grpc.add_ObdServicer_to_server(Obd(), server)

    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve_obd_data()    

# with daemon.DaemonContext():
#     serve_obd_data()