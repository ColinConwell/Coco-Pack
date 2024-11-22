import sys
import argparse
from pathlib import Path
import subprocess
import os

SHELL_COMMANDS = {
    'ezshell': 'ezshell.sh',
    'prompt': 'prompt.sh',
    'colorcode': 'colorcode.sh',
    'jekyll': 'helpers/jekyll.sh',
}

def get_script_path(script_name):
    """Get the full path to a shell script"""
    package_dir = Path(__file__).parent.parent.parent.parent
    return package_dir / 'shell' / script_name

def print_usage():
    """Print usage information"""
    print("Usage: cocopack <command> [args...]")
    print("\nAvailable commands:")
    for cmd in SHELL_COMMANDS:
        print(f"  {cmd}")
    print("\nFor command-specific help:")
    print("  cocopack <command> --help")

def source_shell_script(script_path, *args):
    """Source a shell script and run a command"""
    cmd = f"source {script_path}"
    if args:
        cmd += f" && {' '.join(args)}"
    return os.system(cmd)

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help']:
        print_usage()
        sys.exit(0)

    command = sys.argv[1]
    if command not in SHELL_COMMANDS:
        print(f"Unknown command: {command}")
        print_usage()
        sys.exit(1)

    script_path = get_script_path(SHELL_COMMANDS[command])
    if not script_path.exists():
        print(f"Script not found: {script_path}")
        sys.exit(1)

    # Pass remaining arguments to the script
    args = sys.argv[2:]
    exit_code = source_shell_script(script_path, *args)
    sys.exit(exit_code >> 8)  # Convert shell exit code to Python exit code

if __name__ == '__main__':
    main() 