# AUTOGENERATED! DO NOT EDIT! File to edit: ../ex_nbs/05_music.ipynb.

# %% auto 0
__all__ = ['music_dd_data', 'file_dd_data', 'edit_dd_data', 'view_dd_data', 'account_dd_data', 'music_headers', 'discover',
           'library', 'playlist', 'listen_now_albums', 'made_for_you_albums', 'music_content', 'tabs', 'sb', 'sidebar',
           'music_homepage', 'wrap_in_a', 'AlbumImg', 'AlbumFooter', 'Album', 'create_album_grid', 'podcast_tab',
           'LAlignedIconTxts', 'page']

# %% ../ex_nbs/05_music.ipynb
from fasthtml.common import *
from fasthtml.components import Uk
from fh_frankenui import *
from fasthtml.components import Uk_icon
from fasthtml.svg import *
from fh_matplotlib import matplotlib2fasthtml
import numpy as np
from pathlib import Path
import matplotlib.pylab as plt

# %% ../ex_nbs/05_music.ipynb
music_dd_data = [SpacedPPs("About Music",("Preferences", "⌘")),
                 SpacedPPs(("Hide Music", "⌘H"),("Hide Others", "⇧⌘H"),("Quit Music", "⌘Q"))]

file_dd_data = [SpacedPPs("New" ,("Open Stream URL", "⌘U"),("Close Window", "⌘W")),
                SpacedPPs("Library",("Import", "⌘O"),("Burn Playlist to Disc", )),
                SpacedPPs(("Show in Finder", "⇧⌘R"),"Convert"),
                SpacedPPs("Page Setup","Print")]

edit_dd_data = [SpacedPPs(("Undo", "⌘Z"),("Redo", "⇧⌘Z")), SpacedPPs(("Cut", "⌘X"),("Copy", "⌘C"),("Paste", "⌘V")),
                SpacedPPs(("Select All", "⌘A"),("Deselect All", "⇧⌘A")),
                SpacedTxtIcon('Smart Dictation','microphone',0.5), SpacedTxtIcon("Emojis & Symbols",'world',0.5)]

view_dd_data = [SpacedPPs("Show Playing Next", "Show Lyrics", "Show Status Bar", "Hide Sidebar", "Enter Full Screen")]

account_dd_data = [Span("Switch Account", cls="ml-6"), [SpacedPP("Andy"), LAlignedTxtIcon("Benoit", 'plus-circle', 0.5, icon_right=False), SpacedPP("Luis")],
                   SpacedPPs("Manage Family"), SpacedPPs("Add Account")]

# %% ../ex_nbs/05_music.ipynb
def wrap_in_a(item, has_header=False):
    if isinstance(item, (list, tuple)): return [wrap_in_a(o) for o in item]
    else: return A(item)

# %% ../ex_nbs/05_music.ipynb
music_headers = UkNavbar(
    lnav=(
        UkNavbarDropdown(*wrap_in_a(music_dd_data), label='Music'),
        UkNavbarDropdown(*wrap_in_a(file_dd_data), label='File'),
        UkNavbarDropdown(*wrap_in_a(edit_dd_data), label='Edit'),
        UkNavbarDropdown(*wrap_in_a(view_dd_data), label='View'),
        UkNavbarDropdown(*wrap_in_a(account_dd_data), label='Account')),
    cls='p-2')

# %% ../ex_nbs/05_music.ipynb
_fn = lambda x: A(role='button')(LAlignedTxtIcon(*tuplify(x),icon_right=False, cls='space-x-4'))
discover = (UkH4("Discover"), *map(_fn, (("Listen Now", "play-circle"), ("Browse", 'thumbnails'), ("Radio", "rss"))))
library = (UkH4("Library"), *map(_fn, (("Playlists", "play-circle"), ("Songs", "bell"), ("Made for You", "user"),("Artists", "users"),("Albums", "bookmark"))))
playlist = (UkH4("Playlist"), *map(_fn, ("Recently Added", "Recently Played", "Top Songs", "Top Albums", "Top Artists", 
                                         "Logic Discography","Bedtime Beats", "I miss Y2K Pop")))

# %% ../ex_nbs/05_music.ipynb
def AlbumImg(url):
    return Div(cls="overflow-hidden rounded-md")(Img(cls="transition-transform duration-200 hover:scale-105", src=url))

def AlbumFooter(title, artist):
    return Div(cls='space-y-1')(P(title,cls=TextB.wt_bold),P(artist,cls=TextB.cl_muted))

def Album(url,title,artist):
    return Div(AlbumImg(url),AlbumFooter(title,artist))

# %% ../ex_nbs/05_music.ipynb
listen_now_albums = (("Roar", "Catty Perry"), ("Feline on a Prayer", "Cat Jovi"),("Fur Elise", "Ludwig van Beethovpurr"),("Purrple Rain", "Prince's Cat"))

made_for_you_albums = [("Like a Feline", "Catdonna"),("Livin' La Vida Purrda", "Ricky Catin"),("Meow Meow Rocket", "Elton Cat"),
        ("Rolling in the Purr", "Catdelle",),("Purrs of Silence", "Cat Garfunkel"),("Meow Me Maybe", "Carly Rae Purrsen"),]
    

# %% ../ex_nbs/05_music.ipynb
def create_album_grid(albums, cols=4):  
    return Grid(*[Div(cls="uk-grid-small")(
                Div(cls="overflow-hidden rounded-md")(
                    Img(cls="transition-transform duration-200 hover:scale-105", src=img_url, alt="")),
                Div(cls="space-y-1 text-sm")(
                    H3(album['title'], cls="font-medium leading-none"),
                    P(album['artist'], cls="text-xs text-muted-foreground"))) for album in albums],
                cols,gap=4)

# %% ../ex_nbs/05_music.ipynb
_album = lambda t,a: Album('https://ucarecdn.com/e5607eaf-2b2a-43b9-ada9-330824b6afd7/music1.webp',t,a)

music_content = (Div(UkH3("Listen Now"), cls="mt-6 space-y-1"),
                    P("Top picks for you. Updated daily.",cls=TextT.muted_sm),
                    UkHLine(),
                    Grid(*[_album(t,a) for t,a in listen_now_albums], cols=4, cls=GridT.medium),
                    Div(UkH3("Made for You"), cls="mt-6 space-y-1"),
                    P("Your personal playlists. Updated daily.", cls=TextT.muted_sm),
                    UkHLine(),
                    Grid(*[_album(t,a) for t,a in made_for_you_albums], cols=6, cls=GridT.small))

# %% ../ex_nbs/05_music.ipynb
tabs = Ul(Li(A('Music', href='#'),cls='uk-active'),
    Li(A('Podcasts', href='#')),
    Li(A('Live', cls='opacity-50'), cls='uk-disabled'),
    uk_switcher='connect: #component-nav; animation: uk-animation-fade',
    cls='uk-tab-alt')

# %% ../ex_nbs/05_music.ipynb
def podcast_tab():
    return Div(
        Div(cls="space-y-3")(
            UkH3("New Episodes"),
            P("Your favorite podcasts. Updated daily.", cls=TextT.muted_sm)),
        Div(cls="my-4 h-[1px] w-full bg-border"),
        Div(cls="uk-placeholder flex h-[450px] items-center justify-center rounded-md",uk_placeholder=True)(
            Div(cls="text-center space-y-6")(
                UkIcon("microphone", 3),
                UkH4("No episodes added"),
                P("You have not added any podcasts. Add one below.", cls=TextT.muted_sm),
                UkButton("Add Podcast", cls=UkButtonT.primary))))

# %% ../ex_nbs/05_music.ipynb
def LAlignedIconTxts(ns, icns): return [Li(A(LAlignedIconTxt(n,i))) for n,i in zip(ns,icns)]

# %% ../ex_nbs/05_music.ipynb
sb = (Ul(cls='space-y-2')(
         Li(UkH3("Discover")), 
         *LAlignedIconTxts(["Listen Now", "Browse", "Radio"], ["play-circle", "thumbnails", "rss"])),
      Ul(cls='space-y-2')(
          Li(UkH3("Library")), 
          *LAlignedIconTxts(["Playlists", "Songs", "Made for You", "Artists", "Albums"], 
                           ["play-circle", "bell", "user", "users", "bookmark"])),
      Ul(cls='space-y-2')(
          Li(UkH3("Playlist")),
          *LAlignedIconTxts(["Recently Added", "Recently Played"], ["", ""]),)) 

# %% ../ex_nbs/05_music.ipynb
sidebar = UkSidebar(*sb)

# %% ../ex_nbs/05_music.ipynb
def page():
    return Div(music_headers,UkHSplit(),
        Grid(sidebar,
            Div(cls="col-span-4 border-l border-border")(
                Div(cls="px-8 py-6")(
                    Div(cls="flex items-center justify-between")(
                        Div(cls="max-w-80")(tabs),
                        UkButton(cls=UkButtonT.primary)(Span(cls="mr-2 size-4")(UkIcon('plus-circle', 0.8)),"Add music")),
                    Ul(id="component-nav", cls="uk-switcher")(
                        Li(*music_content),
                        Li(podcast_tab())))),
            cols=5))

# %% ../ex_nbs/05_music.ipynb
music_homepage = page()
