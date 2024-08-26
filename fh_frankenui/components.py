# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_components.ipynb.

# %% auto 0
__all__ = ['UkInput', 'UkSwitch', 'UkTextArea', 'UkFormLabel', 'UkH1', 'UkH2', 'UkH3', 'UkH4', 'UkH5', 'UkH6', 'stringify',
           'VEnum', 'Theme', 'TextB', 'TextT', 'UkGenericInput', 'Options', 'UkSelect', 'UkButtonT', 'UkDropdownButton',
           'UkButton', 'UkGenericComponent', 'UkHSplit', 'Card']

# %% ../nbs/01_components.ipynb 15
from fasthtml.common import *
from fasthtml.svg import Svg
from enum import Enum, EnumType
from fasthtml.components import Uk_select,Uk_input_tag
from functools import partial

# %% ../nbs/01_components.ipynb 21
def stringify(o):
    # need a better name, stringify might be too general for what it does 
    if is_listy(o): return ' '.join(map(str,o)) if o else ""
    return o.__str__()

# %% ../nbs/01_components.ipynb 23
class VEnum(Enum):
    def __add__(self, other):
        return stringify((self, other))

    def __radd__(self, other):
        return stringify((other, self))
    
    def __str__(self):
        base = self.__class__.__name__       
        if isinstance(self.__class__, EnumType):
            base = base.lstrip('Uk').rstrip('T')
        return f"uk-{base.lower()}-{self.value}".strip('-')

# %% ../nbs/01_components.ipynb 25
class Theme(Enum):
    slate = "slate"
    stone = "stone"
    gray = "gray"
    neutral = "neutral"
    red = "red"
    rose = "rose"
    orange = "orange"
    green = "green"
    blue = "blue"
    yellow = "yellow"
    violet = "violet"
    zinc = "zinc"

    def headers(self):
        js = (Script(src="https://cdn.tailwindcss.com"),
              Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit.min.js"),
              Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit-icons.min.js"),
              Script(type="module", src="https://unpkg.com/franken-wc@0.0.6/dist/js/wc.iife.js")
              )
        _url = "https://unpkg.com/franken-wc@0.0.6/dist/css/{theme}.min.css"
        return (*js, Link(rel="stylesheet", href=_url.format(theme=self.value)))

# %% ../nbs/01_components.ipynb 26
class TextB(Enum):
    sz_xsmall = 'text-xs'
    sz_small = 'text-sm'
    cl_muted = 'uk-text-muted'
    
    wt_light = 'font-light'
    wt_normal = 'font-normal'
    wt_medium = 'font-medium'
    wt_bold = 'font-bold'
# font-thin	font-weight: 100;
# font-extralight	font-weight: 200;
# font-light	font-weight: 300;
# font-normal	font-weight: 400;
# 
# font-semibold	font-weight: 600;
# font-bold	font-weight: 700;
# font-extrabold	font-weight: 800;
# font-black    
    
    
# font-medium text-sm
    def __str__(self):
        return self.value

# %% ../nbs/01_components.ipynb 27
class TextT(Enum):
    muted_sm = TextB.sz_small, TextB.cl_muted # Text below card headings
    medium_sm = TextB.sz_small, TextB.wt_medium

    def __str__(self):
        if is_listy(self.value): return ' '.join(map(str,self.value))
        return self.value

# %% ../nbs/01_components.ipynb 30
def UkGenericInput(input_fn,
                    label=(), 
                    lbl_cls=(),
                    inp_cls=(),
                    cls=('space-y-2',), # Div cls
                    id="", **kwargs):
    lbl_cls, inp_cls, cls = map(stringify,(lbl_cls, inp_cls, cls))
    if label: 
        label = Label(cls='uk-form-label '+lbl_cls)(label)
        if id: label.fr = id
    res = input_fn(**kwargs)
    if inp_cls: res.attrs['class'] += inp_cls
    if id: res.id = id
    return Div(cls=cls)(label, res)

# %% ../nbs/01_components.ipynb 31
UkInput =     partial(UkGenericInput, partial(Input,        cls='uk-input'))
UkSwitch =    partial(UkGenericInput, partial(CheckboxX,    cls='uk-toggle-switch uk-toggle-switch-primary')) 
UkTextArea =  partial(UkGenericInput, partial(Textarea,     cls='uk-textarea'))
UkFormLabel = partial(UkGenericInput, partial(Uk_input_tag, cls='uk-form-label'))

# %% ../nbs/01_components.ipynb 32
def Options(options: tuple, selected_idx=None):
    return [Option(o,selected=i==selected_idx) for i,o in enumerate(options)]

# %% ../nbs/01_components.ipynb 34
def UkSelect(*options,
            label=(), 
            lbl_cls=(),
            inp_cls=(),
            cls=('space-y-2',), # Div cls
            id="", **kwargs):
    lbl_cls, inp_cls, cls = map(stringify,(lbl_cls, inp_cls, cls))
    if label:
        label = Label(cls='uk-form-label' + lbl_cls)(label)
        if id: label.fr = id
    res = Uk_select(cls=inp_cls, uk_cloak=True, **kwargs)(*options)
    if id: res.id = id
    return Div(cls=cls)(label, res)

# %% ../nbs/01_components.ipynb 35
class UkButtonT(VEnum):
    default = 'default'
    primary = 'primary'
    secondary = 'secondary'
    danger = 'danger'
    ghost = 'ghost'
    text = 'text'
    link = 'link'

# %% ../nbs/01_components.ipynb 36
def UkDropdownButton(label, # Shown on the button
                     options, # list of tuples that contain what you want listed
                     btn_cls=UkButtonT.default, # Button class
                     cls=() # parent div class
                     ):
    btn_cls, cls = map(stringify,(btn_cls, cls))
    btn = Button(type='button', cls='uk-button ' + btn_cls)(label, Span(uk_icon='icon: triangle-down'))
    dd_opts = [Li(A(href="#demo", cls='uk-drop-close',uk_toggle=True, role="button")(Div(o))) for o in options]
    dd = Div(uk_drop='mode: click; pos: bottom-right', cls='uk-dropdown uk-drop')(Ul(cls='uk-dropdown-nav')(*([Li(cls='uk-nav-divider')] + dd_opts)))
    return Div(cls=cls)(Div(cls='flex items-center space-x-4')(btn, dd))

# %% ../nbs/01_components.ipynb 38
def UkButton(*c, 
            cls=UkButtonT.default, # Use UkButtonT or styles 
            **kwargs):    
    return Button(cls='uk-button ' + stringify(cls), **kwargs)(*c)

# %% ../nbs/01_components.ipynb 39
def UkGenericComponent(component_fn, *c, cls=(), **kwargs):
        res = component_fn(**kwargs)(*c)
        if cls: res.attrs['class'] += ' ' + cls
        return res

UkH1 = partial(UkGenericComponent, partial(H1,cls='uk-h1'))
UkH2 = partial(UkGenericComponent, partial(H2,cls='uk-h2'))
UkH3 = partial(UkGenericComponent, partial(H3,cls='uk-h3'))
UkH4 = partial(UkGenericComponent, partial(H4,cls='uk-h4'))
UkH5 = partial(UkGenericComponent, partial(H5,cls='uk-h5'))
UkH6 = partial(UkGenericComponent, partial(H6,cls='uk-h6'))


# %% ../nbs/01_components.ipynb 41
def UkHSplit(*c, cls=(), line_cls=(), text_cls=()):
    cls, line_cls, text_cls = map(stringify,(cls, line_cls, text_cls))
    return Div(cls='relative ' + cls)(
        Div(cls="absolute inset-0 flex items-center " + line_cls)(Span(cls="w-full border-t border-border")),
        Div(cls="relative flex justify-center " + text_cls)(Span(cls="bg-background px-2 ")(*c)))

# %% ../nbs/01_components.ipynb 43
def Card(*c, # Components that go in the body
        header=None, # Components that go in the header
        footer=None,  # Components that go in the footer
        body_cls='space-y-6', # classes for the body
        header_cls=(), # classes for the header
        footer_cls=(), # classes for the footer
        cls=(), #class for outermost component
        **kwargs # classes that for the card itself
        ):
    header_cls, footer_cls, body_cls, cls = map(stringify, (header_cls, footer_cls, body_cls, cls))
    res = []
    if header: res += [Div(cls='uk-card-header ' + header_cls)(header),]
    res += [Div(cls='uk-card-body ' + body_cls)(*c),]
    if footer: res += [Div(cls='uk-card-footer ' + footer_cls)(footer),]
    return Div(cls='uk-card '+cls, **kwargs)(*res)
