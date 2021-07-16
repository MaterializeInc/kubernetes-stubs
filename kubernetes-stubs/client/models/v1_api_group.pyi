import datetime
import typing

import kubernetes.client

class V1APIGroup:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    name: str
    preferred_version: typing.Optional[kubernetes.client.V1GroupVersionForDiscovery]
    server_address_by_client_cid_rs: typing.Optional[
        list[kubernetes.client.V1ServerAddressByClientCIDR]
    ]
    versions: list[kubernetes.client.V1GroupVersionForDiscovery]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        name: str,
        preferred_version: typing.Optional[
            kubernetes.client.V1GroupVersionForDiscovery
        ] = ...,
        server_address_by_client_cid_rs: typing.Optional[
            list[kubernetes.client.V1ServerAddressByClientCIDR]
        ] = ...,
        versions: list[kubernetes.client.V1GroupVersionForDiscovery]
    ) -> None: ...
