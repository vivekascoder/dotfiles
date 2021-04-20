

from libqtile import widget
from core.utils import get_theme

colors = get_theme('dracula')

def base(fg='foreground', bg='background'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='foreground', bg='background', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="foreground", bg="background", right=False, **kwargs):
    return widget.TextBox(
        **base(fg, bg),
        text= "" if not right else "", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2,
        **kwargs
    )

def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='foreground', bg='background'),
            margin_y=3,
            margin_x=0,
            padding_y=4,
            padding_x=0,
            borderwidth=1,
            active=colors['purple'],
            inactive=colors['foreground'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['red'],
            this_current_screen_border=colors['background-alt'],
            this_screen_border=colors['red'],
            other_current_screen_border=colors['foreground'],
            other_screen_border=colors['red'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(
        	**base(fg='foreground'), 
        	fontsize=14, 
        	padding=5,
        	max_chars = 30,
        	fmt = "  {}"
        ),
        separator(),
    ]


