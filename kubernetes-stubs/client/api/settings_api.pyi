import typing

import kubernetes.client

class SettingsApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
