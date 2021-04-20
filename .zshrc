# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/home/vivekascoder/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
# ZSH_THEME="robbyrussell"
# ZSH_THEME="cloud"
# ZSH_THEME="bira"
# ZSH_THEME="darkblood"
# ZSH_THEME="gnzh"
# ZSH_THEME="half-life"
ZSH_THEME="intheloop"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# Caution: this setting can cause issues with multiline prompts (zsh 5.7.1 and newer seem to work)
# See https://github.com/ohmyzsh/ohmyzsh/issues/5765
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
    git
    zsh-syntax-highlighting
	zsh-autosuggestions
)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
#
#

alias issh="kitty +kitten ssh"

## Editing Goes here...
export PATH="$PATH:$HOME/.local/bin"
export PATH="$PATH:$HOME/bin"
export vimrc="$HOME/.config/nvim/init.vim"
export zshrc="$HOME/.zshrc"
export GEM_HOME="$HOME/.local/gems"
export PATH="$PATH:$HOME/.local/gems/bin"
export ROCKET_HOME="$HOME/.local"
NPM_PACKAGES="${HOME}/.npm-packages"

export PATH="$PATH:$NPM_PACKAGES/bin"
export PATH="$PATH:$HOME/.cargo/bin"

# Preserve MANPATH if you already defined it somewhere in your config.
# Otherwise, fall back to `manpath` so we can inherit from `/etc/manpath`.
export MANPATH="${MANPATH-$(manpath)}:$NPM_PACKAGES/share/man"
alias ssh-dev="issh vivekascoder@divcorn.centralindia.cloudapp.azure.com -L 3000:localhost:3000 -L 8080:localhost:8080 -L 8000:localhost:8000"
alias dmenu='dmenu -i -l 10 -fn "Iosevka Nerd Font" -p "Select File: " -nb "#282a36" -nf "#f8f8f2" -sf "#44475a" -sb "#bd93f9" '
# Krunker: Hello@321
# alias s="shutdown -P now"
alias pip="pip3"
alias python="python3"
alias icat='kitty +kitten icat'
export userchrome='/home/vivekascoder/.mozilla/firefox/dsx49yor.default-release-1-1618054765012/chrome'
alias em='xrandr --output HDMI-1 --mode "1920x1080" --right-of eDP-1'
alias dm="xrandr --output HDMI-1 --off"
alias s='vlc -I ncurses --no-video ~/Music 2> /dev/null'
alias walme='cat /home/vivekascoder/.config/nitrogen/bg-saved.cfg | grep file | cut -d= -f2 | xargs wal -i'
alias config='/usr/bin/git --git-dir=/home/vivekascoder/dotfiles/ --work-tree=/home/vivekascoder'
alias getgif='ffmpeg -i qtile.mp4 -ss 00:00:00.000 -pix_fmt rgb24 -r 10 -s 960x540 -t 00:00:10.000 output.gif'
