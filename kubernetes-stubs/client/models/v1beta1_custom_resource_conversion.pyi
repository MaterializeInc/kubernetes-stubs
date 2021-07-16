import datetime
import typing

import kubernetes.client

class V1beta1CustomResourceConversion:
    conversion_review_versions: typing.Optional[list[str]]
    strategy: str
    webhook_client_config: typing.Optional[
        kubernetes.client.ApiextensionsV1beta1WebhookClientConfig
    ]
    def __init__(
        self,
        *,
        conversion_review_versions: typing.Optional[list[str]] = ...,
        strategy: str,
        webhook_client_config: typing.Optional[
            kubernetes.client.ApiextensionsV1beta1WebhookClientConfig
        ] = ...
    ) -> None: ...
