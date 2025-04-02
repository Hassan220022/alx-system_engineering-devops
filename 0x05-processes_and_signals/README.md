# 0x05. Processes and Signals

This project covers the concepts of processes, PIDs, and signal handling in Bash.

## Learning Objectives
- What is a PID
- What is a process
- How to find a process' PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

## Requirements
- All scripts are written in Bash
- All scripts are exactly executable
- All scripts pass Shellcheck without any error
- The first line of all scripts is `#!/usr/bin/env bash`
- The second line of all scripts is a comment explaining what the script does

## Projects

- **0-what-is-my-pid**: Displays the script's own PID
- **1-list_your_processes**: Displays a list of currently running processes
- **2-show_your_bash_pid**: Shows lines containing the bash word from process list
- **3-show_your_bash_pid_made_easy**: Shows PID and process name containing "bash"
- **4-to_infinity_and_beyond**: Displays text indefinitely with a sleep
- **5-dont_stop_me_now**: Stops the 4-to_infinity_and_beyond process using kill
- **6-stop_me_if_you_can**: Stops the 4-to_infinity_and_beyond process without kill
- **7-highlander**: Displays text with signal handling
- **8-beheaded_process**: Kills the 7-highlander process

## Advanced Tasks
- **100-process_and_pid_file**: Creates a PID file and handles multiple signals
- **101-manage_my_process**: Init script to manage a background process
- **102-zombie.c**: C program that creates zombie processes 