import datetime
import typing

import kubernetes.client

class V1WindowsSecurityContextOptions:
    gmsa_credential_spec: typing.Optional[str]
    gmsa_credential_spec_name: typing.Optional[str]
    run_as_user_name: typing.Optional[str]
    def __init__(
        self,
        *,
        gmsa_credential_spec: typing.Optional[str] = ...,
        gmsa_credential_spec_name: typing.Optional[str] = ...,
        run_as_user_name: typing.Optional[str] = ...
    ) -> None: ...
