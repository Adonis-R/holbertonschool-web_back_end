#!/usr/bin/env python3
"""
Redis basic operations module.
This module provides a Cache class for basic Redis operations
including storing data, retrieving data with type conversion,
counting method calls, and storing call history.
"""

import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times a method is called.
    
    Args:
        method: The method to be decorated
        
    Returns:
        Callable: The wrapped method that increments a counter each time it's called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the call count and calls the original method.
        
        Args:
            self: The instance of the class
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
            
        Returns:
            Any: The return value of the original method
        """
        # Use the method's qualified name as the key
        key = method.__qualname__
        # Increment the count for this method
        self._redis.incr(key)
        # Call and return the original method
        return method(self, *args, **kwargs)
    
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a method.
    
    Args:
        method: The method to be decorated
        
    Returns:
        Callable: The wrapped method that stores input/output history
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that stores method inputs and outputs.
        
        Args:
            self: The instance of the class
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
            
        Returns:
            Any: The return value of the original method
        """
        # Create keys for inputs and outputs based on method's qualified name
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        
        # Store the input arguments as a string
        self._redis.rpush(input_key, str(args))
        
        # Execute the original method to get the output
        output = method(self, *args, **kwargs)
        
        # Store the output
        self._redis.rpush(output_key, output)
        
        return output
    
    return wrapper


class Cache:
    """
    A Cache class for basic Redis operations.
    
    This class provides methods to store and retrieve data from Redis,
    with support for type conversion and method call tracking.
    """
    
    def __init__(self):
        """
        Initialize the Cache instance.
        
        Creates a Redis client instance and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.
        
        Args:
            data: The data to store (can be str, bytes, int, or float)
            
        Returns:
            str: The randomly generated key used to store the data
        """
        # Generate a random key using uuid
        key = str(uuid.uuid4())
        # Store the data in Redis
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Retrieve data from Redis and optionally apply a conversion function.
        
        Args:
            key: The key to retrieve data for
            fn: Optional callable to convert the data back to desired format
            
        Returns:
            Any: The retrieved data, optionally converted by fn
        """
        # Get the data from Redis
        data = self._redis.get(key)
        
        # If data doesn't exist, return None (Redis.get behavior)
        if data is None:
            return None
        
        # If a conversion function is provided, apply it
        if fn is not None:
            return fn(data)
        
        return data
    
    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data from Redis and convert it to a string.
        
        Args:
            key: The key to retrieve data for
            
        Returns:
            Optional[str]: The retrieved data as a string, or None if key doesn't exist
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))
    
    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from Redis and convert it to an integer.
        
        Args:
            key: The key to retrieve data for
            
        Returns:
            Optional[int]: The retrieved data as an integer, or None if key doesn't exist
        """
        return self.get(key, fn=int)


def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function.
    
    Args:
        method: The method to display the call history for
    """
    # Get the Redis instance from the method's class
    redis_instance = method.__self__._redis
    
    # Get the method's qualified name
    method_name = method.__qualname__
    
    # Get the call count
    call_count = redis_instance.get(method_name)
    if call_count is None:
        call_count = 0
    else:
        call_count = int(call_count)
    
    print(f"{method_name} was called {call_count} times:")
    
    # Get inputs and outputs
    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"
    
    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)
    
    # Display each call with its input and output
    for input_data, output_data in zip(inputs, outputs):
        input_str = input_data.decode("utf-8")
        output_str = output_data.decode("utf-8")
        print(f"{method_name}(*{input_str}) -> {output_str}")
