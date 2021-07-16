import typing

import kubernetes.client

class VersionApi:
    def get_code(self) -> kubernetes.client.VersionInfo: ...
