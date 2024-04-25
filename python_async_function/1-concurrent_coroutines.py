#!/usr/bin/env python3
""" Concurrent coroutines """

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns list of delays in ascending order """
    tasks = []
    delays = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delays.append(await task)

    return sorted(delays)
