"""FrankenUI Cards Example"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../ex_nbs/02_cards.ipynb.

# %% auto 0
__all__ = ['Left1', 'Card1Svg', 'Card2Svg', 'AppleSvg', 'Left2', 'area_opts', 'severity_opts', 'Right1', 'franken_desc', 'Right2',
           'Right3', 'team_members', 'options', 'body', 'Middle1', 'access_roles', 'Middle2', 'Middle3',
           'section_content', 'Middle4', 'cards_homepage', 'page']

# %% ../ex_nbs/02_cards.ipynb 2
from fasthtml.common import *
from fh_frankenui import *
from fasthtml.svg import *
import calendar

# %% ../ex_nbs/02_cards.ipynb 7
Left1 = Card(Grid(UkButton(UkIcon('github',cls='uk-margin-small-right'),'Github'),
                  UkButton(UkIcon('google',cls='uk-margin-small-right'),'Google'),
                  cols=2,gap=6),
            UkHSplit("OR CONTINUE WITH", text_cls = (TextB.sz_xsmall, TextB.cl_muted)),
            UkInput('Email',    'email',   placeholder='m@example.com'),
            UkInput('Password', 'Password',placeholder='Password',     type='Password'),
            header=(UkH3('Create an account'),P(cls=TextT.muted_sm)('Enter your email below to create your account')),
            footer=UkButton(cls=(UkButtonT.primary,'w-full'))('Create Account'),
            body_cls='space-y-4 py-0')

# %% ../ex_nbs/02_cards.ipynb 9
Card1Svg = Svg(viewBox="0 0 24 24", fill="none", stroke="currentColor", stroke_linecap="round", stroke_linejoin="round", stroke_width="2", cls="mb-3 h-6 w-6")(Rect(width="20", height="14", x="2", y="5", rx="2"),Path(d="M2 10h20"))
Card2Svg = Svg(role="img", viewBox="0 0 24 24", cls="mb-3 h-6 w-6")(Path(d="M7.076 21.337H2.47a.641.641 0 0 1-.633-.74L4.944.901C5.026.382 5.474 0 5.998 0h7.46c2.57 0 4.578.543 5.69 1.81 1.01 1.15 1.304 2.42 1.012 4.287-.023.143-.047.288-.077.437-.983 5.05-4.349 6.797-8.647 6.797h-2.19c-.524 0-.968.382-1.05.9l-1.12 7.106zm14.146-14.42a3.35 3.35 0 0 0-.607-.541c-.013.076-.026.175-.041.254-.93 4.778-4.005 7.201-9.138 7.201h-2.19a.563.563 0 0 0-.556.479l-1.187 7.527h-.506l-.24 1.516a.56.56 0 0 0 .554.647h3.882c.46 0 .85-.334.922-.788.06-.26.76-4.852.816-5.09a.932.932 0 0 1 .923-.788h.58c3.76 0 6.705-1.528 7.565-5.946.36-1.847.174-3.388-.777-4.471z", fill="currentColor")),
AppleSvg = Svg(role="img", viewBox="0 0 24 24", cls="mb-3 h-6 w-6")(Path(d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701", fill="currentColor"))

# %% ../ex_nbs/02_cards.ipynb 10
Left2 = Card(
    Grid(
        UkButton(CenteredDiv(Card1Svg,"Card"), cls='h-20 w-full border-2 border-primary'),
        UkButton(CenteredDiv(Card2Svg, "Card"), cls='h-20 w-full'),
        UkButton(CenteredDiv(AppleSvg, "Apple"), cls='h-20 w-full'),
        cols=3,gap=4),
    Div(cls='space-y-4')(
    UkInput('Name', 'name',placeholder='m@example.com'),
    UkInput('Card Number', 'card_number',placeholder='m@example.com'),
    Grid(UkSelect(*Options(*calendar.month_name[1:],0),label='Expires',id='expire_month'),
         UkSelect(*Options(*range(2024,2030),0),       label='Year',   id='expire_year'),
         UkInput('CVV', 'cvv',placeholder='CVV', cls=""),
         cols=3,gap=4)),
    header=(UkH3('Payment Method'),P(cls=TextT.muted_sm)('Add a new payment method to your account.')))

# %% ../ex_nbs/02_cards.ipynb 12
area_opts = ('Team','Billing','Account','Deployment','Support')
severity_opts = ('Severity 1 (Highest)', 'Severity 2', 'Severity 3', 'Severity 4 (Lowest)')
Right1 = Card(
    Grid(UkSelect(*Options(*area_opts),    label='Area',    id='area'),
         UkSelect(*Options(*severity_opts),label='Severity',id='area'),
         cols=2,gap=2),
    UkInput(    label='Subject',    placeholder='I need help with'),
    UkTextArea( label='Description',placeholder='Please include all information relevant to your issue'),
    UkFormLabel(label="Tags",state="danger", value="Spam,Invalid"),
    header=(H3('Report an issue'),P(cls=TextT.muted_sm)('What area are you having problems with')),
    footer = FullySpacedDiv(UkButton(cls=UkButtonT.ghost)('Cancel'),UkButton(cls=UkButtonT.primary)('Submit')))


# %% ../ex_nbs/02_cards.ipynb 14
franken_desc ="HTML-first, framework-agnostic, beautifully designed components that you can truly copy and paste into your site. Accessible. Customizable. Open Source."
Right2 = Card(UkH4("franken/ui"),
              P(cls=TextT.muted_sm)(franken_desc),
              Div(cls=('flex','gap-x-4',TextT.muted_sm))(
                Div(cls='flex items-center')("TypeScript"),
                Div(cls='flex items-center')(UkIcon('star'),"20k"),"Updated April 2023"))

# %% ../ex_nbs/02_cards.ipynb 16
Right3 = Card(
    UkSwitch(label = Div(UkH5('Strictly Necessary'),P(cls=(TextT.muted_sm,TextB.wt_normal))('These cookies are essential in order to use the website and use its features.')),
                cls='flex items-center justify-between gap-2'),
    UkSwitch(label = Div(UkH5('Functional Cookies'),P(cls=(TextT.muted_sm,TextB.wt_normal))('These cookies allow the website to provide personalized functionality.')),
                cls='flex items-center justify-between gap-2'),
    UkSwitch(label = Div(UkH5('Performance Cookies'),P(cls=(TextT.muted_sm,TextB.wt_normal))('These cookies help to improve the performance of the website.')),
                cls='flex items-center justify-between gap-2'),
    header=(UkH4('Cookie Settings'),P(cls=(TextT.muted_sm, 'mt-1.5'))('Manage your cookie settings here.')),
    footer=UkButton(cls='uk-button-primary w-full')('Save Preferences'),)

# %% ../ex_nbs/02_cards.ipynb 18
team_members = [{"name": "Sofia Davis", "email": "m@example.com", "role": "Owner"},{"name": "Jackson Lee", "email": "p@example.com", "role": "Member"},]

options = [
    A(Div(Div('Viewer'), Div('Can view and comment.', cls=TextT.muted_sm))),
    A(Div(Div('Developer'), Div('Can view, comment and edit.', cls=TextT.muted_sm))),
    A(Div(Div('Billing'), Div('Can view, comment and manage billing.', cls=TextT.muted_sm))),
    A(Div(Div('Owner'), Div('Admin-level access to all resources.', cls=TextT.muted_sm)))
]

body = [Div(cls='flex items-center space-x-4')(
        DiceBearAvatar(member['name'], 10,10),
        Div(cls='flex-1')(
            P(member['name'], cls='text-sm font-medium leading-none'),
            P(member['email'], cls=TextT.muted_sm)
        ),
        UkDropdownButton([options], label=member['role']),
    ) for member in team_members]

Middle1 = Card(*body,
        header = (UkH4('Team Members'),Div('Invite your team members to collaborate.', cls=('mt-1.5', TextT.muted_sm))),)

# %% ../ex_nbs/02_cards.ipynb 20
access_roles = ("Read and write access", "Read-only access")
team_members = [{"name": "Olivia Martin", "email": "m@example.com", "role": "Read and write access"},
                {"name": "Isabella Nguyen", "email": "b@example.com", "role": "Read-only access"},
                {"name": "Sofia Davis", "email": "p@example.com", "role": "Read-only access"}]

# %% ../ex_nbs/02_cards.ipynb 21
Middle2 = Card(
    Div(cls='flex gap-x-2')(
        UkInput(value='http://example.com/link/to/document',cls='flex-1'),
        UkButton('Copy link')),
    Div(cls='uk-divider-icon my-4'),
    H4(cls='text-sm font-medium')('People with access'),
    *[Div(cls='flex items-center space-x-4')(
        DiceBearAvatar(member['name'], 10,10),
        Div(cls='flex-1')(
            P(member['name'], cls='text-sm font-medium leading-none'),
            P(member['email'], cls=TextT.muted_sm)),
        UkSelect(*Options(*access_roles, selected_idx=access_roles.index(member['role'])))) for member in team_members],
    header = (UkH4('Share this document'),Div('Anyone with the link can view this document.', cls=('mt-1.5',TextT.muted_sm))))

# %% ../ex_nbs/02_cards.ipynb 23
Middle3 = Card(UkButton('Jan 20, 2024 - Feb 09, 2024'))

# %% ../ex_nbs/02_cards.ipynb 25
section_content =(('bell','Everything',"Email digest, mentions & all activity."),
                  ('user',"Available","Only mentions and comments"),
                  ('ban',"Ignoring","Turn of all notifications"))

# %% ../ex_nbs/02_cards.ipynb 26
Middle4 = Card(
    Ul(cls="uk-nav uk-nav-secondary")
    (*[Li(cls='-mx-1')(A(Div(cls="flex gap-x-4")(Div(uk_icon=icon),Div(cls='flex-1')(P(name),P(cls=TextT.muted_sm)(desc)))))
            for icon, name, desc in section_content]),
    header = (UkH4('Notification'),Div('Choose what you want to be notified about.', cls=('mt-1.5', TextT.muted_sm))),
    body_cls='pt-0')

# %% ../ex_nbs/02_cards.ipynb 28
def page():
    return Title("Custom"),Div(cls='uk-child-width-1-3@l uk-child-width-1-2@m', uk_grid=True)(
            Div(cls='space-y-6')(map(Div,(Left1,Left2))),
            Div(cls='space-y-6')(map(Div,(Middle1,Middle2,Middle3,Middle4))),
            Div(cls='space-y-6')(map(Div,(Right1,Right2, Right3))))

# %% ../ex_nbs/02_cards.ipynb 29
cards_homepage = page()
