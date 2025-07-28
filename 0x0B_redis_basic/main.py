#!/usr/bin/env python3
"""
Test file for Redis basic operations
"""
import redis

Cache = __import__('exercise').Cache
replay = __import__('exercise').replay

def test_task_0():
    """Test task 0: Writing strings to Redis"""
    print("=== Testing Task 0: Writing strings to Redis ===")
    cache = Cache()

    data = b"hello"
    key = cache.store(data)
    print(f"Generated key: {key}")

    local_redis = redis.Redis()
    retrieved_data = local_redis.get(key)
    print(f"Retrieved data: {retrieved_data}")
    print()

def test_task_1():
    """Test task 1: Reading from Redis and recovering original type"""
    print("=== Testing Task 1: Reading from Redis and recovering original type ===")
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        retrieved = cache.get(key, fn=fn)
        print(f"Stored: {value}, Retrieved: {retrieved}, Match: {retrieved == value}")
    
    # Test get_str and get_int
    str_key = cache.store("hello")
    int_key = cache.store(42)
    
    print(f"get_str result: {cache.get_str(str_key)}")
    print(f"get_int result: {cache.get_int(int_key)}")
    print()

def test_task_2():
    """Test task 2: Incrementing values"""
    print("=== Testing Task 2: Incrementing values ===")
    cache = Cache()

    cache.store(b"first")
    print(f"Call count after 1st store: {cache.get(cache.store.__qualname__)}")

    cache.store(b"second")
    cache.store(b"third")
    print(f"Call count after 3rd store: {cache.get(cache.store.__qualname__)}")
    print()

def test_task_3():
    """Test task 3: Storing lists"""
    print("=== Testing Task 3: Storing lists ===")
    cache = Cache()

    s1 = cache.store("first")
    print(f"Key 1: {s1}")
    s2 = cache.store("second")
    print(f"Key 2: {s2}")
    s3 = cache.store("third")
    print(f"Key 3: {s3}")

    inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
    outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

    print(f"inputs: {inputs}")
    print(f"outputs: {outputs}")
    print()

def test_task_4():
    """Test task 4: Retrieving lists"""
    print("=== Testing Task 4: Retrieving lists ===")
    cache = Cache()
    
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    
    replay(cache.store)
    print()

if __name__ == "__main__":
    test_task_0()
    test_task_1()
    test_task_2()
    test_task_3()
    test_task_4()
