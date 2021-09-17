from fanstatic import Library, Resource, Group
from uvcreha.browser.resources import application_webpush,  f_input_group


library = Library("reha.siguv_theme", "static")

custom_css = Resource(library, "siguvtheme.css")

sidebar_css = Resource(library, "sidebar.css")

main_css = Resource(library, "main.css")

main_js = Resource(library, "main.js")

bootstrap_css = Resource(
    library,
    "uvc_serviceportal_bootstrap.css",
    compiler="sass",
    source="scss/siguv.scss",
)

bootstrap_js = Resource(
    library,
    "bootstrap.bundle.js",
    depends=[main_js],
    bottom=True
)

siguvtheme = Group(
    [
        application_webpush,
        custom_css,
        main_css,
        sidebar_css,
        bootstrap_css,
        bootstrap_js,
        f_input_group
    ]
)
