
import grpc
import obdservice_pb2
import obdservice_pb2_grpc

with grpc.insecure_channel('[::]:50052') as channel:
    stub = obdservice_pb2_grpc.ObdStub(channel)

    request_data = obdservice_pb2.ObdDataTypes(speed=True, rpm=True)

    for current_data in stub.StreamObd(request_data):
        print(current_data.currentspeed, " ", current_data.currentrpm)