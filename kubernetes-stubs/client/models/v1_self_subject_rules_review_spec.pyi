import datetime
import typing

import kubernetes.client

class V1SelfSubjectRulesReviewSpec:
    namespace: typing.Optional[str]
    def __init__(self, *, namespace: typing.Optional[str] = ...) -> None: ...
