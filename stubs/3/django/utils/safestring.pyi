class SafeData(object):
    ...


class SafeText(str, SafeData):
    ...


SafeString = SafeText


def mark_safe(s: str) -> SafeString:
    ...
