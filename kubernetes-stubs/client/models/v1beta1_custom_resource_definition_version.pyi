import datetime
import typing

import kubernetes.client

class V1beta1CustomResourceDefinitionVersion:
    additional_printer_columns: typing.Optional[
        list[kubernetes.client.V1beta1CustomResourceColumnDefinition]
    ]
    name: str
    schema: typing.Optional[kubernetes.client.V1beta1CustomResourceValidation]
    served: bool
    storage: bool
    subresources: typing.Optional[kubernetes.client.V1beta1CustomResourceSubresources]
    def __init__(
        self,
        *,
        additional_printer_columns: typing.Optional[
            list[kubernetes.client.V1beta1CustomResourceColumnDefinition]
        ] = ...,
        name: str,
        schema: typing.Optional[
            kubernetes.client.V1beta1CustomResourceValidation
        ] = ...,
        served: bool,
        storage: bool,
        subresources: typing.Optional[
            kubernetes.client.V1beta1CustomResourceSubresources
        ] = ...
    ) -> None: ...
