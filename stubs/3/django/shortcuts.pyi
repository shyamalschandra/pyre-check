from typing import Any

from django.http.response import HttpResponseRedirect


def get_object_or_404(klass: Any, *args: Any, **kwargs: Any) -> Any:
    ...


def redirect(to: Any, *args: Any, **kwargs: Any) -> HttpResponseRedirect:
    ...
