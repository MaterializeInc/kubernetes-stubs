import datetime
import typing

import kubernetes.client

class V1CustomResourceDefinitionVersion:
    additional_printer_columns: typing.Optional[
        list[kubernetes.client.V1CustomResourceColumnDefinition]
    ]
    deprecated: typing.Optional[bool]
    deprecation_warning: typing.Optional[str]
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
        deprecated: typing.Optional[bool] = ...,
        deprecation_warning: typing.Optional[str] = ...,
        name: str,
        schema: typing.Optional[kubernetes.client.V1CustomResourceValidation] = ...,
        served: bool,
        storage: bool,
        subresources: typing.Optional[
            kubernetes.client.V1CustomResourceSubresources
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1CustomResourceDefinitionVersionDict: ...

class V1CustomResourceDefinitionVersionDict(typing.TypedDict, total=False):
    additionalPrinterColumns: typing.Optional[
        list[kubernetes.client.V1CustomResourceColumnDefinitionDict]
    ]
    deprecated: typing.Optional[bool]
    deprecationWarning: typing.Optional[str]
    name: str
    schema: typing.Optional[kubernetes.client.V1CustomResourceValidationDict]
    served: bool
    storage: bool
    subresources: typing.Optional[kubernetes.client.V1CustomResourceSubresourcesDict]
