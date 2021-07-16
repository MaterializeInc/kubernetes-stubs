import datetime
import typing

import kubernetes.client

class V1alpha1Webhook:
    client_config: kubernetes.client.V1alpha1WebhookClientConfig
    throttle: typing.Optional[kubernetes.client.V1alpha1WebhookThrottleConfig]
    def __init__(
        self,
        *,
        client_config: kubernetes.client.V1alpha1WebhookClientConfig,
        throttle: typing.Optional[kubernetes.client.V1alpha1WebhookThrottleConfig] = ...
    ) -> None: ...
