import datetime
import typing

import kubernetes.client

class VersionInfo:
    build_date: str
    compiler: str
    git_commit: str
    git_tree_state: str
    git_version: str
    go_version: str
    major: str
    minor: str
    platform: str
    def __init__(
        self,
        *,
        build_date: str,
        compiler: str,
        git_commit: str,
        git_tree_state: str,
        git_version: str,
        go_version: str,
        major: str,
        minor: str,
        platform: str
    ) -> None: ...
