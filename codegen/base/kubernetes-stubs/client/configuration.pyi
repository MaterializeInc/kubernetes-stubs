import logging
from typing import Callable, Optional

class Configuration(object):
    host: str
    temp_folder_path: str
    api_key: dict[str, str]
    api_key_prefix: str
    username: str
    password: str
    discard_unknown_keys: bool

    refresh_api_key_hook: Callable[[Configuration], None]
    logger: dict[str, logging.Logger]
    logger_format: str
    logger_stream_handler: logging.StreamHandler
    logger_file_handler: logging.FileHandler
    logger_file: str
    debug: bool = False
    verify_ssl: bool = True
    ssl_ca_cert: str
    cert_file: str
    key_file: str
    assert_hostname: bool
    connection_pool_maxsize: int
    proxy: str
    no_proxy: str
    proxy_headers: dict[str, str]
    safe_chars_for_path_param: str = ""
    retries: int
    client_side_validation: bool = True

    def __init__(
        self,
        host: str = ...,
        api_key: Optional[str] = ...,
        api_key_prefix: Optional[str] = ...,
        username: Optional[str] = ...,
        password: Optional[str] = ...,
        discard_unknown_keys: bool = ...,
    ) -> None: ...
    @classmethod
    def set_default(cls, default: Configuration): ...
    @classmethod
    def get_default_copy(cls) -> Configuration: ...
