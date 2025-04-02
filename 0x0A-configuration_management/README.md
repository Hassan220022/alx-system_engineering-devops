# 0x0A. Configuration management

## Background Context
This project is inspired by a real-world incident at SlideShare where an auto-remediation tool called Skynet accidentally terminated 75% of their document conversion infrastructure servers. The incident highlighted the importance of proper configuration management and automation tools like Puppet, which helped restore the infrastructure in under an hour.

## Resources
- [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
- [Puppet resource type: file](https://puppet.com/docs/puppet/5.5/types/file.html)
- [Puppet's Declarative Language: Modeling Instead of Scripting](https://puppet.com/blog/puppets-declarative-language-modeling-instead-of-scripting)
- [Puppet lint](https://github.com/rodjek/puppet-lint)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

## Requirements
### General
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Puppet manifests must run without error
- Puppet manifests first line must be a comment explaining what the manifest is about
- Puppet manifests files must end with the extension .pp

### Versioning
- Ubuntu 20.04 VM should have Puppet 5.5 preinstalled
- No need to upgrade versions as this project focuses on basic syntax

## Tasks

### 0. Create a file
Using Puppet, create a file in /tmp with the following requirements:
- File path: /tmp/school
- File permission: 0744
- File owner: www-data
- File group: www-data
- File content: "I love Puppet"

### 1. Install a package
Using Puppet, install Flask from pip3 with the following requirements:
- Install Flask
- Version must be 2.1.0

### 2. Execute a command
Using Puppet, create a manifest that kills a process named killmenow with the following requirements:
- Must use the exec Puppet resource
- Must use pkill

## Installation Instructions
To set up the environment:

```bash
# Install Ruby
apt-get install -y ruby=1:2.7+1 --allow-downgrades

# Install required Ruby packages
apt-get install -y ruby-augeas
apt-get install -y ruby-shadow

# Install Puppet
apt-get install -y puppet

# Install puppet-lint
gem install puppet-lint
```

## Usage
To apply any of the manifests:

```bash
puppet apply <filename>.pp
```

For example:
```bash
puppet apply 0-create_a_file.pp
``` 