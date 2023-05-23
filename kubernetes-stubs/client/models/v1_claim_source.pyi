import datetime
import typing

import kubernetes.client

class V1ClaimSource:
    resource_claim_name: typing.Optional[str]
    resource_claim_template_name: typing.Optional[str]
    def __init__(
        self,
        *,
        resource_claim_name: typing.Optional[str] = ...,
        resource_claim_template_name: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1ClaimSourceDict: ...

class V1ClaimSourceDict(typing.TypedDict, total=False):
    resourceClaimName: typing.Optional[str]
    resourceClaimTemplateName: typing.Optional[str]
