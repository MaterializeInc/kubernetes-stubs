import datetime
import typing

import kubernetes.client

class V1alpha1ResourceClass:
    api_version: typing.Optional[str]
    driver_name: str
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    parameters_ref: typing.Optional[
        kubernetes.client.V1alpha1ResourceClassParametersReference
    ]
    suitable_nodes: typing.Optional[kubernetes.client.V1NodeSelector]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        driver_name: str,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        parameters_ref: typing.Optional[
            kubernetes.client.V1alpha1ResourceClassParametersReference
        ] = ...,
        suitable_nodes: typing.Optional[kubernetes.client.V1NodeSelector] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1ResourceClassDict: ...

class V1alpha1ResourceClassDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    driverName: str
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
    parametersRef: typing.Optional[
        kubernetes.client.V1alpha1ResourceClassParametersReferenceDict
    ]
    suitableNodes: typing.Optional[kubernetes.client.V1NodeSelectorDict]
