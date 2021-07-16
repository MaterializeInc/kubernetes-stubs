import typing

import kubernetes.client

class LogsApi:
    def log_file_list_handler(self) -> None: ...
    def log_file_handler(self, logpath: str) -> None: ...
