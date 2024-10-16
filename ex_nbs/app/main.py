"""FrankenUI Tasks Example"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../99_main.ipynb.

# %% auto 0
__all__ = ['hdrs', 'app', 'theme_switcher', 'tasks', 'cards', 'dashboard', 'forms', 'music', 'auth', 'playground', 'mail',
           'Navbar', 'NavItem', 'NavDropdown', 'UkNavBar', 'home']

# %% ../99_main.ipynb
from fasthtml.common import *
import fasthtml.common as fh
from fh_frankenui.components import *
from fh_frankenui.core import *
from fasthtml.components import Uk_icon, Uk_theme_switcher

# %% ../99_main.ipynb
from tasks import tasks_homepage
from cards import cards_homepage
from dashboard import dashboard_homepage
from forms import forms_homepage
from music import music_homepage
from auth import auth_homepage
from playground import playground_homepage
from mail import mail_homepage

# %% ../99_main.ipynb
hdrs = (fh.Script(src="https://cdn.tailwindcss.com"),
        fh.Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit.min.js"),
        fh.Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit-icons.min.js"),
        fh.Script(type="module", src="https://unpkg.com/franken-wc@0.0.6/dist/js/wc.iife.js"),
        fh.Link(rel="stylesheet", href="https://unpkg.com/franken-wc@0.0.6/dist/css/blue.min.css"),)

# %% ../99_main.ipynb
app = FastHTML(hdrs=Theme.blue.headers(),debug=True,default_hdrs=False)

# %% ../99_main.ipynb
@app.route('/tasks')
def tasks(): return tasks_homepage

@app.route('/cards')
def cards(): return cards_homepage

@app.route('/dashboard')
def dashboard(): return dashboard_homepage

@app.route('/forms')
def forms(): return forms_homepage

@app.route('/music')
def music(): return music_homepage

@app.route('/auth')
def auth(): return auth_homepage

@app.route('/playground')
def playground(): return playground_homepage

@app.route('/mail')
def mail(): return mail_homepage

# %% ../99_main.ipynb
def Navbar(*c, left=(), center=(), right=(), container=True, transparent=False, sticky=False, cls=(), **kwargs):
    nav_cls = f"uk-navbar-container{'uk-navbar-transparent' if transparent else ''}"
    nav = Nav(cls=nav_cls, uk_navbar=True, **kwargs)(
        Div(cls='uk-navbar-left')(*left) if left else None,
        Div(cls='uk-navbar-center')(*center) if center else None,
        Div(cls='uk-navbar-right')(*right) if right else None,
        *c
    )
    sticky_attrs = {'uk-sticky': 'sel-target: .uk-navbar-container; cls-active: uk-navbar-sticky'} if sticky else {}
    return Div(cls=f"uk-container {stringify(cls)}" if container else stringify(cls), **sticky_attrs)(nav)

def NavItem(label, href='#', active=False, parent=False, cls=()):
    item_cls = f"{'uk-active' if active else ''} {'uk-parent' if parent else ''} {stringify(cls)}".strip()
    return Li(cls=item_cls)(A(href=href)(label))

def NavDropdown(label, items, cls=()):
    return Li(cls=f"uk-parent {stringify(cls)}".strip())(
        A(href='#')(label),
        Div(cls='uk-navbar-dropdown')(Ul(cls='uk-nav uk-navbar-dropdown-nav')(*items)))

# %% ../99_main.ipynb
def UkNavBar(*lis):
    return Nav(cls='uk-navbar-left')(
        Ul(cls='uk-navbar-nav')(
        *lis
        ))

# %% ../99_main.ipynb
theme_switcher = Div(
    Button(Span("Change to Dark Theme", id='theme-toggle-light-icon', cls='dark:hidden'),
            Span("Change to Light Theme", id='theme-toggle-dark-icon', cls='hidden dark:block'),
            id='theme-toggle'),

Script('var themeToggleBtn = document.getElementById("theme-toggle");\r\n    themeToggleBtn.addEventListener("click", function () {\r\n      if (localStorage.getItem("color-theme")) {\r\n        if (localStorage.getItem("color-theme") === "light") {\r\n          document.documentElement.classList.add("dark");\r\n          localStorage.setItem("color-theme", "dark");\r\n        } else {\r\n          document.documentElement.classList.remove("dark");\r\n          localStorage.setItem("color-theme", "light");\r\n        }\r\n      } else {\r\n        if (document.documentElement.classList.contains("dark")) {\r\n          document.documentElement.classList.remove("dark");\r\n          localStorage.setItem("color-theme", "light");\r\n        } else {\r\n          document.documentElement.classList.add("dark");\r\n          localStorage.setItem("color-theme", "dark");\r\n        }\r\n      }\r\n    });'))

# %% ../99_main.ipynb
@app.route('/')
def home():
    sidebar_items = ["Tasks", "Cards", "Dashboard", "Form", "Music", "Auth", "Playground", "Mail", "Theme"]

    sidebar = NavContainer(map(lambda x: Li(A(x)),sidebar_items),
                uk_switcher="connect: #main-nav; animation: uk-animation-fade",
                cls=(NavT.secondary,"space-y-4 p-4 w-1/10"))

    content = Div(cls="flex-1")(
        Ul(id="main-nav", cls="uk-switcher w-full")(
            Li(tasks_homepage),
            Li(cards_homepage),
            Li(dashboard_homepage),
            Li(forms_homepage),
            Li(music_homepage),
            Li(auth_homepage),
            Li(playground_homepage),
            Li(mail_homepage),   
            Li(theme_switcher)
        ))
    return Body(cls="bg-background text-foreground")(Div(cls="flex w-full")(sidebar,content))          


# %% ../99_main.ipynb
serve()
