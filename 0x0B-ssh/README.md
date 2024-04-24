# SSH Configuration and Management

This project is part of the ALX Software Engineering curriculum and focuses on understanding and managing SSH (Secure Shell) for remote server management.

## Project Details

- **Course**: 0x0B. SSH
- **Weight**: 1
- **Project Duration**: April 19, 2024, to April 25, 2024
- **Environment**: Ubuntu 20.04 LTS

## Background Context

As part of this project, students are attributed an Ubuntu server located in a data center. Unlike previous levels, the connection to this server will be established using SSH with RSA key authentication, enhancing security and understanding of remote server management.

## Learning Objectives

By the end of this project, students are expected to demonstrate knowledge on:

- The role and operation of servers.
- SSH's architecture and how it facilitates secure remote management.
- Generating and using RSA key pairs for authentication.
- Writing Bash scripts that automate the login process without a password.
- Configuring SSH client and server settings for enhanced security.

## Requirements

- **Coding Standards**: Scripts must be written in Bash and adhere to `#!/usr/bin/env bash` with a description comment.
- **Tools**: vi, vim, emacs
- **Scripts**: Must be executable and end with a new line.

## Resources

- Understanding server hardware and management.
- In-depth SSH tutorials and configuration guides.
- Public Key Authentication and SSH internals.

## Tasks

### Mandatory

1. **Use a Private Key**:

   - Script that connects to a server using a specified private RSA key.

2. **Create an SSH Key Pair**:

   - Script to generate a 4096-bit RSA key pair with a passphrase.

3. **Client Configuration File**:

   - Customize the SSH client to prefer key authentication and refuse password authentication.

4. **Let Me In!**:
   - Add a given public SSH key to the server to allow connections from the specified user.

### Optional

- Advanced tasks that delve deeper into SSH security measures and configurations.

## Usage

Each script can be run from a Unix shell. Permissions may need to be adjusted using `chmod +x <script_name>`.

## Contributions

This project is an individual assignment under ALX's strict anti-plagiarism policy and does not accept contributions.

## Authors

- **[Hassan Mikawi](https://github.com/Hassan220022)** - Complete the project independently to comply with ALX's honor code.

## Acknowledgments

- ALX Africa for the educational opportunity.
- Peer sessions and code reviews.
- External resources and publications that provided in-depth SSH insights.
