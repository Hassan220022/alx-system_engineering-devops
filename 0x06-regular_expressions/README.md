# 0x06. Regular Expressions

## Description

This project is part of the ALX Software Engineering curriculum's DevOps track. It focuses on utilizing regular expressions (regex) in Ruby, leveraging the Oniguruma library. The project includes various tasks to match specific patterns and handle text processing in a precise and efficient manner.

## Curriculum

- **SE Foundations**
- **DevOps**

## Project Details

- **Weight**: 1
- **Project Duration**: February 27, 2024, 6:00 AM to February 28, 2024, 6:00 AM
- **Auto Review Launch**: At the deadline

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS
- All scripts must be executable (`chmod +x`)
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env ruby`
- Regex must be built for the Oniguruma library

## Tasks

### 0. Simply Matching School

**File**: `0-simply_match_school.rb`

- The regex must match "School".
- Example usage:
  ```bash
  ./0-simply_match_school.rb School | cat -e
  ```

### 1. Repetition Token #0

**File**: `1-repetition_token_0.rb`

- Match specific patterns using repetition tokens.

### 2. Repetition Token #1

**File**: `2-repetition_token_1.rb`

- Continuation of pattern matching with different criteria.

### 3. Repetition Token #2

**File**: `3-repetition_token_2.rb`

- Advanced regex patterns for more specific use cases.

### 4. Repetition Token #3

**File**: `4-repetition_token_3.rb`

- Regex that does not contain square brackets but matches complex patterns.

### 5. Not Quite HBTN Yet

**File**: `5-beginning_and_end.rb`

- The regex must match a string that starts with 'h', ends with 'n', and has any single character in between.

### 6. Call Me Maybe

**File**: `6-phone_number.rb`

- The regex must match a 10-digit phone number.

### 7. OMG WHY ARE YOU SHOUTING?

**File**: `7-OMG_WHY_ARE_YOU_SHOUTING.rb`

- The regex must match capital letters only.

### Advanced Task: Textme

**File**: `100-textme.rb`

- Extract specific parts from logs for analysis.

## Background Context

For these tasks, you will use a Ruby script environment to apply regular expressions for various text matching and extraction purposes. Here is a typical command:

```ruby
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
```

## Resources

- [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
- [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
- [Rubular is your best friend](https://rubular.com)
- [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
- [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)

---

**Copyright © 2024 ALX, All rights reserved.**
