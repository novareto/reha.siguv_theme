from reiter.application.browser import registries, TemplateLoader


TEMPLATES = TemplateLoader("./templates")
ui = registries.UIRegistry(macros=TEMPLATES['macros.pt'].macros)
