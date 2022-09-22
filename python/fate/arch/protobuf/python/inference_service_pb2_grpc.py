# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import inference_service_pb2 as inference__service__pb2


class InferenceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.inference = channel.unary_unary(
            "/com.webank.ai.fate.api.serving.InferenceService/inference",
            request_serializer=inference__service__pb2.InferenceMessage.SerializeToString,
            response_deserializer=inference__service__pb2.InferenceMessage.FromString,
        )
        self.startInferenceJob = channel.unary_unary(
            "/com.webank.ai.fate.api.serving.InferenceService/startInferenceJob",
            request_serializer=inference__service__pb2.InferenceMessage.SerializeToString,
            response_deserializer=inference__service__pb2.InferenceMessage.FromString,
        )
        self.getInferenceResult = channel.unary_unary(
            "/com.webank.ai.fate.api.serving.InferenceService/getInferenceResult",
            request_serializer=inference__service__pb2.InferenceMessage.SerializeToString,
            response_deserializer=inference__service__pb2.InferenceMessage.FromString,
        )


class InferenceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def inference(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def startInferenceJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def getInferenceResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_InferenceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "inference": grpc.unary_unary_rpc_method_handler(
            servicer.inference,
            request_deserializer=inference__service__pb2.InferenceMessage.FromString,
            response_serializer=inference__service__pb2.InferenceMessage.SerializeToString,
        ),
        "startInferenceJob": grpc.unary_unary_rpc_method_handler(
            servicer.startInferenceJob,
            request_deserializer=inference__service__pb2.InferenceMessage.FromString,
            response_serializer=inference__service__pb2.InferenceMessage.SerializeToString,
        ),
        "getInferenceResult": grpc.unary_unary_rpc_method_handler(
            servicer.getInferenceResult,
            request_deserializer=inference__service__pb2.InferenceMessage.FromString,
            response_serializer=inference__service__pb2.InferenceMessage.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "com.webank.ai.fate.api.serving.InferenceService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class InferenceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def inference(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/com.webank.ai.fate.api.serving.InferenceService/inference",
            inference__service__pb2.InferenceMessage.SerializeToString,
            inference__service__pb2.InferenceMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def startInferenceJob(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/com.webank.ai.fate.api.serving.InferenceService/startInferenceJob",
            inference__service__pb2.InferenceMessage.SerializeToString,
            inference__service__pb2.InferenceMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def getInferenceResult(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/com.webank.ai.fate.api.serving.InferenceService/getInferenceResult",
            inference__service__pb2.InferenceMessage.SerializeToString,
            inference__service__pb2.InferenceMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
