
# import daemon
from concurrent import futures
import time
import obd

import grpc
import obdservice_pb2
import obdservice_pb2_grpc


class Obd():
    def __init__(self, keys):
        print("Setting up listener")
        self.connection = self.connect_obd()
        if not self.connection.is_connected():
            raise ConnectionError
        print("OBD Connected")
        self.cmds = {key: getattr(obd.commands,key) for key in keys}

    def connect_obd(self):
        return obd.OBD()

    def query_obd_data(self):
        print("querying")
        while True:
            for key, cmd in self.cmds.items():
                if key == 'SPEED':
                    speed = str(self.connection.query(cmd).value)
                if key == 'RPM':
                    rpm = str(self.connection.query(cmd).value)

            yield route_guide_pb2.ObdResponse(currentspeed=speed, currentrpm=rpm)


class ObdServer(obdservice_pb2_grpc.ObdServicer):


    def StreamObd(self, request, context):
        print("Got a connection")

        keys = []
        if request.speed:
            keys.append("SPEED")
        if request.rpm:
            keys.append("RPM")

        try:
            obd_connection = Obd(keys)
        except ConnectionError:
            context.abort(grpc.StatusCode.UNAVAILABLE, "Could not connect to OBD.")

        return obd_connection.query_obd_data()


def serve_obd_data():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    obdservice_pb2_grpc.add_ObdServicer_to_server(ObdServer(), server)

    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve_obd_data()    

# with daemon.DaemonContext():
#     serve_obd_data()
