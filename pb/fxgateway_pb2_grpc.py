# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import fxgateway_pb2 as fxgateway__pb2


class FxGatewayStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Invoke = channel.unary_unary(
                '/pb.FxGateway/Invoke',
                request_serializer=fxgateway__pb2.InvokeServiceRequest.SerializeToString,
                response_deserializer=fxgateway__pb2.Message.FromString,
                )
        self.List = channel.unary_unary(
                '/pb.FxGateway/List',
                request_serializer=fxgateway__pb2.Empty.SerializeToString,
                response_deserializer=fxgateway__pb2.Functions.FromString,
                )
        self.Deploy = channel.unary_unary(
                '/pb.FxGateway/Deploy',
                request_serializer=fxgateway__pb2.CreateFunctionRequest.SerializeToString,
                response_deserializer=fxgateway__pb2.Message.FromString,
                )
        self.Delete = channel.unary_unary(
                '/pb.FxGateway/Delete',
                request_serializer=fxgateway__pb2.DeleteFunctionRequest.SerializeToString,
                response_deserializer=fxgateway__pb2.Message.FromString,
                )
        self.Update = channel.unary_unary(
                '/pb.FxGateway/Update',
                request_serializer=fxgateway__pb2.CreateFunctionRequest.SerializeToString,
                response_deserializer=fxgateway__pb2.Message.FromString,
                )
        self.GetMeta = channel.unary_unary(
                '/pb.FxGateway/GetMeta',
                request_serializer=fxgateway__pb2.FunctionRequest.SerializeToString,
                response_deserializer=fxgateway__pb2.Function.FromString,
                )
        self.GetLog = channel.unary_unary(
                '/pb.FxGateway/GetLog',
                request_serializer=fxgateway__pb2.FunctionRequest.SerializeToString,
                response_deserializer=fxgateway__pb2.Message.FromString,
                )
        self.ReplicaUpdate = channel.unary_unary(
                '/pb.FxGateway/ReplicaUpdate',
                request_serializer=fxgateway__pb2.ScaleServiceRequest.SerializeToString,
                response_deserializer=fxgateway__pb2.Message.FromString,
                )
        self.Info = channel.unary_unary(
                '/pb.FxGateway/Info',
                request_serializer=fxgateway__pb2.Empty.SerializeToString,
                response_deserializer=fxgateway__pb2.Message.FromString,
                )
        self.HealthCheck = channel.unary_unary(
                '/pb.FxGateway/HealthCheck',
                request_serializer=fxgateway__pb2.Empty.SerializeToString,
                response_deserializer=fxgateway__pb2.Message.FromString,
                )


class FxGatewayServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Invoke(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deploy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMeta(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLog(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicaUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HealthCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FxGatewayServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Invoke': grpc.unary_unary_rpc_method_handler(
                    servicer.Invoke,
                    request_deserializer=fxgateway__pb2.InvokeServiceRequest.FromString,
                    response_serializer=fxgateway__pb2.Message.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=fxgateway__pb2.Empty.FromString,
                    response_serializer=fxgateway__pb2.Functions.SerializeToString,
            ),
            'Deploy': grpc.unary_unary_rpc_method_handler(
                    servicer.Deploy,
                    request_deserializer=fxgateway__pb2.CreateFunctionRequest.FromString,
                    response_serializer=fxgateway__pb2.Message.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=fxgateway__pb2.DeleteFunctionRequest.FromString,
                    response_serializer=fxgateway__pb2.Message.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=fxgateway__pb2.CreateFunctionRequest.FromString,
                    response_serializer=fxgateway__pb2.Message.SerializeToString,
            ),
            'GetMeta': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMeta,
                    request_deserializer=fxgateway__pb2.FunctionRequest.FromString,
                    response_serializer=fxgateway__pb2.Function.SerializeToString,
            ),
            'GetLog': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLog,
                    request_deserializer=fxgateway__pb2.FunctionRequest.FromString,
                    response_serializer=fxgateway__pb2.Message.SerializeToString,
            ),
            'ReplicaUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicaUpdate,
                    request_deserializer=fxgateway__pb2.ScaleServiceRequest.FromString,
                    response_serializer=fxgateway__pb2.Message.SerializeToString,
            ),
            'Info': grpc.unary_unary_rpc_method_handler(
                    servicer.Info,
                    request_deserializer=fxgateway__pb2.Empty.FromString,
                    response_serializer=fxgateway__pb2.Message.SerializeToString,
            ),
            'HealthCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.HealthCheck,
                    request_deserializer=fxgateway__pb2.Empty.FromString,
                    response_serializer=fxgateway__pb2.Message.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.FxGateway', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FxGateway(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Invoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.FxGateway/Invoke',
            fxgateway__pb2.InvokeServiceRequest.SerializeToString,
            fxgateway__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.FxGateway/List',
            fxgateway__pb2.Empty.SerializeToString,
            fxgateway__pb2.Functions.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deploy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.FxGateway/Deploy',
            fxgateway__pb2.CreateFunctionRequest.SerializeToString,
            fxgateway__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.FxGateway/Delete',
            fxgateway__pb2.DeleteFunctionRequest.SerializeToString,
            fxgateway__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.FxGateway/Update',
            fxgateway__pb2.CreateFunctionRequest.SerializeToString,
            fxgateway__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMeta(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.FxGateway/GetMeta',
            fxgateway__pb2.FunctionRequest.SerializeToString,
            fxgateway__pb2.Function.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.FxGateway/GetLog',
            fxgateway__pb2.FunctionRequest.SerializeToString,
            fxgateway__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicaUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.FxGateway/ReplicaUpdate',
            fxgateway__pb2.ScaleServiceRequest.SerializeToString,
            fxgateway__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.FxGateway/Info',
            fxgateway__pb2.Empty.SerializeToString,
            fxgateway__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HealthCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.FxGateway/HealthCheck',
            fxgateway__pb2.Empty.SerializeToString,
            fxgateway__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)