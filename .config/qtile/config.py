
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os
import subprocess
from core.utils import get_theme
from core.widgets import workspaces, powerline
mod = "mod4"
# terminal = guess_terminal()
BAR_FONT = 'Iosevka Nerd Font'
terminal = "kitty"
colors = get_theme('dracula')



@hook.subscribe.startup_once
def autostart():
	""" Autostarting neccessary apps. """
	home = os.path.expanduser('~/.config/qtile/autostart.sh')
	subprocess.call([home])

autostart()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, 'shift'], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    # Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    Key([mod], "d", 
        # lazy.spawn('dmenu_run -b -i -fn "Iosevka Nerd Font" -p "Select File: " -nb "#282a36" -nf "#f8f8f2" -sf "#44475a" -sb "#bd93f9"'),
        lazy.spawn('rofi -show drun'),
        desc="Running Old School Dmenu"
    ),
    Key([mod, "shift"], "s", 
        # lazy.spawn('dmenu_run -b -i -fn "Iosevka Nerd Font" -p "Select File: " -nb "#282a36" -nf "#f8f8f2" -sf "#44475a" -sb "#bd93f9"'),
        lazy.spawn('flameshot full --path /home/vivekascoder/Pictures'),
        desc="Taking screenshot of full monitor"
    )
]

# groups = [Group(i) for i in "123456789"]
groups = [Group(i) for i in [
    "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ",
]]

# for i in groups:
#     keys.extend([
#         # mod1 + letter of group = switch to group
#         Key([mod], i.name, lazy.group[i.name].toscreen(),
#             desc="Switch to group {}".format(i.name)),

#         # mod1 + shift + letter of group = switch to & move focused window to group
#         Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#             desc="Switch to & move focused window to group {}".format(i.name)),
#         # Or, use below if you prefer not to switch to that group.
#         # # mod1 + shift + letter of group = move focused window to group
#         # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#         #     desc="move focused window to group {}".format(i.name)),
#     ])

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layouts = [
    layout.Columns(
        border_focus = colors['purple'],
        border_width = 3,
        border_normal = colors['background-alt'],
        border_focus_stack=colors['purple'], 
        margin=10
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=BAR_FONT,
    fontsize=18,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.CurrentLayoutIcon(background=colors['background']),
                # widget.GroupBox(
                # 	font = BAR_FONT
                # ),
                *workspaces(),
                widget.Prompt(),
                # widget.WindowName(
                # 	font = BAR_FONT,,,,,
                # ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                powerline(fg='purple', bg='background'),
                widget.Systray(
                    background = colors['purple'],
                    foreground = colors['green'],
                    padding = 10

                ),
                powerline(fg='green', bg='purple'),
                widget.Volume(
                    background = colors['green'],
                    foreground = colors['background'],
                    padding = 10,
                    fmt = '{}  ﰝ'
                    # emoji = True
                ),
                powerline(fg='orange', bg='green'),
                widget.Clock(
                	format=' %Y-%m-%d %a %I:%M %p',
                	font = BAR_FONT,
                	icon_size = '5',
                    background = colors['orange'],
                    foreground = colors['background'],
                    padding = 10,
                ),
                powerline(fg='cyan', bg='orange'),
                widget.Battery(
                	charge_char = ' ',
                	full_char = '',
                	discharge_char = '',
                	format = "{char} {percent:2.0%}",
                    background = colors['cyan'],
                    foreground = colors['background'],
                    padding = 10,
                ),
                powerline(fg='red', bg='cyan'),
                widget.QuickExit(
                	default_text = '📛',
                    background = colors['red'],
                    padding = 10,
                ),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='copyq')
],
border_width = 3,
border_focus = colors['purple'],
border_normal = colors['background-alt'])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
