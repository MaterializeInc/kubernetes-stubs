import datetime
import typing

import kubernetes.client

class V1CertificateSigningRequestSpec:
    extra: typing.Optional[dict[str, list[str]]]
    groups: typing.Optional[list[str]]
    request: str
    signer_name: str
    uid: typing.Optional[str]
    usages: typing.Optional[list[str]]
    username: typing.Optional[str]
    def __init__(
        self,
        *,
        extra: typing.Optional[dict[str, list[str]]] = ...,
        groups: typing.Optional[list[str]] = ...,
        request: str,
        signer_name: str,
        uid: typing.Optional[str] = ...,
        usages: typing.Optional[list[str]] = ...,
        username: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1CertificateSigningRequestSpecDict: ...

class V1CertificateSigningRequestSpecDict(typing.TypedDict, total=False):
    extra: typing.Optional[dict[str, list[str]]]
    groups: typing.Optional[list[str]]
    request: str
    signerName: str
    uid: typing.Optional[str]
    usages: typing.Optional[list[str]]
    username: typing.Optional[str]
