import typing

import kubernetes.client

class AuditregistrationApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
