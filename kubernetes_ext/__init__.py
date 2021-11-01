import typing

import kubernetes.client


class CoreV1ComponentStatusManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ComponentStatusList:
        return self.client.list_component_status(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1ComponentStatus:
        return self.client.read_component_status(name=name, pretty=pretty)


class CoreV1ConfigMapForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ConfigMapList:
        return self.client.list_config_map_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class CoreV1EndpointsForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1EndpointsList:
        return self.client.list_endpoints_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class CoreV1EventForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.CoreV1EventList:
        return self.client.list_event_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class CoreV1LimitRangeForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1LimitRangeList:
        return self.client.list_limit_range_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class CoreV1NamespaceManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1NamespaceList:
        return self.client.list_namespace(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1Namespace,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Namespace:
        return self.client.create_namespace(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Namespace:
        return self.client.read_namespace(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1Namespace,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Namespace:
        return self.client.replace_namespace(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespace(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Namespace:
        return self.client.patch_namespace(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1NamespacedBindingManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1Binding,
        *,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1Binding:
        return self.client.create_namespaced_binding(
            namespace=namespace,
            body=body,
            dry_run=dry_run,
            field_manager=field_manager,
            pretty=pretty,
        )


class CoreV1NamespacedConfigMapManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ConfigMapList:
        return self.client.list_namespaced_config_map(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1ConfigMap,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ConfigMap:
        return self.client.create_namespaced_config_map(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ConfigMap:
        return self.client.read_namespaced_config_map(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1ConfigMap,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ConfigMap:
        return self.client.replace_namespaced_config_map(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_config_map(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ConfigMap:
        return self.client.patch_namespaced_config_map(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1CollectionNamespacedConfigMapManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_config_map(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CoreV1NamespacedEndpointsManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1EndpointsList:
        return self.client.list_namespaced_endpoints(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1Endpoints,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Endpoints:
        return self.client.create_namespaced_endpoints(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Endpoints:
        return self.client.read_namespaced_endpoints(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Endpoints,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Endpoints:
        return self.client.replace_namespaced_endpoints(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_endpoints(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Endpoints:
        return self.client.patch_namespaced_endpoints(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1CollectionNamespacedEndpointsManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_endpoints(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CoreV1NamespacedEventManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.CoreV1EventList:
        return self.client.list_namespaced_event(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.CoreV1Event,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.CoreV1Event:
        return self.client.create_namespaced_event(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.CoreV1Event:
        return self.client.read_namespaced_event(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.CoreV1Event,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.CoreV1Event:
        return self.client.replace_namespaced_event(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_event(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.CoreV1Event:
        return self.client.patch_namespaced_event(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1CollectionNamespacedEventManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_event(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CoreV1NamespacedLimitRangeManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1LimitRangeList:
        return self.client.list_namespaced_limit_range(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1LimitRange,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1LimitRange:
        return self.client.create_namespaced_limit_range(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1LimitRange:
        return self.client.read_namespaced_limit_range(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1LimitRange,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1LimitRange:
        return self.client.replace_namespaced_limit_range(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_limit_range(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1LimitRange:
        return self.client.patch_namespaced_limit_range(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1CollectionNamespacedLimitRangeManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_limit_range(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CoreV1NamespacedPersistentVolumeClaimManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PersistentVolumeClaimList:
        return self.client.list_namespaced_persistent_volume_claim(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1PersistentVolumeClaim,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1PersistentVolumeClaim:
        return self.client.create_namespaced_persistent_volume_claim(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PersistentVolumeClaim:
        return self.client.read_namespaced_persistent_volume_claim(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1PersistentVolumeClaim,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1PersistentVolumeClaim:
        return self.client.replace_namespaced_persistent_volume_claim(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1PersistentVolumeClaim:
        return self.client.delete_namespaced_persistent_volume_claim(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PersistentVolumeClaim:
        return self.client.patch_namespaced_persistent_volume_claim(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1CollectionNamespacedPersistentVolumeClaimManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_persistent_volume_claim(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CoreV1NamespacedPersistentVolumeClaimStatusManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1PersistentVolumeClaim:
        return self.client.read_namespaced_persistent_volume_claim_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1PersistentVolumeClaim,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1PersistentVolumeClaim:
        return self.client.replace_namespaced_persistent_volume_claim_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PersistentVolumeClaim:
        return self.client.patch_namespaced_persistent_volume_claim_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1NamespacedPodManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PodList:
        return self.client.list_namespaced_pod(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1Pod,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Pod:
        return self.client.create_namespaced_pod(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Pod:
        return self.client.read_namespaced_pod(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Pod,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Pod:
        return self.client.replace_namespaced_pod(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Pod:
        return self.client.delete_namespaced_pod(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Pod:
        return self.client.patch_namespaced_pod(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1CollectionNamespacedPodManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_pod(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CoreV1GetNamespacedPodAttachManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        *,
        container: typing.Optional[str] = None,
        stderr: typing.Optional[bool] = None,
        stdin: typing.Optional[bool] = None,
        stdout: typing.Optional[bool] = None,
        tty: typing.Optional[bool] = None
    ) -> str:
        return self.client.connect_get_namespaced_pod_attach(
            name=name,
            namespace=namespace,
            container=container,
            stderr=stderr,
            stdin=stdin,
            stdout=stdout,
            tty=tty,
        )


class CoreV1PostNamespacedPodAttachManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        *,
        container: typing.Optional[str] = None,
        stderr: typing.Optional[bool] = None,
        stdin: typing.Optional[bool] = None,
        stdout: typing.Optional[bool] = None,
        tty: typing.Optional[bool] = None
    ) -> str:
        return self.client.connect_post_namespaced_pod_attach(
            name=name,
            namespace=namespace,
            container=container,
            stderr=stderr,
            stdin=stdin,
            stdout=stdout,
            tty=tty,
        )


class CoreV1NamespacedPodBindingManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def create(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Binding,
        *,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1Binding:
        return self.client.create_namespaced_pod_binding(
            name=name,
            namespace=namespace,
            body=body,
            dry_run=dry_run,
            field_manager=field_manager,
            pretty=pretty,
        )


class CoreV1NamespacedPodEvictionManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def create(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1beta1Eviction,
        *,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1Eviction:
        return self.client.create_namespaced_pod_eviction(
            name=name,
            namespace=namespace,
            body=body,
            dry_run=dry_run,
            field_manager=field_manager,
            pretty=pretty,
        )


class CoreV1GetNamespacedPodExecManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        *,
        command: typing.Optional[str] = None,
        container: typing.Optional[str] = None,
        stderr: typing.Optional[bool] = None,
        stdin: typing.Optional[bool] = None,
        stdout: typing.Optional[bool] = None,
        tty: typing.Optional[bool] = None
    ) -> str:
        return self.client.connect_get_namespaced_pod_exec(
            name=name,
            namespace=namespace,
            command=command,
            container=container,
            stderr=stderr,
            stdin=stdin,
            stdout=stdout,
            tty=tty,
        )


class CoreV1PostNamespacedPodExecManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        *,
        command: typing.Optional[str] = None,
        container: typing.Optional[str] = None,
        stderr: typing.Optional[bool] = None,
        stdin: typing.Optional[bool] = None,
        stdout: typing.Optional[bool] = None,
        tty: typing.Optional[bool] = None
    ) -> str:
        return self.client.connect_post_namespaced_pod_exec(
            name=name,
            namespace=namespace,
            command=command,
            container=container,
            stderr=stderr,
            stdin=stdin,
            stdout=stdout,
            tty=tty,
        )


class CoreV1NamespacedPodLogManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def read(
        self,
        name: str,
        namespace: str,
        *,
        container: typing.Optional[str] = None,
        follow: typing.Optional[bool] = None,
        insecure_skip_tls_verify_backend: typing.Optional[bool] = None,
        limit_bytes: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        previous: typing.Optional[bool] = None,
        since_seconds: typing.Optional[int] = None,
        tail_lines: typing.Optional[int] = None,
        timestamps: typing.Optional[bool] = None
    ) -> str:
        return self.client.read_namespaced_pod_log(
            name=name,
            namespace=namespace,
            container=container,
            follow=follow,
            insecure_skip_tls_verify_backend=insecure_skip_tls_verify_backend,
            limit_bytes=limit_bytes,
            pretty=pretty,
            previous=previous,
            since_seconds=since_seconds,
            tail_lines=tail_lines,
            timestamps=timestamps,
        )


class CoreV1GetNamespacedPodPortforwardManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, ports: typing.Optional[int] = None
    ) -> str:
        return self.client.connect_get_namespaced_pod_portforward(
            name=name, namespace=namespace, ports=ports
        )


class CoreV1PostNamespacedPodPortforwardManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, ports: typing.Optional[int] = None
    ) -> str:
        return self.client.connect_post_namespaced_pod_portforward(
            name=name, namespace=namespace, ports=ports
        )


class CoreV1GetNamespacedPodProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, path: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_get_namespaced_pod_proxy(
            name=name, namespace=namespace, path=path
        )


class CoreV1PutNamespacedPodProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, path: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_put_namespaced_pod_proxy(
            name=name, namespace=namespace, path=path
        )


class CoreV1PostNamespacedPodProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, path: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_post_namespaced_pod_proxy(
            name=name, namespace=namespace, path=path
        )


class CoreV1DeleteNamespacedPodProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, path: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_delete_namespaced_pod_proxy(
            name=name, namespace=namespace, path=path
        )


class CoreV1OptionsNamespacedPodProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, path: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_options_namespaced_pod_proxy(
            name=name, namespace=namespace, path=path
        )


class CoreV1HeadNamespacedPodProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, path: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_head_namespaced_pod_proxy(
            name=name, namespace=namespace, path=path
        )


class CoreV1PatchNamespacedPodProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, path: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_patch_namespaced_pod_proxy(
            name=name, namespace=namespace, path=path
        )


class CoreV1GetNamespacedPodProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        path: str,
        *,
        path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_get_namespaced_pod_proxy_with_path(
            name=name, namespace=namespace, path=path, path2=path2
        )


class CoreV1PutNamespacedPodProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        path: str,
        *,
        path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_put_namespaced_pod_proxy_with_path(
            name=name, namespace=namespace, path=path, path2=path2
        )


class CoreV1PostNamespacedPodProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        path: str,
        *,
        path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_post_namespaced_pod_proxy_with_path(
            name=name, namespace=namespace, path=path, path2=path2
        )


class CoreV1DeleteNamespacedPodProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        path: str,
        *,
        path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_delete_namespaced_pod_proxy_with_path(
            name=name, namespace=namespace, path=path, path2=path2
        )


class CoreV1OptionsNamespacedPodProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        path: str,
        *,
        path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_options_namespaced_pod_proxy_with_path(
            name=name, namespace=namespace, path=path, path2=path2
        )


class CoreV1HeadNamespacedPodProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        path: str,
        *,
        path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_head_namespaced_pod_proxy_with_path(
            name=name, namespace=namespace, path=path, path2=path2
        )


class CoreV1PatchNamespacedPodProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        path: str,
        *,
        path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_patch_namespaced_pod_proxy_with_path(
            name=name, namespace=namespace, path=path, path2=path2
        )


class CoreV1NamespacedPodStatusManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1Pod:
        return self.client.read_namespaced_pod_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Pod,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Pod:
        return self.client.replace_namespaced_pod_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Pod:
        return self.client.patch_namespaced_pod_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1NamespacedPodTemplateManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PodTemplateList:
        return self.client.list_namespaced_pod_template(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1PodTemplate,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1PodTemplate:
        return self.client.create_namespaced_pod_template(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PodTemplate:
        return self.client.read_namespaced_pod_template(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1PodTemplate,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1PodTemplate:
        return self.client.replace_namespaced_pod_template(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1PodTemplate:
        return self.client.delete_namespaced_pod_template(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PodTemplate:
        return self.client.patch_namespaced_pod_template(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1CollectionNamespacedPodTemplateManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_pod_template(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CoreV1NamespacedReplicationControllerManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ReplicationControllerList:
        return self.client.list_namespaced_replication_controller(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1ReplicationController,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ReplicationController:
        return self.client.create_namespaced_replication_controller(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ReplicationController:
        return self.client.read_namespaced_replication_controller(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1ReplicationController,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ReplicationController:
        return self.client.replace_namespaced_replication_controller(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_replication_controller(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ReplicationController:
        return self.client.patch_namespaced_replication_controller(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1CollectionNamespacedReplicationControllerManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_replication_controller(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CoreV1NamespacedReplicationControllerScaleManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1Scale:
        return self.client.read_namespaced_replication_controller_scale(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Scale,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Scale:
        return self.client.replace_namespaced_replication_controller_scale(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Scale:
        return self.client.patch_namespaced_replication_controller_scale(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1NamespacedReplicationControllerStatusManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1ReplicationController:
        return self.client.read_namespaced_replication_controller_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1ReplicationController,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ReplicationController:
        return self.client.replace_namespaced_replication_controller_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ReplicationController:
        return self.client.patch_namespaced_replication_controller_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1NamespacedResourceQuotaManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ResourceQuotaList:
        return self.client.list_namespaced_resource_quota(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1ResourceQuota,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ResourceQuota:
        return self.client.create_namespaced_resource_quota(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ResourceQuota:
        return self.client.read_namespaced_resource_quota(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1ResourceQuota,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ResourceQuota:
        return self.client.replace_namespaced_resource_quota(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1ResourceQuota:
        return self.client.delete_namespaced_resource_quota(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ResourceQuota:
        return self.client.patch_namespaced_resource_quota(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1CollectionNamespacedResourceQuotaManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_resource_quota(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CoreV1NamespacedResourceQuotaStatusManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1ResourceQuota:
        return self.client.read_namespaced_resource_quota_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1ResourceQuota,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ResourceQuota:
        return self.client.replace_namespaced_resource_quota_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ResourceQuota:
        return self.client.patch_namespaced_resource_quota_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1NamespacedSecretManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1SecretList:
        return self.client.list_namespaced_secret(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1Secret,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Secret:
        return self.client.create_namespaced_secret(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Secret:
        return self.client.read_namespaced_secret(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Secret,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Secret:
        return self.client.replace_namespaced_secret(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_secret(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Secret:
        return self.client.patch_namespaced_secret(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1CollectionNamespacedSecretManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_secret(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CoreV1NamespacedServiceAccountManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ServiceAccountList:
        return self.client.list_namespaced_service_account(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1ServiceAccount,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ServiceAccount:
        return self.client.create_namespaced_service_account(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ServiceAccount:
        return self.client.read_namespaced_service_account(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1ServiceAccount,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ServiceAccount:
        return self.client.replace_namespaced_service_account(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1ServiceAccount:
        return self.client.delete_namespaced_service_account(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ServiceAccount:
        return self.client.patch_namespaced_service_account(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1CollectionNamespacedServiceAccountManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_service_account(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CoreV1NamespacedServiceAccountTokenManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def create(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1TokenRequest,
        *,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1TokenRequest:
        return self.client.create_namespaced_service_account_token(
            name=name,
            namespace=namespace,
            body=body,
            dry_run=dry_run,
            field_manager=field_manager,
            pretty=pretty,
        )


class CoreV1NamespacedServiceManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ServiceList:
        return self.client.list_namespaced_service(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1Service,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Service:
        return self.client.create_namespaced_service(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Service:
        return self.client.read_namespaced_service(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Service,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Service:
        return self.client.replace_namespaced_service(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_service(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Service:
        return self.client.patch_namespaced_service(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1GetNamespacedServiceProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, path: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_get_namespaced_service_proxy(
            name=name, namespace=namespace, path=path
        )


class CoreV1PutNamespacedServiceProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, path: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_put_namespaced_service_proxy(
            name=name, namespace=namespace, path=path
        )


class CoreV1PostNamespacedServiceProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, path: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_post_namespaced_service_proxy(
            name=name, namespace=namespace, path=path
        )


class CoreV1DeleteNamespacedServiceProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, path: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_delete_namespaced_service_proxy(
            name=name, namespace=namespace, path=path
        )


class CoreV1OptionsNamespacedServiceProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, path: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_options_namespaced_service_proxy(
            name=name, namespace=namespace, path=path
        )


class CoreV1HeadNamespacedServiceProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, path: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_head_namespaced_service_proxy(
            name=name, namespace=namespace, path=path
        )


class CoreV1PatchNamespacedServiceProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, namespace: str, *, path: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_patch_namespaced_service_proxy(
            name=name, namespace=namespace, path=path
        )


class CoreV1GetNamespacedServiceProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        path: str,
        *,
        path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_get_namespaced_service_proxy_with_path(
            name=name, namespace=namespace, path=path, path2=path2
        )


class CoreV1PutNamespacedServiceProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        path: str,
        *,
        path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_put_namespaced_service_proxy_with_path(
            name=name, namespace=namespace, path=path, path2=path2
        )


class CoreV1PostNamespacedServiceProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        path: str,
        *,
        path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_post_namespaced_service_proxy_with_path(
            name=name, namespace=namespace, path=path, path2=path2
        )


class CoreV1DeleteNamespacedServiceProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        path: str,
        *,
        path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_delete_namespaced_service_proxy_with_path(
            name=name, namespace=namespace, path=path, path2=path2
        )


class CoreV1OptionsNamespacedServiceProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        path: str,
        *,
        path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_options_namespaced_service_proxy_with_path(
            name=name, namespace=namespace, path=path, path2=path2
        )


class CoreV1HeadNamespacedServiceProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        path: str,
        *,
        path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_head_namespaced_service_proxy_with_path(
            name=name, namespace=namespace, path=path, path2=path2
        )


class CoreV1PatchNamespacedServiceProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self,
        name: str,
        namespace: str,
        path: str,
        *,
        path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_patch_namespaced_service_proxy_with_path(
            name=name, namespace=namespace, path=path, path2=path2
        )


class CoreV1NamespacedServiceStatusManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1Service:
        return self.client.read_namespaced_service_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Service,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Service:
        return self.client.replace_namespaced_service_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Service:
        return self.client.patch_namespaced_service_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1NamespaceFinalizeManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1Namespace,
        *,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1Namespace:
        return self.client.replace_namespace_finalize(
            name=name,
            body=body,
            dry_run=dry_run,
            field_manager=field_manager,
            pretty=pretty,
        )


class CoreV1NamespaceStatusManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1Namespace:
        return self.client.read_namespace_status(name=name, pretty=pretty)

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1Namespace,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Namespace:
        return self.client.replace_namespace_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Namespace:
        return self.client.patch_namespace_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1NodeManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1NodeList:
        return self.client.list_node(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1Node,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Node:
        return self.client.create_node(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Node:
        return self.client.read_node(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1Node,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Node:
        return self.client.replace_node(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_node(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Node:
        return self.client.patch_node(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1CollectionNodeManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_node(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CoreV1GetNodeProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(self, name: str, *, path: typing.Optional[str] = None) -> str:
        return self.client.connect_get_node_proxy(name=name, path=path)


class CoreV1PutNodeProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(self, name: str, *, path: typing.Optional[str] = None) -> str:
        return self.client.connect_put_node_proxy(name=name, path=path)


class CoreV1PostNodeProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(self, name: str, *, path: typing.Optional[str] = None) -> str:
        return self.client.connect_post_node_proxy(name=name, path=path)


class CoreV1DeleteNodeProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(self, name: str, *, path: typing.Optional[str] = None) -> str:
        return self.client.connect_delete_node_proxy(name=name, path=path)


class CoreV1OptionsNodeProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(self, name: str, *, path: typing.Optional[str] = None) -> str:
        return self.client.connect_options_node_proxy(name=name, path=path)


class CoreV1HeadNodeProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(self, name: str, *, path: typing.Optional[str] = None) -> str:
        return self.client.connect_head_node_proxy(name=name, path=path)


class CoreV1PatchNodeProxyManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(self, name: str, *, path: typing.Optional[str] = None) -> str:
        return self.client.connect_patch_node_proxy(name=name, path=path)


class CoreV1GetNodeProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, path: str, *, path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_get_node_proxy_with_path(
            name=name, path=path, path2=path2
        )


class CoreV1PutNodeProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, path: str, *, path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_put_node_proxy_with_path(
            name=name, path=path, path2=path2
        )


class CoreV1PostNodeProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, path: str, *, path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_post_node_proxy_with_path(
            name=name, path=path, path2=path2
        )


class CoreV1DeleteNodeProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, path: str, *, path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_delete_node_proxy_with_path(
            name=name, path=path, path2=path2
        )


class CoreV1OptionsNodeProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, path: str, *, path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_options_node_proxy_with_path(
            name=name, path=path, path2=path2
        )


class CoreV1HeadNodeProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, path: str, *, path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_head_node_proxy_with_path(
            name=name, path=path, path2=path2
        )


class CoreV1PatchNodeProxyWithPathManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def connect(
        self, name: str, path: str, *, path2: typing.Optional[str] = None
    ) -> str:
        return self.client.connect_patch_node_proxy_with_path(
            name=name, path=path, path2=path2
        )


class CoreV1NodeStatusManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1Node:
        return self.client.read_node_status(name=name, pretty=pretty)

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1Node,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Node:
        return self.client.replace_node_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Node:
        return self.client.patch_node_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1PersistentVolumeClaimForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PersistentVolumeClaimList:
        return self.client.list_persistent_volume_claim_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class CoreV1PersistentVolumeManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PersistentVolumeList:
        return self.client.list_persistent_volume(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1PersistentVolume,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1PersistentVolume:
        return self.client.create_persistent_volume(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PersistentVolume:
        return self.client.read_persistent_volume(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1PersistentVolume,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1PersistentVolume:
        return self.client.replace_persistent_volume(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1PersistentVolume:
        return self.client.delete_persistent_volume(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PersistentVolume:
        return self.client.patch_persistent_volume(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1CollectionPersistentVolumeManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_persistent_volume(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CoreV1PersistentVolumeStatusManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1PersistentVolume:
        return self.client.read_persistent_volume_status(name=name, pretty=pretty)

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1PersistentVolume,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1PersistentVolume:
        return self.client.replace_persistent_volume_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PersistentVolume:
        return self.client.patch_persistent_volume_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoreV1PodForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PodList:
        return self.client.list_pod_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class CoreV1PodTemplateForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PodTemplateList:
        return self.client.list_pod_template_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class CoreV1ReplicationControllerForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ReplicationControllerList:
        return self.client.list_replication_controller_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class CoreV1ResourceQuotaForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ResourceQuotaList:
        return self.client.list_resource_quota_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class CoreV1SecretForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1SecretList:
        return self.client.list_secret_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class CoreV1ServiceAccountForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ServiceAccountList:
        return self.client.list_service_account_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class CoreV1ServiceForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.CoreV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ServiceList:
        return self.client.list_service_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class AdmissionregistrationV1MutatingWebhookConfigurationManager:
    def __init__(self, client: kubernetes.client.AdmissionregistrationV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1MutatingWebhookConfigurationList:
        return self.client.list_mutating_webhook_configuration(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1MutatingWebhookConfiguration,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1MutatingWebhookConfiguration:
        return self.client.create_mutating_webhook_configuration(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1MutatingWebhookConfiguration:
        return self.client.read_mutating_webhook_configuration(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1MutatingWebhookConfiguration,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1MutatingWebhookConfiguration:
        return self.client.replace_mutating_webhook_configuration(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_mutating_webhook_configuration(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1MutatingWebhookConfiguration:
        return self.client.patch_mutating_webhook_configuration(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AdmissionregistrationV1CollectionMutatingWebhookConfigurationManager:
    def __init__(self, client: kubernetes.client.AdmissionregistrationV1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_mutating_webhook_configuration(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class AdmissionregistrationV1ValidatingWebhookConfigurationManager:
    def __init__(self, client: kubernetes.client.AdmissionregistrationV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ValidatingWebhookConfigurationList:
        return self.client.list_validating_webhook_configuration(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1ValidatingWebhookConfiguration,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ValidatingWebhookConfiguration:
        return self.client.create_validating_webhook_configuration(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ValidatingWebhookConfiguration:
        return self.client.read_validating_webhook_configuration(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1ValidatingWebhookConfiguration,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ValidatingWebhookConfiguration:
        return self.client.replace_validating_webhook_configuration(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_validating_webhook_configuration(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ValidatingWebhookConfiguration:
        return self.client.patch_validating_webhook_configuration(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AdmissionregistrationV1CollectionValidatingWebhookConfigurationManager:
    def __init__(self, client: kubernetes.client.AdmissionregistrationV1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_validating_webhook_configuration(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class AdmissionregistrationV1beta1MutatingWebhookConfigurationManager:
    def __init__(
        self, client: kubernetes.client.AdmissionregistrationV1beta1Api
    ) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1MutatingWebhookConfigurationList:
        return self.client.list_mutating_webhook_configuration(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1beta1MutatingWebhookConfiguration,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1MutatingWebhookConfiguration:
        return self.client.create_mutating_webhook_configuration(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1MutatingWebhookConfiguration:
        return self.client.read_mutating_webhook_configuration(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1MutatingWebhookConfiguration,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1MutatingWebhookConfiguration:
        return self.client.replace_mutating_webhook_configuration(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_mutating_webhook_configuration(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1MutatingWebhookConfiguration:
        return self.client.patch_mutating_webhook_configuration(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AdmissionregistrationV1beta1CollectionMutatingWebhookConfigurationManager:
    def __init__(
        self, client: kubernetes.client.AdmissionregistrationV1beta1Api
    ) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_mutating_webhook_configuration(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class AdmissionregistrationV1beta1ValidatingWebhookConfigurationManager:
    def __init__(
        self, client: kubernetes.client.AdmissionregistrationV1beta1Api
    ) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1ValidatingWebhookConfigurationList:
        return self.client.list_validating_webhook_configuration(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1beta1ValidatingWebhookConfiguration,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1ValidatingWebhookConfiguration:
        return self.client.create_validating_webhook_configuration(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1ValidatingWebhookConfiguration:
        return self.client.read_validating_webhook_configuration(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1ValidatingWebhookConfiguration,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1ValidatingWebhookConfiguration:
        return self.client.replace_validating_webhook_configuration(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_validating_webhook_configuration(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1ValidatingWebhookConfiguration:
        return self.client.patch_validating_webhook_configuration(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AdmissionregistrationV1beta1CollectionValidatingWebhookConfigurationManager:
    def __init__(
        self, client: kubernetes.client.AdmissionregistrationV1beta1Api
    ) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_validating_webhook_configuration(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class ApiextensionsV1CustomResourceDefinitionManager:
    def __init__(self, client: kubernetes.client.ApiextensionsV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1CustomResourceDefinitionList:
        return self.client.list_custom_resource_definition(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1CustomResourceDefinition,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1CustomResourceDefinition:
        return self.client.create_custom_resource_definition(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1CustomResourceDefinition:
        return self.client.read_custom_resource_definition(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1CustomResourceDefinition,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1CustomResourceDefinition:
        return self.client.replace_custom_resource_definition(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_custom_resource_definition(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1CustomResourceDefinition:
        return self.client.patch_custom_resource_definition(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class ApiextensionsV1CollectionCustomResourceDefinitionManager:
    def __init__(self, client: kubernetes.client.ApiextensionsV1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_custom_resource_definition(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class ApiextensionsV1CustomResourceDefinitionStatusManager:
    def __init__(self, client: kubernetes.client.ApiextensionsV1Api) -> None:
        self.client = client

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1CustomResourceDefinition:
        return self.client.read_custom_resource_definition_status(
            name=name, pretty=pretty
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1CustomResourceDefinition,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1CustomResourceDefinition:
        return self.client.replace_custom_resource_definition_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1CustomResourceDefinition:
        return self.client.patch_custom_resource_definition_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class ApiextensionsV1beta1CustomResourceDefinitionManager:
    def __init__(self, client: kubernetes.client.ApiextensionsV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CustomResourceDefinitionList:
        return self.client.list_custom_resource_definition(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1beta1CustomResourceDefinition,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CustomResourceDefinition:
        return self.client.create_custom_resource_definition(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CustomResourceDefinition:
        return self.client.read_custom_resource_definition(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1CustomResourceDefinition,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CustomResourceDefinition:
        return self.client.replace_custom_resource_definition(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_custom_resource_definition(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CustomResourceDefinition:
        return self.client.patch_custom_resource_definition(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class ApiextensionsV1beta1CollectionCustomResourceDefinitionManager:
    def __init__(self, client: kubernetes.client.ApiextensionsV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_custom_resource_definition(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class ApiextensionsV1beta1CustomResourceDefinitionStatusManager:
    def __init__(self, client: kubernetes.client.ApiextensionsV1beta1Api) -> None:
        self.client = client

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CustomResourceDefinition:
        return self.client.read_custom_resource_definition_status(
            name=name, pretty=pretty
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1CustomResourceDefinition,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CustomResourceDefinition:
        return self.client.replace_custom_resource_definition_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CustomResourceDefinition:
        return self.client.patch_custom_resource_definition_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class ApiregistrationV1ApiServiceManager:
    def __init__(self, client: kubernetes.client.ApiregistrationV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1APIServiceList:
        return self.client.list_api_service(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1APIService,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1APIService:
        return self.client.create_api_service(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1APIService:
        return self.client.read_api_service(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1APIService,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1APIService:
        return self.client.replace_api_service(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_api_service(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1APIService:
        return self.client.patch_api_service(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class ApiregistrationV1CollectionApiServiceManager:
    def __init__(self, client: kubernetes.client.ApiregistrationV1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_api_service(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class ApiregistrationV1ApiServiceStatusManager:
    def __init__(self, client: kubernetes.client.ApiregistrationV1Api) -> None:
        self.client = client

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1APIService:
        return self.client.read_api_service_status(name=name, pretty=pretty)

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1APIService,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1APIService:
        return self.client.replace_api_service_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1APIService:
        return self.client.patch_api_service_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class ApiregistrationV1beta1ApiServiceManager:
    def __init__(self, client: kubernetes.client.ApiregistrationV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1APIServiceList:
        return self.client.list_api_service(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1beta1APIService,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1APIService:
        return self.client.create_api_service(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1APIService:
        return self.client.read_api_service(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1APIService,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1APIService:
        return self.client.replace_api_service(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_api_service(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1APIService:
        return self.client.patch_api_service(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class ApiregistrationV1beta1CollectionApiServiceManager:
    def __init__(self, client: kubernetes.client.ApiregistrationV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_api_service(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class ApiregistrationV1beta1ApiServiceStatusManager:
    def __init__(self, client: kubernetes.client.ApiregistrationV1beta1Api) -> None:
        self.client = client

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1APIService:
        return self.client.read_api_service_status(name=name, pretty=pretty)

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1APIService,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1APIService:
        return self.client.replace_api_service_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1APIService:
        return self.client.patch_api_service_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AppsV1ControllerRevisionForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ControllerRevisionList:
        return self.client.list_controller_revision_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class AppsV1DaemonSetForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1DaemonSetList:
        return self.client.list_daemon_set_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class AppsV1DeploymentForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1DeploymentList:
        return self.client.list_deployment_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class AppsV1NamespacedControllerRevisionManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ControllerRevisionList:
        return self.client.list_namespaced_controller_revision(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1ControllerRevision,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ControllerRevision:
        return self.client.create_namespaced_controller_revision(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ControllerRevision:
        return self.client.read_namespaced_controller_revision(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1ControllerRevision,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ControllerRevision:
        return self.client.replace_namespaced_controller_revision(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_controller_revision(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ControllerRevision:
        return self.client.patch_namespaced_controller_revision(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AppsV1CollectionNamespacedControllerRevisionManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_controller_revision(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class AppsV1NamespacedDaemonSetManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1DaemonSetList:
        return self.client.list_namespaced_daemon_set(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1DaemonSet,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1DaemonSet:
        return self.client.create_namespaced_daemon_set(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1DaemonSet:
        return self.client.read_namespaced_daemon_set(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1DaemonSet,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1DaemonSet:
        return self.client.replace_namespaced_daemon_set(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_daemon_set(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1DaemonSet:
        return self.client.patch_namespaced_daemon_set(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AppsV1CollectionNamespacedDaemonSetManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_daemon_set(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class AppsV1NamespacedDaemonSetStatusManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1DaemonSet:
        return self.client.read_namespaced_daemon_set_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1DaemonSet,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1DaemonSet:
        return self.client.replace_namespaced_daemon_set_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1DaemonSet:
        return self.client.patch_namespaced_daemon_set_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AppsV1NamespacedDeploymentManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1DeploymentList:
        return self.client.list_namespaced_deployment(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1Deployment,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Deployment:
        return self.client.create_namespaced_deployment(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Deployment:
        return self.client.read_namespaced_deployment(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Deployment,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Deployment:
        return self.client.replace_namespaced_deployment(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_deployment(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Deployment:
        return self.client.patch_namespaced_deployment(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AppsV1CollectionNamespacedDeploymentManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_deployment(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class AppsV1NamespacedDeploymentScaleManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1Scale:
        return self.client.read_namespaced_deployment_scale(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Scale,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Scale:
        return self.client.replace_namespaced_deployment_scale(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Scale:
        return self.client.patch_namespaced_deployment_scale(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AppsV1NamespacedDeploymentStatusManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1Deployment:
        return self.client.read_namespaced_deployment_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Deployment,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Deployment:
        return self.client.replace_namespaced_deployment_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Deployment:
        return self.client.patch_namespaced_deployment_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AppsV1NamespacedReplicaSetManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ReplicaSetList:
        return self.client.list_namespaced_replica_set(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1ReplicaSet,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ReplicaSet:
        return self.client.create_namespaced_replica_set(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ReplicaSet:
        return self.client.read_namespaced_replica_set(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1ReplicaSet,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ReplicaSet:
        return self.client.replace_namespaced_replica_set(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_replica_set(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ReplicaSet:
        return self.client.patch_namespaced_replica_set(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AppsV1CollectionNamespacedReplicaSetManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_replica_set(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class AppsV1NamespacedReplicaSetScaleManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1Scale:
        return self.client.read_namespaced_replica_set_scale(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Scale,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Scale:
        return self.client.replace_namespaced_replica_set_scale(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Scale:
        return self.client.patch_namespaced_replica_set_scale(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AppsV1NamespacedReplicaSetStatusManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1ReplicaSet:
        return self.client.read_namespaced_replica_set_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1ReplicaSet,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ReplicaSet:
        return self.client.replace_namespaced_replica_set_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ReplicaSet:
        return self.client.patch_namespaced_replica_set_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AppsV1NamespacedStatefulSetManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1StatefulSetList:
        return self.client.list_namespaced_stateful_set(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1StatefulSet,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1StatefulSet:
        return self.client.create_namespaced_stateful_set(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1StatefulSet:
        return self.client.read_namespaced_stateful_set(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1StatefulSet,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1StatefulSet:
        return self.client.replace_namespaced_stateful_set(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_stateful_set(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1StatefulSet:
        return self.client.patch_namespaced_stateful_set(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AppsV1CollectionNamespacedStatefulSetManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_stateful_set(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class AppsV1NamespacedStatefulSetScaleManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1Scale:
        return self.client.read_namespaced_stateful_set_scale(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Scale,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Scale:
        return self.client.replace_namespaced_stateful_set_scale(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Scale:
        return self.client.patch_namespaced_stateful_set_scale(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AppsV1NamespacedStatefulSetStatusManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1StatefulSet:
        return self.client.read_namespaced_stateful_set_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1StatefulSet,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1StatefulSet:
        return self.client.replace_namespaced_stateful_set_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1StatefulSet:
        return self.client.patch_namespaced_stateful_set_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AppsV1ReplicaSetForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ReplicaSetList:
        return self.client.list_replica_set_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class AppsV1StatefulSetForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.AppsV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1StatefulSetList:
        return self.client.list_stateful_set_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class AuthenticationV1TokenReviewManager:
    def __init__(self, client: kubernetes.client.AuthenticationV1Api) -> None:
        self.client = client

    def create(
        self,
        body: kubernetes.client.V1TokenReview,
        *,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1TokenReview:
        return self.client.create_token_review(
            body=body, dry_run=dry_run, field_manager=field_manager, pretty=pretty
        )


class AuthenticationV1beta1TokenReviewManager:
    def __init__(self, client: kubernetes.client.AuthenticationV1beta1Api) -> None:
        self.client = client

    def create(
        self,
        body: kubernetes.client.V1beta1TokenReview,
        *,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1TokenReview:
        return self.client.create_token_review(
            body=body, dry_run=dry_run, field_manager=field_manager, pretty=pretty
        )


class AuthorizationV1NamespacedLocalSubjectAccessReviewManager:
    def __init__(self, client: kubernetes.client.AuthorizationV1Api) -> None:
        self.client = client

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1LocalSubjectAccessReview,
        *,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1LocalSubjectAccessReview:
        return self.client.create_namespaced_local_subject_access_review(
            namespace=namespace,
            body=body,
            dry_run=dry_run,
            field_manager=field_manager,
            pretty=pretty,
        )


class AuthorizationV1SelfSubjectAccessReviewManager:
    def __init__(self, client: kubernetes.client.AuthorizationV1Api) -> None:
        self.client = client

    def create(
        self,
        body: kubernetes.client.V1SelfSubjectAccessReview,
        *,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1SelfSubjectAccessReview:
        return self.client.create_self_subject_access_review(
            body=body, dry_run=dry_run, field_manager=field_manager, pretty=pretty
        )


class AuthorizationV1SelfSubjectRulesReviewManager:
    def __init__(self, client: kubernetes.client.AuthorizationV1Api) -> None:
        self.client = client

    def create(
        self,
        body: kubernetes.client.V1SelfSubjectRulesReview,
        *,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1SelfSubjectRulesReview:
        return self.client.create_self_subject_rules_review(
            body=body, dry_run=dry_run, field_manager=field_manager, pretty=pretty
        )


class AuthorizationV1SubjectAccessReviewManager:
    def __init__(self, client: kubernetes.client.AuthorizationV1Api) -> None:
        self.client = client

    def create(
        self,
        body: kubernetes.client.V1SubjectAccessReview,
        *,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1SubjectAccessReview:
        return self.client.create_subject_access_review(
            body=body, dry_run=dry_run, field_manager=field_manager, pretty=pretty
        )


class AuthorizationV1beta1NamespacedLocalSubjectAccessReviewManager:
    def __init__(self, client: kubernetes.client.AuthorizationV1beta1Api) -> None:
        self.client = client

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1beta1LocalSubjectAccessReview,
        *,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1LocalSubjectAccessReview:
        return self.client.create_namespaced_local_subject_access_review(
            namespace=namespace,
            body=body,
            dry_run=dry_run,
            field_manager=field_manager,
            pretty=pretty,
        )


class AuthorizationV1beta1SelfSubjectAccessReviewManager:
    def __init__(self, client: kubernetes.client.AuthorizationV1beta1Api) -> None:
        self.client = client

    def create(
        self,
        body: kubernetes.client.V1beta1SelfSubjectAccessReview,
        *,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1SelfSubjectAccessReview:
        return self.client.create_self_subject_access_review(
            body=body, dry_run=dry_run, field_manager=field_manager, pretty=pretty
        )


class AuthorizationV1beta1SelfSubjectRulesReviewManager:
    def __init__(self, client: kubernetes.client.AuthorizationV1beta1Api) -> None:
        self.client = client

    def create(
        self,
        body: kubernetes.client.V1beta1SelfSubjectRulesReview,
        *,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1SelfSubjectRulesReview:
        return self.client.create_self_subject_rules_review(
            body=body, dry_run=dry_run, field_manager=field_manager, pretty=pretty
        )


class AuthorizationV1beta1SubjectAccessReviewManager:
    def __init__(self, client: kubernetes.client.AuthorizationV1beta1Api) -> None:
        self.client = client

    def create(
        self,
        body: kubernetes.client.V1beta1SubjectAccessReview,
        *,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1SubjectAccessReview:
        return self.client.create_subject_access_review(
            body=body, dry_run=dry_run, field_manager=field_manager, pretty=pretty
        )


class AutoscalingV1HorizontalPodAutoscalerForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.AutoscalingV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1HorizontalPodAutoscalerList:
        return self.client.list_horizontal_pod_autoscaler_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class AutoscalingV1NamespacedHorizontalPodAutoscalerManager:
    def __init__(self, client: kubernetes.client.AutoscalingV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1HorizontalPodAutoscalerList:
        return self.client.list_namespaced_horizontal_pod_autoscaler(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1HorizontalPodAutoscaler,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1HorizontalPodAutoscaler:
        return self.client.create_namespaced_horizontal_pod_autoscaler(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1HorizontalPodAutoscaler:
        return self.client.read_namespaced_horizontal_pod_autoscaler(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1HorizontalPodAutoscaler,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1HorizontalPodAutoscaler:
        return self.client.replace_namespaced_horizontal_pod_autoscaler(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_horizontal_pod_autoscaler(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1HorizontalPodAutoscaler:
        return self.client.patch_namespaced_horizontal_pod_autoscaler(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AutoscalingV1CollectionNamespacedHorizontalPodAutoscalerManager:
    def __init__(self, client: kubernetes.client.AutoscalingV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_horizontal_pod_autoscaler(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class AutoscalingV1NamespacedHorizontalPodAutoscalerStatusManager:
    def __init__(self, client: kubernetes.client.AutoscalingV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1HorizontalPodAutoscaler:
        return self.client.read_namespaced_horizontal_pod_autoscaler_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1HorizontalPodAutoscaler,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1HorizontalPodAutoscaler:
        return self.client.replace_namespaced_horizontal_pod_autoscaler_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1HorizontalPodAutoscaler:
        return self.client.patch_namespaced_horizontal_pod_autoscaler_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AutoscalingV2beta1HorizontalPodAutoscalerForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.AutoscalingV2beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V2beta1HorizontalPodAutoscalerList:
        return self.client.list_horizontal_pod_autoscaler_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class AutoscalingV2beta1NamespacedHorizontalPodAutoscalerManager:
    def __init__(self, client: kubernetes.client.AutoscalingV2beta1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V2beta1HorizontalPodAutoscalerList:
        return self.client.list_namespaced_horizontal_pod_autoscaler(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V2beta1HorizontalPodAutoscaler,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V2beta1HorizontalPodAutoscaler:
        return self.client.create_namespaced_horizontal_pod_autoscaler(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V2beta1HorizontalPodAutoscaler:
        return self.client.read_namespaced_horizontal_pod_autoscaler(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V2beta1HorizontalPodAutoscaler,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V2beta1HorizontalPodAutoscaler:
        return self.client.replace_namespaced_horizontal_pod_autoscaler(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_horizontal_pod_autoscaler(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V2beta1HorizontalPodAutoscaler:
        return self.client.patch_namespaced_horizontal_pod_autoscaler(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AutoscalingV2beta1CollectionNamespacedHorizontalPodAutoscalerManager:
    def __init__(self, client: kubernetes.client.AutoscalingV2beta1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_horizontal_pod_autoscaler(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class AutoscalingV2beta1NamespacedHorizontalPodAutoscalerStatusManager:
    def __init__(self, client: kubernetes.client.AutoscalingV2beta1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V2beta1HorizontalPodAutoscaler:
        return self.client.read_namespaced_horizontal_pod_autoscaler_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V2beta1HorizontalPodAutoscaler,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V2beta1HorizontalPodAutoscaler:
        return self.client.replace_namespaced_horizontal_pod_autoscaler_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V2beta1HorizontalPodAutoscaler:
        return self.client.patch_namespaced_horizontal_pod_autoscaler_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AutoscalingV2beta2HorizontalPodAutoscalerForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.AutoscalingV2beta2Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V2beta2HorizontalPodAutoscalerList:
        return self.client.list_horizontal_pod_autoscaler_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class AutoscalingV2beta2NamespacedHorizontalPodAutoscalerManager:
    def __init__(self, client: kubernetes.client.AutoscalingV2beta2Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V2beta2HorizontalPodAutoscalerList:
        return self.client.list_namespaced_horizontal_pod_autoscaler(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V2beta2HorizontalPodAutoscaler,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V2beta2HorizontalPodAutoscaler:
        return self.client.create_namespaced_horizontal_pod_autoscaler(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V2beta2HorizontalPodAutoscaler:
        return self.client.read_namespaced_horizontal_pod_autoscaler(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V2beta2HorizontalPodAutoscaler,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V2beta2HorizontalPodAutoscaler:
        return self.client.replace_namespaced_horizontal_pod_autoscaler(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_horizontal_pod_autoscaler(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V2beta2HorizontalPodAutoscaler:
        return self.client.patch_namespaced_horizontal_pod_autoscaler(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class AutoscalingV2beta2CollectionNamespacedHorizontalPodAutoscalerManager:
    def __init__(self, client: kubernetes.client.AutoscalingV2beta2Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_horizontal_pod_autoscaler(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class AutoscalingV2beta2NamespacedHorizontalPodAutoscalerStatusManager:
    def __init__(self, client: kubernetes.client.AutoscalingV2beta2Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V2beta2HorizontalPodAutoscaler:
        return self.client.read_namespaced_horizontal_pod_autoscaler_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V2beta2HorizontalPodAutoscaler,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V2beta2HorizontalPodAutoscaler:
        return self.client.replace_namespaced_horizontal_pod_autoscaler_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V2beta2HorizontalPodAutoscaler:
        return self.client.patch_namespaced_horizontal_pod_autoscaler_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class BatchV1JobForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.BatchV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1JobList:
        return self.client.list_job_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class BatchV1NamespacedJobManager:
    def __init__(self, client: kubernetes.client.BatchV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1JobList:
        return self.client.list_namespaced_job(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1Job,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Job:
        return self.client.create_namespaced_job(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Job:
        return self.client.read_namespaced_job(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Job,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Job:
        return self.client.replace_namespaced_job(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_job(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Job:
        return self.client.patch_namespaced_job(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class BatchV1CollectionNamespacedJobManager:
    def __init__(self, client: kubernetes.client.BatchV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_job(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class BatchV1NamespacedJobStatusManager:
    def __init__(self, client: kubernetes.client.BatchV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1Job:
        return self.client.read_namespaced_job_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Job,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Job:
        return self.client.replace_namespaced_job_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Job:
        return self.client.patch_namespaced_job_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class BatchV1beta1CronJobForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.BatchV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CronJobList:
        return self.client.list_cron_job_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class BatchV1beta1NamespacedCronJobManager:
    def __init__(self, client: kubernetes.client.BatchV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CronJobList:
        return self.client.list_namespaced_cron_job(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1beta1CronJob,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CronJob:
        return self.client.create_namespaced_cron_job(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CronJob:
        return self.client.read_namespaced_cron_job(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1beta1CronJob,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CronJob:
        return self.client.replace_namespaced_cron_job(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_cron_job(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CronJob:
        return self.client.patch_namespaced_cron_job(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class BatchV1beta1CollectionNamespacedCronJobManager:
    def __init__(self, client: kubernetes.client.BatchV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_cron_job(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class BatchV1beta1NamespacedCronJobStatusManager:
    def __init__(self, client: kubernetes.client.BatchV1beta1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CronJob:
        return self.client.read_namespaced_cron_job_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1beta1CronJob,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CronJob:
        return self.client.replace_namespaced_cron_job_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CronJob:
        return self.client.patch_namespaced_cron_job_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class BatchV2alpha1CronJobForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.BatchV2alpha1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V2alpha1CronJobList:
        return self.client.list_cron_job_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class BatchV2alpha1NamespacedCronJobManager:
    def __init__(self, client: kubernetes.client.BatchV2alpha1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V2alpha1CronJobList:
        return self.client.list_namespaced_cron_job(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V2alpha1CronJob,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V2alpha1CronJob:
        return self.client.create_namespaced_cron_job(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V2alpha1CronJob:
        return self.client.read_namespaced_cron_job(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V2alpha1CronJob,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V2alpha1CronJob:
        return self.client.replace_namespaced_cron_job(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_cron_job(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V2alpha1CronJob:
        return self.client.patch_namespaced_cron_job(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class BatchV2alpha1CollectionNamespacedCronJobManager:
    def __init__(self, client: kubernetes.client.BatchV2alpha1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_cron_job(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class BatchV2alpha1NamespacedCronJobStatusManager:
    def __init__(self, client: kubernetes.client.BatchV2alpha1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V2alpha1CronJob:
        return self.client.read_namespaced_cron_job_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V2alpha1CronJob,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V2alpha1CronJob:
        return self.client.replace_namespaced_cron_job_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V2alpha1CronJob:
        return self.client.patch_namespaced_cron_job_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CertificatesV1CertificateSigningRequestManager:
    def __init__(self, client: kubernetes.client.CertificatesV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1CertificateSigningRequestList:
        return self.client.list_certificate_signing_request(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1CertificateSigningRequest,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1CertificateSigningRequest:
        return self.client.create_certificate_signing_request(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1CertificateSigningRequest:
        return self.client.read_certificate_signing_request(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1CertificateSigningRequest,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1CertificateSigningRequest:
        return self.client.replace_certificate_signing_request(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_certificate_signing_request(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1CertificateSigningRequest:
        return self.client.patch_certificate_signing_request(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CertificatesV1CollectionCertificateSigningRequestManager:
    def __init__(self, client: kubernetes.client.CertificatesV1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_certificate_signing_request(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CertificatesV1CertificateSigningRequestApprovalManager:
    def __init__(self, client: kubernetes.client.CertificatesV1Api) -> None:
        self.client = client

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1CertificateSigningRequest:
        return self.client.read_certificate_signing_request_approval(
            name=name, pretty=pretty
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1CertificateSigningRequest,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1CertificateSigningRequest:
        return self.client.replace_certificate_signing_request_approval(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1CertificateSigningRequest:
        return self.client.patch_certificate_signing_request_approval(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CertificatesV1CertificateSigningRequestStatusManager:
    def __init__(self, client: kubernetes.client.CertificatesV1Api) -> None:
        self.client = client

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1CertificateSigningRequest:
        return self.client.read_certificate_signing_request_status(
            name=name, pretty=pretty
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1CertificateSigningRequest,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1CertificateSigningRequest:
        return self.client.replace_certificate_signing_request_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1CertificateSigningRequest:
        return self.client.patch_certificate_signing_request_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CertificatesV1beta1CertificateSigningRequestManager:
    def __init__(self, client: kubernetes.client.CertificatesV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CertificateSigningRequestList:
        return self.client.list_certificate_signing_request(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1beta1CertificateSigningRequest,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CertificateSigningRequest:
        return self.client.create_certificate_signing_request(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CertificateSigningRequest:
        return self.client.read_certificate_signing_request(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1CertificateSigningRequest,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CertificateSigningRequest:
        return self.client.replace_certificate_signing_request(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_certificate_signing_request(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CertificateSigningRequest:
        return self.client.patch_certificate_signing_request(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CertificatesV1beta1CollectionCertificateSigningRequestManager:
    def __init__(self, client: kubernetes.client.CertificatesV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_certificate_signing_request(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CertificatesV1beta1CertificateSigningRequestApprovalManager:
    def __init__(self, client: kubernetes.client.CertificatesV1beta1Api) -> None:
        self.client = client

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CertificateSigningRequest:
        return self.client.read_certificate_signing_request_approval(
            name=name, pretty=pretty
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1CertificateSigningRequest,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CertificateSigningRequest:
        return self.client.replace_certificate_signing_request_approval(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CertificateSigningRequest:
        return self.client.patch_certificate_signing_request_approval(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CertificatesV1beta1CertificateSigningRequestStatusManager:
    def __init__(self, client: kubernetes.client.CertificatesV1beta1Api) -> None:
        self.client = client

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CertificateSigningRequest:
        return self.client.read_certificate_signing_request_status(
            name=name, pretty=pretty
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1CertificateSigningRequest,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CertificateSigningRequest:
        return self.client.replace_certificate_signing_request_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CertificateSigningRequest:
        return self.client.patch_certificate_signing_request_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoordinationV1LeaseForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.CoordinationV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1LeaseList:
        return self.client.list_lease_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class CoordinationV1NamespacedLeaseManager:
    def __init__(self, client: kubernetes.client.CoordinationV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1LeaseList:
        return self.client.list_namespaced_lease(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1Lease,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Lease:
        return self.client.create_namespaced_lease(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Lease:
        return self.client.read_namespaced_lease(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Lease,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Lease:
        return self.client.replace_namespaced_lease(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_lease(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Lease:
        return self.client.patch_namespaced_lease(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoordinationV1CollectionNamespacedLeaseManager:
    def __init__(self, client: kubernetes.client.CoordinationV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_lease(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class CoordinationV1beta1LeaseForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.CoordinationV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1LeaseList:
        return self.client.list_lease_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class CoordinationV1beta1NamespacedLeaseManager:
    def __init__(self, client: kubernetes.client.CoordinationV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1LeaseList:
        return self.client.list_namespaced_lease(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1beta1Lease,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1Lease:
        return self.client.create_namespaced_lease(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1Lease:
        return self.client.read_namespaced_lease(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1beta1Lease,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1Lease:
        return self.client.replace_namespaced_lease(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_lease(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1Lease:
        return self.client.patch_namespaced_lease(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class CoordinationV1beta1CollectionNamespacedLeaseManager:
    def __init__(self, client: kubernetes.client.CoordinationV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_lease(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class DiscoveryV1beta1EndpointSliceForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.DiscoveryV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1EndpointSliceList:
        return self.client.list_endpoint_slice_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class DiscoveryV1beta1NamespacedEndpointSliceManager:
    def __init__(self, client: kubernetes.client.DiscoveryV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1EndpointSliceList:
        return self.client.list_namespaced_endpoint_slice(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1beta1EndpointSlice,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1EndpointSlice:
        return self.client.create_namespaced_endpoint_slice(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1EndpointSlice:
        return self.client.read_namespaced_endpoint_slice(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1beta1EndpointSlice,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1EndpointSlice:
        return self.client.replace_namespaced_endpoint_slice(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_endpoint_slice(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1EndpointSlice:
        return self.client.patch_namespaced_endpoint_slice(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class DiscoveryV1beta1CollectionNamespacedEndpointSliceManager:
    def __init__(self, client: kubernetes.client.DiscoveryV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_endpoint_slice(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class EventsV1EventForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.EventsV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.EventsV1EventList:
        return self.client.list_event_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class EventsV1NamespacedEventManager:
    def __init__(self, client: kubernetes.client.EventsV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.EventsV1EventList:
        return self.client.list_namespaced_event(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.EventsV1Event,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.EventsV1Event:
        return self.client.create_namespaced_event(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.EventsV1Event:
        return self.client.read_namespaced_event(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.EventsV1Event,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.EventsV1Event:
        return self.client.replace_namespaced_event(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_event(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.EventsV1Event:
        return self.client.patch_namespaced_event(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class EventsV1CollectionNamespacedEventManager:
    def __init__(self, client: kubernetes.client.EventsV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_event(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class EventsV1beta1EventForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.EventsV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1EventList:
        return self.client.list_event_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class EventsV1beta1NamespacedEventManager:
    def __init__(self, client: kubernetes.client.EventsV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1EventList:
        return self.client.list_namespaced_event(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1beta1Event,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1Event:
        return self.client.create_namespaced_event(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1Event:
        return self.client.read_namespaced_event(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1beta1Event,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1Event:
        return self.client.replace_namespaced_event(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_event(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1Event:
        return self.client.patch_namespaced_event(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class EventsV1beta1CollectionNamespacedEventManager:
    def __init__(self, client: kubernetes.client.EventsV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_event(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class ExtensionsV1beta1IngressForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.ExtensionsV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.ExtensionsV1beta1IngressList:
        return self.client.list_ingress_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class ExtensionsV1beta1NamespacedIngressManager:
    def __init__(self, client: kubernetes.client.ExtensionsV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.ExtensionsV1beta1IngressList:
        return self.client.list_namespaced_ingress(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.ExtensionsV1beta1Ingress,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.ExtensionsV1beta1Ingress:
        return self.client.create_namespaced_ingress(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.ExtensionsV1beta1Ingress:
        return self.client.read_namespaced_ingress(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.ExtensionsV1beta1Ingress,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.ExtensionsV1beta1Ingress:
        return self.client.replace_namespaced_ingress(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_ingress(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.ExtensionsV1beta1Ingress:
        return self.client.patch_namespaced_ingress(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class ExtensionsV1beta1CollectionNamespacedIngressManager:
    def __init__(self, client: kubernetes.client.ExtensionsV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_ingress(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class ExtensionsV1beta1NamespacedIngressStatusManager:
    def __init__(self, client: kubernetes.client.ExtensionsV1beta1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.ExtensionsV1beta1Ingress:
        return self.client.read_namespaced_ingress_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.ExtensionsV1beta1Ingress,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.ExtensionsV1beta1Ingress:
        return self.client.replace_namespaced_ingress_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.ExtensionsV1beta1Ingress:
        return self.client.patch_namespaced_ingress_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class FlowcontrolApiserverV1alpha1FlowSchemaManager:
    def __init__(
        self, client: kubernetes.client.FlowcontrolApiserverV1alpha1Api
    ) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1FlowSchemaList:
        return self.client.list_flow_schema(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1alpha1FlowSchema,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1FlowSchema:
        return self.client.create_flow_schema(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1FlowSchema:
        return self.client.read_flow_schema(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1alpha1FlowSchema,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1FlowSchema:
        return self.client.replace_flow_schema(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_flow_schema(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1FlowSchema:
        return self.client.patch_flow_schema(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class FlowcontrolApiserverV1alpha1CollectionFlowSchemaManager:
    def __init__(
        self, client: kubernetes.client.FlowcontrolApiserverV1alpha1Api
    ) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_flow_schema(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class FlowcontrolApiserverV1alpha1FlowSchemaStatusManager:
    def __init__(
        self, client: kubernetes.client.FlowcontrolApiserverV1alpha1Api
    ) -> None:
        self.client = client

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1FlowSchema:
        return self.client.read_flow_schema_status(name=name, pretty=pretty)

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1alpha1FlowSchema,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1FlowSchema:
        return self.client.replace_flow_schema_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1FlowSchema:
        return self.client.patch_flow_schema_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class FlowcontrolApiserverV1alpha1PriorityLevelConfigurationManager:
    def __init__(
        self, client: kubernetes.client.FlowcontrolApiserverV1alpha1Api
    ) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1PriorityLevelConfigurationList:
        return self.client.list_priority_level_configuration(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1alpha1PriorityLevelConfiguration,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1PriorityLevelConfiguration:
        return self.client.create_priority_level_configuration(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1PriorityLevelConfiguration:
        return self.client.read_priority_level_configuration(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1alpha1PriorityLevelConfiguration,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1PriorityLevelConfiguration:
        return self.client.replace_priority_level_configuration(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_priority_level_configuration(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1PriorityLevelConfiguration:
        return self.client.patch_priority_level_configuration(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class FlowcontrolApiserverV1alpha1CollectionPriorityLevelConfigurationManager:
    def __init__(
        self, client: kubernetes.client.FlowcontrolApiserverV1alpha1Api
    ) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_priority_level_configuration(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class FlowcontrolApiserverV1alpha1PriorityLevelConfigurationStatusManager:
    def __init__(
        self, client: kubernetes.client.FlowcontrolApiserverV1alpha1Api
    ) -> None:
        self.client = client

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1PriorityLevelConfiguration:
        return self.client.read_priority_level_configuration_status(
            name=name, pretty=pretty
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1alpha1PriorityLevelConfiguration,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1PriorityLevelConfiguration:
        return self.client.replace_priority_level_configuration_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1PriorityLevelConfiguration:
        return self.client.patch_priority_level_configuration_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class NetworkingV1IngressClassManager:
    def __init__(self, client: kubernetes.client.NetworkingV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1IngressClassList:
        return self.client.list_ingress_class(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1IngressClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1IngressClass:
        return self.client.create_ingress_class(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1IngressClass:
        return self.client.read_ingress_class(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1IngressClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1IngressClass:
        return self.client.replace_ingress_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_ingress_class(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1IngressClass:
        return self.client.patch_ingress_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class NetworkingV1CollectionIngressClassManager:
    def __init__(self, client: kubernetes.client.NetworkingV1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_ingress_class(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class NetworkingV1IngressForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.NetworkingV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1IngressList:
        return self.client.list_ingress_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class NetworkingV1NamespacedIngressManager:
    def __init__(self, client: kubernetes.client.NetworkingV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1IngressList:
        return self.client.list_namespaced_ingress(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1Ingress,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Ingress:
        return self.client.create_namespaced_ingress(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Ingress:
        return self.client.read_namespaced_ingress(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Ingress,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Ingress:
        return self.client.replace_namespaced_ingress(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_ingress(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Ingress:
        return self.client.patch_namespaced_ingress(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class NetworkingV1CollectionNamespacedIngressManager:
    def __init__(self, client: kubernetes.client.NetworkingV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_ingress(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class NetworkingV1NamespacedIngressStatusManager:
    def __init__(self, client: kubernetes.client.NetworkingV1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1Ingress:
        return self.client.read_namespaced_ingress_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Ingress,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Ingress:
        return self.client.replace_namespaced_ingress_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Ingress:
        return self.client.patch_namespaced_ingress_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class NetworkingV1NamespacedNetworkPolicyManager:
    def __init__(self, client: kubernetes.client.NetworkingV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1NetworkPolicyList:
        return self.client.list_namespaced_network_policy(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1NetworkPolicy,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1NetworkPolicy:
        return self.client.create_namespaced_network_policy(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1NetworkPolicy:
        return self.client.read_namespaced_network_policy(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1NetworkPolicy,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1NetworkPolicy:
        return self.client.replace_namespaced_network_policy(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_network_policy(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1NetworkPolicy:
        return self.client.patch_namespaced_network_policy(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class NetworkingV1CollectionNamespacedNetworkPolicyManager:
    def __init__(self, client: kubernetes.client.NetworkingV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_network_policy(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class NetworkingV1NetworkPolicyForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.NetworkingV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1NetworkPolicyList:
        return self.client.list_network_policy_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class NetworkingV1beta1IngressClassManager:
    def __init__(self, client: kubernetes.client.NetworkingV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1IngressClassList:
        return self.client.list_ingress_class(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1beta1IngressClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1IngressClass:
        return self.client.create_ingress_class(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1IngressClass:
        return self.client.read_ingress_class(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1IngressClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1IngressClass:
        return self.client.replace_ingress_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_ingress_class(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1IngressClass:
        return self.client.patch_ingress_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class NetworkingV1beta1CollectionIngressClassManager:
    def __init__(self, client: kubernetes.client.NetworkingV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_ingress_class(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class NetworkingV1beta1IngressForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.NetworkingV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.NetworkingV1beta1IngressList:
        return self.client.list_ingress_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class NetworkingV1beta1NamespacedIngressManager:
    def __init__(self, client: kubernetes.client.NetworkingV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.NetworkingV1beta1IngressList:
        return self.client.list_namespaced_ingress(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.NetworkingV1beta1Ingress,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.NetworkingV1beta1Ingress:
        return self.client.create_namespaced_ingress(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.NetworkingV1beta1Ingress:
        return self.client.read_namespaced_ingress(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.NetworkingV1beta1Ingress,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.NetworkingV1beta1Ingress:
        return self.client.replace_namespaced_ingress(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_ingress(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.NetworkingV1beta1Ingress:
        return self.client.patch_namespaced_ingress(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class NetworkingV1beta1CollectionNamespacedIngressManager:
    def __init__(self, client: kubernetes.client.NetworkingV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_ingress(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class NetworkingV1beta1NamespacedIngressStatusManager:
    def __init__(self, client: kubernetes.client.NetworkingV1beta1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.NetworkingV1beta1Ingress:
        return self.client.read_namespaced_ingress_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.NetworkingV1beta1Ingress,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.NetworkingV1beta1Ingress:
        return self.client.replace_namespaced_ingress_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.NetworkingV1beta1Ingress:
        return self.client.patch_namespaced_ingress_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class NodeV1alpha1RuntimeClassManager:
    def __init__(self, client: kubernetes.client.NodeV1alpha1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1RuntimeClassList:
        return self.client.list_runtime_class(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1alpha1RuntimeClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1RuntimeClass:
        return self.client.create_runtime_class(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1RuntimeClass:
        return self.client.read_runtime_class(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1alpha1RuntimeClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1RuntimeClass:
        return self.client.replace_runtime_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_runtime_class(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1RuntimeClass:
        return self.client.patch_runtime_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class NodeV1alpha1CollectionRuntimeClassManager:
    def __init__(self, client: kubernetes.client.NodeV1alpha1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_runtime_class(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class NodeV1beta1RuntimeClassManager:
    def __init__(self, client: kubernetes.client.NodeV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1RuntimeClassList:
        return self.client.list_runtime_class(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1beta1RuntimeClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1RuntimeClass:
        return self.client.create_runtime_class(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1RuntimeClass:
        return self.client.read_runtime_class(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1RuntimeClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1RuntimeClass:
        return self.client.replace_runtime_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_runtime_class(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1RuntimeClass:
        return self.client.patch_runtime_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class NodeV1beta1CollectionRuntimeClassManager:
    def __init__(self, client: kubernetes.client.NodeV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_runtime_class(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class PolicyV1beta1NamespacedPodDisruptionBudgetManager:
    def __init__(self, client: kubernetes.client.PolicyV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1PodDisruptionBudgetList:
        return self.client.list_namespaced_pod_disruption_budget(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1beta1PodDisruptionBudget,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1PodDisruptionBudget:
        return self.client.create_namespaced_pod_disruption_budget(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1PodDisruptionBudget:
        return self.client.read_namespaced_pod_disruption_budget(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1beta1PodDisruptionBudget,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1PodDisruptionBudget:
        return self.client.replace_namespaced_pod_disruption_budget(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_pod_disruption_budget(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1PodDisruptionBudget:
        return self.client.patch_namespaced_pod_disruption_budget(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class PolicyV1beta1CollectionNamespacedPodDisruptionBudgetManager:
    def __init__(self, client: kubernetes.client.PolicyV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_pod_disruption_budget(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class PolicyV1beta1NamespacedPodDisruptionBudgetStatusManager:
    def __init__(self, client: kubernetes.client.PolicyV1beta1Api) -> None:
        self.client = client

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1PodDisruptionBudget:
        return self.client.read_namespaced_pod_disruption_budget_status(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1beta1PodDisruptionBudget,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1PodDisruptionBudget:
        return self.client.replace_namespaced_pod_disruption_budget_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1PodDisruptionBudget:
        return self.client.patch_namespaced_pod_disruption_budget_status(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class PolicyV1beta1PodDisruptionBudgetForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.PolicyV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1PodDisruptionBudgetList:
        return self.client.list_pod_disruption_budget_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class PolicyV1beta1PodSecurityPolicyManager:
    def __init__(self, client: kubernetes.client.PolicyV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1PodSecurityPolicyList:
        return self.client.list_pod_security_policy(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1beta1PodSecurityPolicy,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1PodSecurityPolicy:
        return self.client.create_pod_security_policy(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1PodSecurityPolicy:
        return self.client.read_pod_security_policy(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1PodSecurityPolicy,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1PodSecurityPolicy:
        return self.client.replace_pod_security_policy(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1PodSecurityPolicy:
        return self.client.delete_pod_security_policy(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1PodSecurityPolicy:
        return self.client.patch_pod_security_policy(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class PolicyV1beta1CollectionPodSecurityPolicyManager:
    def __init__(self, client: kubernetes.client.PolicyV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_pod_security_policy(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class RbacAuthorizationV1ClusterRoleBindingManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ClusterRoleBindingList:
        return self.client.list_cluster_role_binding(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1ClusterRoleBinding,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ClusterRoleBinding:
        return self.client.create_cluster_role_binding(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1ClusterRoleBinding:
        return self.client.read_cluster_role_binding(name=name, pretty=pretty)

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1ClusterRoleBinding,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ClusterRoleBinding:
        return self.client.replace_cluster_role_binding(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_cluster_role_binding(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ClusterRoleBinding:
        return self.client.patch_cluster_role_binding(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class RbacAuthorizationV1CollectionClusterRoleBindingManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_cluster_role_binding(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class RbacAuthorizationV1ClusterRoleManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ClusterRoleList:
        return self.client.list_cluster_role(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1ClusterRole,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ClusterRole:
        return self.client.create_cluster_role(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1ClusterRole:
        return self.client.read_cluster_role(name=name, pretty=pretty)

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1ClusterRole,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1ClusterRole:
        return self.client.replace_cluster_role(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_cluster_role(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1ClusterRole:
        return self.client.patch_cluster_role(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class RbacAuthorizationV1CollectionClusterRoleManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_cluster_role(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class RbacAuthorizationV1NamespacedRoleBindingManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1RoleBindingList:
        return self.client.list_namespaced_role_binding(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1RoleBinding,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1RoleBinding:
        return self.client.create_namespaced_role_binding(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1RoleBinding:
        return self.client.read_namespaced_role_binding(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1RoleBinding,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1RoleBinding:
        return self.client.replace_namespaced_role_binding(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_role_binding(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1RoleBinding:
        return self.client.patch_namespaced_role_binding(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class RbacAuthorizationV1CollectionNamespacedRoleBindingManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_role_binding(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class RbacAuthorizationV1NamespacedRoleManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1RoleList:
        return self.client.list_namespaced_role(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1Role,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Role:
        return self.client.create_namespaced_role(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1Role:
        return self.client.read_namespaced_role(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1Role,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1Role:
        return self.client.replace_namespaced_role(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_role(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1Role:
        return self.client.patch_namespaced_role(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class RbacAuthorizationV1CollectionNamespacedRoleManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_role(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class RbacAuthorizationV1RoleBindingForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1RoleBindingList:
        return self.client.list_role_binding_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class RbacAuthorizationV1RoleForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1RoleList:
        return self.client.list_role_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class RbacAuthorizationV1alpha1ClusterRoleBindingManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1alpha1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1ClusterRoleBindingList:
        return self.client.list_cluster_role_binding(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1alpha1ClusterRoleBinding,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1ClusterRoleBinding:
        return self.client.create_cluster_role_binding(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1ClusterRoleBinding:
        return self.client.read_cluster_role_binding(name=name, pretty=pretty)

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1alpha1ClusterRoleBinding,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1ClusterRoleBinding:
        return self.client.replace_cluster_role_binding(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_cluster_role_binding(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1ClusterRoleBinding:
        return self.client.patch_cluster_role_binding(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class RbacAuthorizationV1alpha1CollectionClusterRoleBindingManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1alpha1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_cluster_role_binding(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class RbacAuthorizationV1alpha1ClusterRoleManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1alpha1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1ClusterRoleList:
        return self.client.list_cluster_role(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1alpha1ClusterRole,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1ClusterRole:
        return self.client.create_cluster_role(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1ClusterRole:
        return self.client.read_cluster_role(name=name, pretty=pretty)

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1alpha1ClusterRole,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1ClusterRole:
        return self.client.replace_cluster_role(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_cluster_role(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1ClusterRole:
        return self.client.patch_cluster_role(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class RbacAuthorizationV1alpha1CollectionClusterRoleManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1alpha1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_cluster_role(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class RbacAuthorizationV1alpha1NamespacedRoleBindingManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1alpha1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1RoleBindingList:
        return self.client.list_namespaced_role_binding(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1alpha1RoleBinding,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1RoleBinding:
        return self.client.create_namespaced_role_binding(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1RoleBinding:
        return self.client.read_namespaced_role_binding(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1alpha1RoleBinding,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1RoleBinding:
        return self.client.replace_namespaced_role_binding(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_role_binding(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1RoleBinding:
        return self.client.patch_namespaced_role_binding(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class RbacAuthorizationV1alpha1CollectionNamespacedRoleBindingManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1alpha1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_role_binding(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class RbacAuthorizationV1alpha1NamespacedRoleManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1alpha1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1RoleList:
        return self.client.list_namespaced_role(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1alpha1Role,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1Role:
        return self.client.create_namespaced_role(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1Role:
        return self.client.read_namespaced_role(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1alpha1Role,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1Role:
        return self.client.replace_namespaced_role(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_role(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1Role:
        return self.client.patch_namespaced_role(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class RbacAuthorizationV1alpha1CollectionNamespacedRoleManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1alpha1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_role(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class RbacAuthorizationV1alpha1RoleBindingForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1alpha1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1RoleBindingList:
        return self.client.list_role_binding_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class RbacAuthorizationV1alpha1RoleForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1alpha1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1RoleList:
        return self.client.list_role_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class RbacAuthorizationV1beta1ClusterRoleBindingManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1ClusterRoleBindingList:
        return self.client.list_cluster_role_binding(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1beta1ClusterRoleBinding,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1ClusterRoleBinding:
        return self.client.create_cluster_role_binding(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1ClusterRoleBinding:
        return self.client.read_cluster_role_binding(name=name, pretty=pretty)

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1ClusterRoleBinding,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1ClusterRoleBinding:
        return self.client.replace_cluster_role_binding(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_cluster_role_binding(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1ClusterRoleBinding:
        return self.client.patch_cluster_role_binding(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class RbacAuthorizationV1beta1CollectionClusterRoleBindingManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_cluster_role_binding(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class RbacAuthorizationV1beta1ClusterRoleManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1ClusterRoleList:
        return self.client.list_cluster_role(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1beta1ClusterRole,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1ClusterRole:
        return self.client.create_cluster_role(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1ClusterRole:
        return self.client.read_cluster_role(name=name, pretty=pretty)

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1ClusterRole,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1ClusterRole:
        return self.client.replace_cluster_role(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_cluster_role(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1ClusterRole:
        return self.client.patch_cluster_role(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class RbacAuthorizationV1beta1CollectionClusterRoleManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_cluster_role(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class RbacAuthorizationV1beta1NamespacedRoleBindingManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1RoleBindingList:
        return self.client.list_namespaced_role_binding(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1beta1RoleBinding,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1RoleBinding:
        return self.client.create_namespaced_role_binding(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1RoleBinding:
        return self.client.read_namespaced_role_binding(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1beta1RoleBinding,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1RoleBinding:
        return self.client.replace_namespaced_role_binding(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_role_binding(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1RoleBinding:
        return self.client.patch_namespaced_role_binding(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class RbacAuthorizationV1beta1CollectionNamespacedRoleBindingManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_role_binding(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class RbacAuthorizationV1beta1NamespacedRoleManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1RoleList:
        return self.client.list_namespaced_role(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1beta1Role,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1Role:
        return self.client.create_namespaced_role(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1Role:
        return self.client.read_namespaced_role(
            name=name, namespace=namespace, pretty=pretty
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1beta1Role,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1Role:
        return self.client.replace_namespaced_role(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_role(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1Role:
        return self.client.patch_namespaced_role(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class RbacAuthorizationV1beta1CollectionNamespacedRoleManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_role(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class RbacAuthorizationV1beta1RoleBindingForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1RoleBindingList:
        return self.client.list_role_binding_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class RbacAuthorizationV1beta1RoleForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.RbacAuthorizationV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1RoleList:
        return self.client.list_role_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class SchedulingV1PriorityClassManager:
    def __init__(self, client: kubernetes.client.SchedulingV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PriorityClassList:
        return self.client.list_priority_class(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1PriorityClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1PriorityClass:
        return self.client.create_priority_class(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PriorityClass:
        return self.client.read_priority_class(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1PriorityClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1PriorityClass:
        return self.client.replace_priority_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_priority_class(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1PriorityClass:
        return self.client.patch_priority_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class SchedulingV1CollectionPriorityClassManager:
    def __init__(self, client: kubernetes.client.SchedulingV1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_priority_class(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class SchedulingV1alpha1PriorityClassManager:
    def __init__(self, client: kubernetes.client.SchedulingV1alpha1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1PriorityClassList:
        return self.client.list_priority_class(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1alpha1PriorityClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1PriorityClass:
        return self.client.create_priority_class(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1PriorityClass:
        return self.client.read_priority_class(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1alpha1PriorityClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1PriorityClass:
        return self.client.replace_priority_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_priority_class(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1PriorityClass:
        return self.client.patch_priority_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class SchedulingV1alpha1CollectionPriorityClassManager:
    def __init__(self, client: kubernetes.client.SchedulingV1alpha1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_priority_class(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class SchedulingV1beta1PriorityClassManager:
    def __init__(self, client: kubernetes.client.SchedulingV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1PriorityClassList:
        return self.client.list_priority_class(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1beta1PriorityClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1PriorityClass:
        return self.client.create_priority_class(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1PriorityClass:
        return self.client.read_priority_class(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1PriorityClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1PriorityClass:
        return self.client.replace_priority_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_priority_class(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1PriorityClass:
        return self.client.patch_priority_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class SchedulingV1beta1CollectionPriorityClassManager:
    def __init__(self, client: kubernetes.client.SchedulingV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_priority_class(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class SettingsV1alpha1NamespacedPodPresetManager:
    def __init__(self, client: kubernetes.client.SettingsV1alpha1Api) -> None:
        self.client = client

    def list(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1PodPresetList:
        return self.client.list_namespaced_pod_preset(
            namespace=namespace,
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        namespace: str,
        body: kubernetes.client.V1alpha1PodPreset,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1PodPreset:
        return self.client.create_namespaced_pod_preset(
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def read(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1PodPreset:
        return self.client.read_namespaced_pod_preset(
            name=name, namespace=namespace, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        namespace: str,
        body: kubernetes.client.V1alpha1PodPreset,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1PodPreset:
        return self.client.replace_namespaced_pod_preset(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_namespaced_pod_preset(
            name=name,
            namespace=namespace,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1PodPreset:
        return self.client.patch_namespaced_pod_preset(
            name=name,
            namespace=namespace,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class SettingsV1alpha1CollectionNamespacedPodPresetManager:
    def __init__(self, client: kubernetes.client.SettingsV1alpha1Api) -> None:
        self.client = client

    def delete(
        self,
        namespace: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_namespaced_pod_preset(
            namespace=namespace,
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class SettingsV1alpha1PodPresetForAllNamespacesManager:
    def __init__(self, client: kubernetes.client.SettingsV1alpha1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pretty: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1PodPresetList:
        return self.client.list_pod_preset_for_all_namespaces(
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            pretty=pretty,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )


class StorageV1CsiDriverManager:
    def __init__(self, client: kubernetes.client.StorageV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1CSIDriverList:
        return self.client.list_csi_driver(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1CSIDriver,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1CSIDriver:
        return self.client.create_csi_driver(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1CSIDriver:
        return self.client.read_csi_driver(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1CSIDriver,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1CSIDriver:
        return self.client.replace_csi_driver(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1CSIDriver:
        return self.client.delete_csi_driver(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1CSIDriver:
        return self.client.patch_csi_driver(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class StorageV1CollectionCsiDriverManager:
    def __init__(self, client: kubernetes.client.StorageV1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_csi_driver(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class StorageV1CsiNodeManager:
    def __init__(self, client: kubernetes.client.StorageV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1CSINodeList:
        return self.client.list_csi_node(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1CSINode,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1CSINode:
        return self.client.create_csi_node(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1CSINode:
        return self.client.read_csi_node(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1CSINode,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1CSINode:
        return self.client.replace_csi_node(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1CSINode:
        return self.client.delete_csi_node(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1CSINode:
        return self.client.patch_csi_node(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class StorageV1CollectionCsiNodeManager:
    def __init__(self, client: kubernetes.client.StorageV1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_csi_node(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class StorageV1StorageClassManager:
    def __init__(self, client: kubernetes.client.StorageV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1StorageClassList:
        return self.client.list_storage_class(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1StorageClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1StorageClass:
        return self.client.create_storage_class(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1StorageClass:
        return self.client.read_storage_class(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1StorageClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1StorageClass:
        return self.client.replace_storage_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1StorageClass:
        return self.client.delete_storage_class(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1StorageClass:
        return self.client.patch_storage_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class StorageV1CollectionStorageClassManager:
    def __init__(self, client: kubernetes.client.StorageV1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_storage_class(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class StorageV1VolumeAttachmentManager:
    def __init__(self, client: kubernetes.client.StorageV1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1VolumeAttachmentList:
        return self.client.list_volume_attachment(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1VolumeAttachment,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1VolumeAttachment:
        return self.client.create_volume_attachment(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1VolumeAttachment:
        return self.client.read_volume_attachment(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1VolumeAttachment,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1VolumeAttachment:
        return self.client.replace_volume_attachment(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1VolumeAttachment:
        return self.client.delete_volume_attachment(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1VolumeAttachment:
        return self.client.patch_volume_attachment(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class StorageV1CollectionVolumeAttachmentManager:
    def __init__(self, client: kubernetes.client.StorageV1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_volume_attachment(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class StorageV1VolumeAttachmentStatusManager:
    def __init__(self, client: kubernetes.client.StorageV1Api) -> None:
        self.client = client

    def read(
        self, name: str, *, pretty: typing.Optional[str] = None
    ) -> kubernetes.client.V1VolumeAttachment:
        return self.client.read_volume_attachment_status(name=name, pretty=pretty)

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1VolumeAttachment,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1VolumeAttachment:
        return self.client.replace_volume_attachment_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1VolumeAttachment:
        return self.client.patch_volume_attachment_status(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class StorageV1alpha1VolumeAttachmentManager:
    def __init__(self, client: kubernetes.client.StorageV1alpha1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1VolumeAttachmentList:
        return self.client.list_volume_attachment(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1alpha1VolumeAttachment,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1VolumeAttachment:
        return self.client.create_volume_attachment(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1VolumeAttachment:
        return self.client.read_volume_attachment(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1alpha1VolumeAttachment,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1VolumeAttachment:
        return self.client.replace_volume_attachment(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1alpha1VolumeAttachment:
        return self.client.delete_volume_attachment(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1alpha1VolumeAttachment:
        return self.client.patch_volume_attachment(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class StorageV1alpha1CollectionVolumeAttachmentManager:
    def __init__(self, client: kubernetes.client.StorageV1alpha1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_volume_attachment(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class StorageV1beta1CsiDriverManager:
    def __init__(self, client: kubernetes.client.StorageV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CSIDriverList:
        return self.client.list_csi_driver(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1beta1CSIDriver,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CSIDriver:
        return self.client.create_csi_driver(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CSIDriver:
        return self.client.read_csi_driver(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1CSIDriver,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CSIDriver:
        return self.client.replace_csi_driver(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CSIDriver:
        return self.client.delete_csi_driver(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CSIDriver:
        return self.client.patch_csi_driver(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class StorageV1beta1CollectionCsiDriverManager:
    def __init__(self, client: kubernetes.client.StorageV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_csi_driver(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class StorageV1beta1CsiNodeManager:
    def __init__(self, client: kubernetes.client.StorageV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CSINodeList:
        return self.client.list_csi_node(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1beta1CSINode,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CSINode:
        return self.client.create_csi_node(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CSINode:
        return self.client.read_csi_node(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1CSINode,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CSINode:
        return self.client.replace_csi_node(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1CSINode:
        return self.client.delete_csi_node(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1CSINode:
        return self.client.patch_csi_node(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class StorageV1beta1CollectionCsiNodeManager:
    def __init__(self, client: kubernetes.client.StorageV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_csi_node(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class StorageV1beta1StorageClassManager:
    def __init__(self, client: kubernetes.client.StorageV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1StorageClassList:
        return self.client.list_storage_class(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1beta1StorageClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1StorageClass:
        return self.client.create_storage_class(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1StorageClass:
        return self.client.read_storage_class(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1StorageClass,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1StorageClass:
        return self.client.replace_storage_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1StorageClass:
        return self.client.delete_storage_class(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1StorageClass:
        return self.client.patch_storage_class(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class StorageV1beta1CollectionStorageClassManager:
    def __init__(self, client: kubernetes.client.StorageV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_storage_class(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )


class StorageV1beta1VolumeAttachmentManager:
    def __init__(self, client: kubernetes.client.StorageV1beta1Api) -> None:
        self.client = client

    def list(
        self,
        *,
        pretty: typing.Optional[str] = None,
        allow_watch_bookmarks: typing.Optional[bool] = None,
        _continue: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None,
        watch: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1VolumeAttachmentList:
        return self.client.list_volume_attachment(
            pretty=pretty,
            allow_watch_bookmarks=allow_watch_bookmarks,
            _continue=_continue,
            field_selector=field_selector,
            label_selector=label_selector,
            limit=limit,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
            watch=watch,
        )

    def create(
        self,
        body: kubernetes.client.V1beta1VolumeAttachment,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1VolumeAttachment:
        return self.client.create_volume_attachment(
            body=body, pretty=pretty, dry_run=dry_run, field_manager=field_manager
        )

    def read(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        exact: typing.Optional[bool] = None,
        export: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1VolumeAttachment:
        return self.client.read_volume_attachment(
            name=name, pretty=pretty, exact=exact, export=export
        )

    def replace(
        self,
        name: str,
        body: kubernetes.client.V1beta1VolumeAttachment,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1VolumeAttachment:
        return self.client.replace_volume_attachment(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
        )

    def delete(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        dry_run: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None
    ) -> kubernetes.client.V1beta1VolumeAttachment:
        return self.client.delete_volume_attachment(
            name=name,
            pretty=pretty,
            body=body,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
        )

    def patch(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_manager: typing.Optional[str] = None,
        force: typing.Optional[bool] = None
    ) -> kubernetes.client.V1beta1VolumeAttachment:
        return self.client.patch_volume_attachment(
            name=name,
            body=body,
            pretty=pretty,
            dry_run=dry_run,
            field_manager=field_manager,
            force=force,
        )


class StorageV1beta1CollectionVolumeAttachmentManager:
    def __init__(self, client: kubernetes.client.StorageV1beta1Api) -> None:
        self.client = client

    def delete(
        self,
        *,
        pretty: typing.Optional[str] = None,
        body: typing.Optional[kubernetes.client.V1DeleteOptions] = None,
        _continue: typing.Optional[str] = None,
        dry_run: typing.Optional[str] = None,
        field_selector: typing.Optional[str] = None,
        grace_period_seconds: typing.Optional[int] = None,
        label_selector: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        orphan_dependents: typing.Optional[bool] = None,
        propagation_policy: typing.Optional[str] = None,
        resource_version: typing.Optional[str] = None,
        resource_version_match: typing.Optional[str] = None,
        timeout_seconds: typing.Optional[int] = None
    ) -> kubernetes.client.V1Status:
        return self.client.delete_collection_volume_attachment(
            pretty=pretty,
            body=body,
            _continue=_continue,
            dry_run=dry_run,
            field_selector=field_selector,
            grace_period_seconds=grace_period_seconds,
            label_selector=label_selector,
            limit=limit,
            orphan_dependents=orphan_dependents,
            propagation_policy=propagation_policy,
            resource_version=resource_version,
            resource_version_match=resource_version_match,
            timeout_seconds=timeout_seconds,
        )
