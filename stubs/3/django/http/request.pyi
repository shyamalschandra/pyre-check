from typing import Any, BinaryIO, Dict, List, Optional, Tuple


# TODO(T22838703): currently this is just shutting up pyre. Properly typing
# this will be low hanging fruit later on.


class HttpRequest(BinaryIO):
    COOKIES: Any = ...
    DEVICE_LANGUAGE_CODE: Any = ...
    FILES: Any = ...
    GET: Any = ...
    LANGUAGE_CODE: Any = ...
    META: Any = ...
    POST: Any = ...
    _body: Any = ...

    _cached_carrier_id: Any = ...
    _cached_carrier_name: Any = ...
    _cached_cdn_prefix: Any = ...
    _cached_wallet_defs: Any = ...

    _read_started: Any = ...
    _slipstream_user_id: Any = ...
    _slipstream_view_name: Any = ...
    _wide_color_enabled: Any = ...
    accepted_lang_header: Any = ...
    akamai_migration: Any = ...
    allow_all_platforms: Any = ...
    app_id: Any = ...
    app_platform: Any = ...
    app_version: Any = ...
    asns: Any = ...
    asyncio_disable_gather: Any = ...
    body: Any = ...
    bypass_cookie_refresh: Any = ...
    cached_carrier_name: Any = ...
    carrier_id: Any = ...
    client_ip: Any = ...
    connection_quality: Any = ...
    context: Any = ...
    count_followed_by: Any = ...
    count_follows: Any = ...
    country_code: Any = ...
    display: Any = ...
    edge_vip: Any = ...
    harakiri_timeout: Any = ...
    is_direct_app: Any = ...
    is_image_low_data_mode: Any = ...
    is_prelease_eligible: Any = ...
    is_video_low_data_mode: Any = ...
    locale_lower_case: Any = ...
    locale: Any = ...
    login_platform: Any = ...
    login_required_middleware_csrf: Any = ...
    machineid_cookie: Any = ...
    maybe_log_rest_sample: Any = ...
    method: Any = ...
    network_info: Any = ...
    os_version: Any = ...
    overwrite_app_platform: Any = ...
    path_info: Any = ...
    path: Any = ...
    platform_details: Any = ...
    remote_ip: Any = ...
    request_origin: Any = ...
    request_uuid: Any = ...
    resolver_match: Any = ...
    session: Any = ...
    signed_body: Any = ...
    signed_request: Any = ...
    slipstream: Any = ...
    source: Any = ...
    ua_string_md5: Any = ...
    started_at: Any = ...
    upload_timeout: Any = ...
    user_agent_string: Any = ...
    user_agent: Any = ...
    user: Any = ...
    via_headers: Any = ...
    view_module: Any = ...
    view_name: Any = ...

    def build_absolute_uri(self, location: Optional[str] = ...) -> str:
        ...

    def get_full_path(self) -> str:
        ...

    def get_host(self) -> str:
        ...

    def get_signed_cookie(
        self, key: str, default: Any = ..., salt: str = ..., max_age: Any = ...
    ) -> str:
        ...

    def is_ajax(self) -> bool:
        ...


class QueryDict(Dict[str, Any]):
    def __init__(
        self,
        query_string: Optional[str] = ...,
        mutable: bool = ...,
        encoding: Any = ...,
    ) -> None:
        ...

    def lists(self) -> List[Tuple[str, Any]]:
        ...


def build_request_repr(
    request: HttpRequest,
    path_override: Any = ...,
    GET_override: Any = ...,
    POST_override: Any = ...,
    COOKIES_override: Any = ...,
    META_override: Any = ...,
) -> str:
    ...
