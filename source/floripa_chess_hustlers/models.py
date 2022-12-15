from attr import define


@define
class Youtube:
    title: str
    url: str
    description: str = ""
