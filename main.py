import argparse
import os
import readline
import subprocess

# Set up command line argument parser
parser = argparse.ArgumentParser(description="A simple command line interface.")
parser.add_argument("-v", "--version", action="version", version="CLI v1.0")
args = parser.parse_args()

# Set up readline module for command history and editing
histfile = os.path.join(os.environ["HOME"], ".cli_history")
try:
    readline.read_history_file(histfile)
except FileNotFoundError:
    pass
readline.set_history_length(1000)
readline.parse_and_bind("tab: complete")

# Define shell commands to support
SUPPORTED_COMMANDS = ["cd", "ls", "pwd", "git", "ifconfig", "clear"]

# Main loop to read and execute user commands
while True:
    try:
        # Read user command from input
        command = input("> ")
        if command == "q":
            break
        
        # Save command to history file
        readline.write_history_file(histfile)
        
        # Split command into tokens
        tokens = command.split()
        
        # Handle empty command or comment (starting with #)
        if not tokens or tokens[0].startswith("#"):
            continue
        
        # Handle supported shell commands
        if tokens[0] in SUPPORTED_COMMANDS:
            if tokens[0] == "cd":
                os.chdir(tokens[1])
            elif tokens[0] == "git":
                subprocess.run(tokens)
            else:
                subprocess.run(tokens)
        
        # Handle other commands
        else:
            print(f"Unknown command: {command}")
    
    # Handle Ctrl-C interrupt
    except KeyboardInterrupt:
        print("^C")
        continue
    
    # Handle End-Of-File (EOF) interrupt
    except EOFError:
        print("Exiting CLI.")
        break
