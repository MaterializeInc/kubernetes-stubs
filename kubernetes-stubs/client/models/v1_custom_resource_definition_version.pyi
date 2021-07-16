import datetime
import typing

import kubernetes.client

class V1CustomResourceDefinitionVersion:
    additional_printer_columns: typing.Optional[
        list[kubernetes.client.V1CustomResourceColumnDefinition]
    ]
    name: str
    schema: typing.Optional[kubernetes.client.V1CustomResourceValidation]
    served: bool
    storage: bool
    subresources: typing.Optional[kubernetes.client.V1CustomResourceSubresources]
    def __init__(
        self,
        *,
        additional_printer_columns: typing.Optional[
            list[kubernetes.client.V1CustomResourceColumnDefinition]
        ] = ...,
        name: str,
        schema: typing.Optional[kubernetes.client.V1CustomResourceValidation] = ...,
        served: bool,
        storage: bool,
        subresources: typing.Optional[
            kubernetes.client.V1CustomResourceSubresources
        ] = ...
    ) -> None: ...
