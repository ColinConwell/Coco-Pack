# >>> ANSI Color Codes >>>

# Color code reset
RESET="\[\033[0m\]"

# Base color codes
BLACK="\[\033[0;30m\]"
RED="\[\033[0;31m\]"
GREEN="\[\033[0;32m\]"
YELLOW="\[\033[0;33m\]"
BLUE="\[\033[0;34m\]"
MAGENTA="\[\033[0;35m\]"
CYAN="\[\033[0;36m\]"
WHITE="\[\033[0;37m\]"

# Bold color codes
BOLD_BLACK="\[\033[1;30m\]"
BOLD_RED="\[\033[1;31m\]"
BOLD_GREEN="\[\033[1;32m\]"
BOLD_YELLOW="\[\033[1;33m\]"
BOLD_BLUE="\[\033[1;34m\]"
BOLD_MAGENTA="\[\033[1;35m\]"
BOLD_CYAN="\[\033[1;36m\]"
BOLD_WHITE="\[\033[1;37m\]"

# Background color codes
BG_BLACK="\[\033[40m\]"
BG_RED="\[\033[41m\]"
BG_GREEN="\[\033[42m\]"
BG_YELLOW="\[\033[43m\]"
BG_BLUE="\[\033[44m\]"
BG_MAGENTA="\[\033[45m\]"
BG_CYAN="\[\033[46m\]"
BG_WHITE="\[\033[47m\]"

# <<< ANSI Color Codes <<<

# >>> Color Function >>>
color_wrap() {
    local color="$1"
    local text="$2"
    echo "${!color}${text}${RESET}"
}
# <<< Color Function <<<
