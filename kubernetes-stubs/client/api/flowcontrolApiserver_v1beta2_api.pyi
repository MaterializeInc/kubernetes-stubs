import typing

import kubernetes.client

class FlowcontrolApiserverV1beta2Api:
    def __init__(
        self, api_client: typing.Optional[kubernetes.client.ApiClient] = ...
    ) -> None: ...
    def get_api_resources(self) -> kubernetes.client.V1APIResourceList: ...
    def list_flow_schema(
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
    ) -> kubernetes.client.V1beta2FlowSchemaList: ...
    def create_flow_schema(
        self,
        body: kubernetes.client.V1beta2FlowSchema,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...
    ) -> kubernetes.client.V1beta2FlowSchema: ...
    def delete_collection_flow_schema(
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
    def read_flow_schema(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes.client.V1beta2FlowSchema: ...
    def replace_flow_schema(
        self,
        name: str,
        body: kubernetes.client.V1beta2FlowSchema,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...
    ) -> kubernetes.client.V1beta2FlowSchema: ...
    def delete_flow_schema(
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
    def patch_flow_schema(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> kubernetes.client.V1beta2FlowSchema: ...
    def read_flow_schema_status(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes.client.V1beta2FlowSchema: ...
    def replace_flow_schema_status(
        self,
        name: str,
        body: kubernetes.client.V1beta2FlowSchema,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...
    ) -> kubernetes.client.V1beta2FlowSchema: ...
    def patch_flow_schema_status(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> kubernetes.client.V1beta2FlowSchema: ...
    def list_priority_level_configuration(
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
    ) -> kubernetes.client.V1beta2PriorityLevelConfigurationList: ...
    def create_priority_level_configuration(
        self,
        body: kubernetes.client.V1beta2PriorityLevelConfiguration,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...
    ) -> kubernetes.client.V1beta2PriorityLevelConfiguration: ...
    def delete_collection_priority_level_configuration(
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
    def read_priority_level_configuration(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes.client.V1beta2PriorityLevelConfiguration: ...
    def replace_priority_level_configuration(
        self,
        name: str,
        body: kubernetes.client.V1beta2PriorityLevelConfiguration,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...
    ) -> kubernetes.client.V1beta2PriorityLevelConfiguration: ...
    def delete_priority_level_configuration(
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
    def patch_priority_level_configuration(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> kubernetes.client.V1beta2PriorityLevelConfiguration: ...
    def read_priority_level_configuration_status(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes.client.V1beta2PriorityLevelConfiguration: ...
    def replace_priority_level_configuration_status(
        self,
        name: str,
        body: kubernetes.client.V1beta2PriorityLevelConfiguration,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...
    ) -> kubernetes.client.V1beta2PriorityLevelConfiguration: ...
    def patch_priority_level_configuration_status(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> kubernetes.client.V1beta2PriorityLevelConfiguration: ...
