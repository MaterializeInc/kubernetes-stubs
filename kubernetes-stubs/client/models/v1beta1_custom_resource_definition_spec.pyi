import datetime
import typing

import kubernetes.client

class V1beta1CustomResourceDefinitionSpec:
    additional_printer_columns: typing.Optional[
        list[kubernetes.client.V1beta1CustomResourceColumnDefinition]
    ]
    conversion: typing.Optional[kubernetes.client.V1beta1CustomResourceConversion]
    group: str
    names: kubernetes.client.V1beta1CustomResourceDefinitionNames
    preserve_unknown_fields: typing.Optional[bool]
    scope: str
    subresources: typing.Optional[kubernetes.client.V1beta1CustomResourceSubresources]
    validation: typing.Optional[kubernetes.client.V1beta1CustomResourceValidation]
    version: typing.Optional[str]
    versions: typing.Optional[
        list[kubernetes.client.V1beta1CustomResourceDefinitionVersion]
    ]
    def __init__(
        self,
        *,
        additional_printer_columns: typing.Optional[
            list[kubernetes.client.V1beta1CustomResourceColumnDefinition]
        ] = ...,
        conversion: typing.Optional[
            kubernetes.client.V1beta1CustomResourceConversion
        ] = ...,
        group: str,
        names: kubernetes.client.V1beta1CustomResourceDefinitionNames,
        preserve_unknown_fields: typing.Optional[bool] = ...,
        scope: str,
        subresources: typing.Optional[
            kubernetes.client.V1beta1CustomResourceSubresources
        ] = ...,
        validation: typing.Optional[
            kubernetes.client.V1beta1CustomResourceValidation
        ] = ...,
        version: typing.Optional[str] = ...,
        versions: typing.Optional[
            list[kubernetes.client.V1beta1CustomResourceDefinitionVersion]
        ] = ...
    ) -> None: ...
