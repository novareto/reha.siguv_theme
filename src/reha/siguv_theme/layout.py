from reiter.application.browser import TemplateLoader
from reha.siguv_theme.resources import theme


TEMPLATES = TemplateLoader("./templates")
GLOBAL_MACROS = TEMPLATES['macros.pt'].macros


class Layout:

    __slots__ = ("_template", "name")

    def __init__(self, request, name):
        self.name = name
        self._template = TEMPLATES["layout.pt"]

    def render(self, content, **namespace):
        theme.need()
        return self._template.render(content=content, **namespace)


def sitecap(request, name, view):
    return TEMPLATES["sitecap.pt"].render(request=request)


def globalmenu(request, name, view):
    return TEMPLATES["globalmenu.pt"].render(request=request)


def navbar(request, name, view):
    return TEMPLATES["navbar.pt"].render(request=request)


def sidebar(request, name, view):
    return TEMPLATES["sidebar.pt"].render(request=request)


def messages(request, name, view):
    utility = request.utilities.get("flash")
    if utility is not None:
        messages = list(utility)
    else:
        messages = []
    return TEMPLATES["messages.pt"].render(messages=messages)


def footer(request, name, view):
    return TEMPLATES["footer.pt"].render(request=request)
