import datetime
import typing

import kubernetes.client

class V1beta1MutatingWebhookConfigurationList:
    api_version: typing.Optional[str]
    items: list[kubernetes.client.V1beta1MutatingWebhookConfiguration]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1beta1MutatingWebhookConfiguration],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...
    ) -> None: ...
