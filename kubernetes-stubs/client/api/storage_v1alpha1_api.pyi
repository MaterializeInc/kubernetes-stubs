import typing

import kubernetes.client

class StorageV1alpha1Api:
    def __init__(
        self, api_client: typing.Optional[kubernetes.client.ApiClient] = ...
    ) -> None: ...
    def get_api_resources(self) -> kubernetes.client.V1APIResourceList: ...
    def list_csi_storage_capacity_for_all_namespaces(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...
    ) -> kubernetes.client.V1alpha1CSIStorageCapacityList: ...
    def list_namespaced_csi_storage_capacity(
        self,
        namespace: str,
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
    ) -> kubernetes.client.V1alpha1CSIStorageCapacityList: ...
    def create_namespaced_csi_storage_capacity(
        self,
        namespace: str,
        body: kubernetes.client.V1alpha1CSIStorageCapacity,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> kubernetes.client.V1alpha1CSIStorageCapacity: ...
    def delete_collection_namespaced_csi_storage_capacity(
        self,
        namespace: str,
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
    def read_namespaced_csi_storage_capacity(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes.client.V1alpha1CSIStorageCapacity: ...
    def replace_namespaced_csi_storage_capacity(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1alpha1CSIStorageCapacity,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> kubernetes.client.V1alpha1CSIStorageCapacity: ...
    def delete_namespaced_csi_storage_capacity(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...
    ) -> kubernetes.client.V1Status: ...
    def patch_namespaced_csi_storage_capacity(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> kubernetes.client.V1alpha1CSIStorageCapacity: ...
    def list_volume_attachment(
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
    ) -> kubernetes.client.V1alpha1VolumeAttachmentList: ...
    def create_volume_attachment(
        self,
        body: kubernetes.client.V1alpha1VolumeAttachment,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> kubernetes.client.V1alpha1VolumeAttachment: ...
    def delete_collection_volume_attachment(
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
    def read_volume_attachment(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes.client.V1alpha1VolumeAttachment: ...
    def replace_volume_attachment(
        self,
        name: str,
        body: kubernetes.client.V1alpha1VolumeAttachment,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...
    ) -> kubernetes.client.V1alpha1VolumeAttachment: ...
    def delete_volume_attachment(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...
    ) -> kubernetes.client.V1alpha1VolumeAttachment: ...
    def patch_volume_attachment(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...
    ) -> kubernetes.client.V1alpha1VolumeAttachment: ...
