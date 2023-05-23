import typing

import kubernetes.client

class AuthenticationV1alpha1Api:
    def __init__(
        self, api_client: typing.Optional[kubernetes.client.ApiClient] = ...
    ) -> None: ...
    def get_api_resources(self) -> kubernetes.client.V1APIResourceList: ...
    def create_self_subject_review(
        self,
        body: kubernetes.client.V1alpha1SelfSubjectReview,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...
    ) -> kubernetes.client.V1alpha1SelfSubjectReview: ...
