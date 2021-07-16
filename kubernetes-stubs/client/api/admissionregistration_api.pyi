import typing

import kubernetes.client

class AdmissionregistrationApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
