"""Utilities for building the docs page that don't belong anywhere else"""


__all__ = ['hjs', 'HShow', 'create_server']

from fasthtml.common import *
from monsterui.all import *
from fasthtml.jupyter import *
from collections.abc import Callable
import inspect
import ast
def get_last_statement(code): return ast.unparse(ast.parse(code).body[-1])
import json
from pathlib import Path


hjs = (
    # Core highlight.js and copy plugin
    Script(src='https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js'),
    Script(src='https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/languages/python.min.js'),
    Script(src='https://cdn.jsdelivr.net/gh/arronhunt/highlightjs-copy/dist/highlightjs-copy.min.js'),
    
    # Themes and styles
    Link(rel='stylesheet', href='https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/styles/atom-one-dark.css', id='hljs-dark'),
    Link(rel='stylesheet', href='https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/styles/atom-one-light.css', id='hljs-light'),
    Link(rel='stylesheet', href='https://cdn.jsdelivr.net/gh/arronhunt/highlightjs-copy/dist/highlightjs-copy.min.css'),

    
    # Initialization script
    Script('''
        // Initialize highlight.js with copy plugin
        hljs.addPlugin(new CopyButtonPlugin());
        hljs.configure({
            cssSelector: 'pre code',
            languages: ['python'],
            ignoreUnescapedHTML: true
        });

        // Theme switching logic
        function updateTheme() {
            const isDark = document.documentElement.classList.contains('dark');
            document.getElementById('hljs-dark').disabled = !isDark;
            document.getElementById('hljs-light').disabled = isDark;
        }

        // Watch for theme changes
        new MutationObserver(mutations => 
            mutations.forEach(m => m.target.tagName === 'HTML' && 
                m.attributeName === 'class' && updateTheme())
        ).observe(document.documentElement, { attributes: true });

        // Initial setup
        updateTheme();
        htmx.onLoad(hljs.highlightAll);
    ''', type='module')
)
def create_flippable_card(content, source_code, extra_cls=None):
    "Creates a card that flips between content and source code"
    _id = 'f'+str(unqid())
    _card = Card(
        Button(
            DivFullySpaced(UkIcon('corner-down-right', 20, 20, 3),"See Source"), 
            uk_toggle=f"target: #{_id}", id=_id, cls=ButtonT.primary),
        Button(
            DivFullySpaced(UkIcon('corner-down-right', 20, 20, 3),"See Output"), 
            uk_toggle=f"target: #{_id}", id=_id, cls=ButtonT.primary, hidden=True),
        Div(content, id=_id),
        Div(Pre(Code(source_code, cls="hljs language-python")), id=_id, hidden=True),
        cls='my-8')
    return Div(_card, cls=extra_cls) if extra_cls else _card

def fn2code_string(fn: Callable) -> tuple: return fn(), inspect.getsource(fn)


def render_nb(path):
    "Renders a Jupyter notebook with markdown cells and flippable code cards"
    namespace = globals().copy()
    # Read and parse the notebook
    nb_content = json.loads(Path(path).read_text())
    cells = nb_content['cells']
    
    # Convert cells to appropriate HTML elements
    rendered_cells = []
    for cell in cells:
        if cell['cell_type'] == 'markdown':
            # Combine all markdown lines and render
            md_content = ''.join(cell['source'])
            rendered_cells.append(render_md(md_content))
        elif cell['cell_type'] == 'code':
            # Skip empty code cells
            if not ''.join(cell['source']).strip(): continue
            # Create flippable card for code
            code_content = ''.join(cell['source'])
            exec(code_content, namespace)
            result = eval(get_last_statement(code_content), namespace)
            
            rendered_cells.append(create_flippable_card(result, code_content))

    # Return all cells wrapped in a container with vertical spacing
    return Container(cls='space-y-4')(*rendered_cells)
