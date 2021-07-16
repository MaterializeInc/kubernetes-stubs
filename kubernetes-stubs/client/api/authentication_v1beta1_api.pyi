import typing

import kubernetes.client

class AuthenticationV1beta1Api:
    def get_api_resources(self) -> kubernetes.client.V1APIResourceList: ...
    def create_token_review(
        self,
        body: kubernetes.client.V1beta1TokenReview,
        *,
        dryRun: typing.Optional[str] = ...,
        fieldManager: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...
    ) -> kubernetes.client.V1beta1TokenReview: ...
