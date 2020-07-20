# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import obdservice_pb2 as obdservice__pb2


class ObdStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamObd = channel.unary_stream(
                '/OBD.Obd/StreamObd',
                request_serializer=obdservice__pb2.ObdDataTypes.SerializeToString,
                response_deserializer=obdservice__pb2.ObdData.FromString,
                )


class ObdServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StreamObd(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ObdServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamObd': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamObd,
                    request_deserializer=obdservice__pb2.ObdDataTypes.FromString,
                    response_serializer=obdservice__pb2.ObdData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'OBD.Obd', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Obd(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StreamObd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/OBD.Obd/StreamObd',
            obdservice__pb2.ObdDataTypes.SerializeToString,
            obdservice__pb2.ObdData.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)