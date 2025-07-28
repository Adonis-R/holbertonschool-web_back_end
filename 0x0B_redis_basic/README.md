# 0x0B. Redis basic

This project demonstrates basic Redis operations using Python, including storing and retrieving data, implementing decorators for method call counting and history tracking.

## Learning Objectives

- Learn how to use Redis for basic operations
- Learn how to use Redis as a simple cache
- Understand Redis data types and commands
- Implement decorators for method tracking

## Requirements

- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All files should end with a new line
- First line of all files should be exactly `#!/usr/bin/env python3`
- Code should use the pycodestyle style (version 2.5)
- All modules, classes, and functions should have documentation
- All functions and coroutines must be type-annotated

## Installation

Install Redis server:
```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

## Tasks

### 0. Writing strings to Redis
- Create a Cache class with Redis client
- Implement store method that generates random key and stores data
- Type-annotate store method correctly

### 1. Reading from Redis and recovering original type
- Implement get method with optional conversion function
- Create get_str and get_int convenience methods
- Preserve original Redis.get behavior

### 2. Incrementing values
- Implement count_calls decorator using INCR command
- Track how many times methods are called
- Use method's qualified name as key

### 3. Storing lists
- Implement call_history decorator using RPUSH command
- Store method inputs and outputs in separate lists
- Track complete call history

### 4. Retrieving lists
- Implement replay function to display call history
- Use LRANGE command to retrieve stored lists
- Format output showing method calls and results

## Files

- `exercise.py`: Main implementation file containing Cache class and decorators
- `README.md`: This file
