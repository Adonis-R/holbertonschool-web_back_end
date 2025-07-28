#!/usr/bin/env python3
"""Module for Redis basic exercises.
"""
import redis  # pyright: ignore[reportMissingImports]
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of calls to a method."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to count calls."""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and
    outputs for a function."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to store call history."""
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output

    return wrapper


def replay(method: Callable) -> None:
    """Display the history of calls of a particular function."""
    redis_client = method.__self__._redis
    key = method.__qualname__

    # Récupère le nombre d'appels
    count = redis_client.get(key)
    if count is None:
        print(f"{key} was never called.")
        return

    print(f"{key} was called {int(count)} times:")

    inputs = redis_client.lrange(f"{key}:inputs", 0, -1)
    outputs = redis_client.lrange(f"{key}:outputs", 0, -1)

    for inp, outp in zip(inputs, outputs):
        print(f"{key}(*{inp.decode('utf-8')}) -> {outp.decode('utf-8')}")


class Cache:
    """Cache class for redis operations."""

    def __init__(self):
        """Store an instance of the redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method that takes a data argument
        and returns a string."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None]:
        """Get method that take a key string argument and an
        optional Callable argument named fn."""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Get method that returns a string."""
        value = self.get(key)
        if value is None:
            return ""
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """Get method that returns an integer."""
        value = self.get(key)
        if value is None:
            return 0
        return int(value) if isinstance(value, bytes) else value
