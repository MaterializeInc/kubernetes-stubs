import datetime
import typing

import kubernetes.client

class V1WebhookConversion:
    client_config: typing.Optional[kubernetes.client.ApiextensionsV1WebhookClientConfig]
    conversion_review_versions: list[str]
    def __init__(
        self,
        *,
        client_config: typing.Optional[
            kubernetes.client.ApiextensionsV1WebhookClientConfig
        ] = ...,
        conversion_review_versions: list[str]
    ) -> None: ...
