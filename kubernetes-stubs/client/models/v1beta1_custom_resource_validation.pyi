import datetime
import typing

import kubernetes.client

class V1beta1CustomResourceValidation:
    open_apiv3_schema: typing.Optional[kubernetes.client.V1beta1JSONSchemaProps]
    def __init__(
        self,
        *,
        open_apiv3_schema: typing.Optional[
            kubernetes.client.V1beta1JSONSchemaProps
        ] = ...
    ) -> None: ...
