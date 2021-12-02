import datetime
import typing

import kubernetes.client

class V1alpha1StorageVersionStatus:
    common_encoding_version: typing.Optional[str]
    conditions: typing.Optional[list[kubernetes.client.V1alpha1StorageVersionCondition]]
    storage_versions: typing.Optional[
        list[kubernetes.client.V1alpha1ServerStorageVersion]
    ]
    def __init__(
        self,
        *,
        common_encoding_version: typing.Optional[str] = ...,
        conditions: typing.Optional[
            list[kubernetes.client.V1alpha1StorageVersionCondition]
        ] = ...,
        storage_versions: typing.Optional[
            list[kubernetes.client.V1alpha1ServerStorageVersion]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1StorageVersionStatusDict: ...

class V1alpha1StorageVersionStatusDict(typing.TypedDict, total=False):
    commonEncodingVersion: typing.Optional[str]
    conditions: typing.Optional[
        list[kubernetes.client.V1alpha1StorageVersionConditionDict]
    ]
    storageVersions: typing.Optional[
        list[kubernetes.client.V1alpha1ServerStorageVersionDict]
    ]
