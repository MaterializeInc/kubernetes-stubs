import typing

import kubernetes.client

class AdmissionregistrationV1alpha1Api:
    def __init__(
        self, api_client: typing.Optional[kubernetes.client.ApiClient] = ...
    ) -> None: ...
    def get_api_resources(self) -> kubernetes.client.V1APIResourceList: ...
    def list_validating_admission_policy(
        self,
        *,
        pretty: typing.Optional[str] = ...,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...
    ) -> kubernetes.client.V1alpha1ValidatingAdmissionPolicyList: ...
    def create_validating_admission_policy(
        self,
        body: kubernetes.client.V1alpha1ValidatingAdmissionPolicy,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...
    ) -> kubernetes.client.V1alpha1ValidatingAdmissionPolicy: ...
    def delete_collection_validating_admission_policy(
        self,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = ...,
        _continue: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        timeout_seconds: typing.Optional[int] = ...
    ) -> kubernetes.client.V1Status: ...
    def read_validating_admission_policy(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes.client.V1alpha1ValidatingAdmissionPolicy: ...
    def replace_validating_admission_policy(
        self,
        name: str,
        body: kubernetes.client.V1alpha1ValidatingAdmissionPolicy,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...
    ) -> kubernetes.client.V1alpha1ValidatingAdmissionPolicy: ...
    def delete_validating_admission_policy(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...
    ) -> kubernetes.client.V1Status: ...
    def patch_validating_admission_policy(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> kubernetes.client.V1alpha1ValidatingAdmissionPolicy: ...
    def list_validating_admission_policy_binding(
        self,
        *,
        pretty: typing.Optional[str] = ...,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...
    ) -> kubernetes.client.V1alpha1ValidatingAdmissionPolicyBindingList: ...
    def create_validating_admission_policy_binding(
        self,
        body: kubernetes.client.V1alpha1ValidatingAdmissionPolicyBinding,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...
    ) -> kubernetes.client.V1alpha1ValidatingAdmissionPolicyBinding: ...
    def delete_collection_validating_admission_policy_binding(
        self,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = ...,
        _continue: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        timeout_seconds: typing.Optional[int] = ...
    ) -> kubernetes.client.V1Status: ...
    def read_validating_admission_policy_binding(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes.client.V1alpha1ValidatingAdmissionPolicyBinding: ...
    def replace_validating_admission_policy_binding(
        self,
        name: str,
        body: kubernetes.client.V1alpha1ValidatingAdmissionPolicyBinding,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...
    ) -> kubernetes.client.V1alpha1ValidatingAdmissionPolicyBinding: ...
    def delete_validating_admission_policy_binding(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...
    ) -> kubernetes.client.V1Status: ...
    def patch_validating_admission_policy_binding(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> kubernetes.client.V1alpha1ValidatingAdmissionPolicyBinding: ...
