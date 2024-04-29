# 0x0F. Load Balancer

![Load Balancer Diagram](image.png)

## Overview

This project focuses on the implementation of a load balancer using HAproxy to distribute incoming traffic between two web servers, thereby increasing redundancy and reliability in our web stack.

## Background Context

With the addition of two new servers, `gc-531266-web-02` and `gc-531266-lb-01`, we aim to improve our web infrastructure by implementing a load balancing scheme. This setup will allow our infrastructure to handle more traffic and provide high availability.

## Resources

- [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
- [HAProxy packages for Debian/Ubuntu](http://haproxy.debian.net/)

## Requirements

- Editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 16.04 LTS
- All scripts must be executable
- Scripts must pass Shellcheck without any error
- Bash scripts should start with `#!/usr/bin/env bash` followed by a comment explaining the script

## Configuration Tasks

### Task 0: Double the number of webservers

Configuration of `web-02` to match `web-01` using Bash scripts to automate the process. A custom Nginx response header will be added to track the web server responding to HTTP requests.

**File**: `0-custom_http_response_header`

### Task 1: Install your load balancer

Installation and configuration of HAproxy on `lb-01` to distribute traffic to `web-01` and `web-02`.

**File**: `1-install_load_balancer`

### Task 2 (Advanced): Add a custom HTTP header with Puppet

Automation of custom HTTP header creation using Puppet.

**File**: `2-puppet_custom_http_response_header.pp`

## Usage

Scripts are to be run on each server to configure them according to the task requirements. For example:

```bash
./0-custom_http_response_header
```

## Author

Project implemented as part of the curriculum at ALX School.

© 2024 ALX, All rights reserved.

```

```
