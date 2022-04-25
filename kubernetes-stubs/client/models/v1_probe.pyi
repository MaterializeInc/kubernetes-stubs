import datetime
import typing

import kubernetes.client

class V1Probe:
    exec: typing.Optional[kubernetes.client.V1ExecAction]
    failure_threshold: typing.Optional[int]
    grpc: typing.Optional[kubernetes.client.V1GRPCAction]
    http_get: typing.Optional[kubernetes.client.V1HTTPGetAction]
    initial_delay_seconds: typing.Optional[int]
    period_seconds: typing.Optional[int]
    success_threshold: typing.Optional[int]
    tcp_socket: typing.Optional[kubernetes.client.V1TCPSocketAction]
    termination_grace_period_seconds: typing.Optional[int]
    timeout_seconds: typing.Optional[int]
    def __init__(
        self,
        *,
        exec: typing.Optional[kubernetes.client.V1ExecAction] = ...,
        failure_threshold: typing.Optional[int] = ...,
        grpc: typing.Optional[kubernetes.client.V1GRPCAction] = ...,
        http_get: typing.Optional[kubernetes.client.V1HTTPGetAction] = ...,
        initial_delay_seconds: typing.Optional[int] = ...,
        period_seconds: typing.Optional[int] = ...,
        success_threshold: typing.Optional[int] = ...,
        tcp_socket: typing.Optional[kubernetes.client.V1TCPSocketAction] = ...,
        termination_grace_period_seconds: typing.Optional[int] = ...,
        timeout_seconds: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V1ProbeDict: ...

class V1ProbeDict(typing.TypedDict, total=False):
    exec: typing.Optional[kubernetes.client.V1ExecActionDict]
    failureThreshold: typing.Optional[int]
    grpc: typing.Optional[kubernetes.client.V1GRPCActionDict]
    httpGet: typing.Optional[kubernetes.client.V1HTTPGetActionDict]
    initialDelaySeconds: typing.Optional[int]
    periodSeconds: typing.Optional[int]
    successThreshold: typing.Optional[int]
    tcpSocket: typing.Optional[kubernetes.client.V1TCPSocketActionDict]
    terminationGracePeriodSeconds: typing.Optional[int]
    timeoutSeconds: typing.Optional[int]
