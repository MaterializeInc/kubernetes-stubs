import typing

import kubernetes.client

class CertificatesApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
