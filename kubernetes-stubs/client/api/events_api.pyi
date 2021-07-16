import typing

import kubernetes.client

class EventsApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
