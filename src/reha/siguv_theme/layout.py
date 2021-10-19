from reiter.application.browser import TemplateLoader
from reha.siguv_theme.resources import theme
from reha.prototypes.contents.meta import ContentAction


TEMPLATES = TemplateLoader("./templates")
GLOBAL_MACROS = TEMPLATES['macros.pt'].macros


class Layout:

    _template = TEMPLATES["layout.pt"]

    def __init__(self, request, name):
        self.name = name

    def render(self, content, **namespace):
        theme.need()
        return self._template.render(content=content, **namespace)


def sitecap(request, name, view):
    return TEMPLATES["sitecap.pt"].render(request=request)


def globalmenu(request, name, view):
    actions = [
        ContentAction(item=request.app, request=request, action=action)
        for action in request.app.actions.partial('global')
    ]
    return TEMPLATES["globalmenu.pt"].render(
        request=request, actions=actions)


def above_content(request, name, view):
    actions = [
        ContentAction(item=request.app, request=request, action=action)
        for action in request.app.actions.partial('content')
    ]
    return TEMPLATES["content.pt"].render(
        request=request, actions=actions
    )


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
