from typing import Any, Dict, List, Optional

from django.http import Http404


class Resolver404(Http404):
    ...


class ResolverMatch:
    kwargs: Dict[str, Any] = ...
    view_name: str = ...
    func: Any = ...
    args: Any = ...
    url_name: str = ...
    app_name: str = ...
    _func_path: str = ...
    view_path: str = ...

    def __getitem__(self, index) -> Any:
        ...


class NoReverseMatch(Exception):
    ...


def reverse(
    viewname: Any,
    urlconf: Any = ...,
    args: Optional[List[Any]] = ...,
    kwargs: Optional[Dict[str, Any]] = ...,
    prefix: Any = ...,
    current_app: Any = ...,
) -> str:
    ...


def resolve(path: str, urlconf: Any = ...) -> ResolverMatch:
    ...
