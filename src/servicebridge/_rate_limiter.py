"""
Token-bucket rate limiter enforcing ServiceBridge API limits:
  - 50 requests per second
  - 60,000 requests per hour
"""

import asyncio
import time


class RateLimiter:
    def __init__(
        self,
        per_second: int = 50,
        per_hour: int = 60_000,
    ) -> None:
        # Per-second bucket
        self._per_second = per_second
        self._second_tokens = float(per_second)
        self._second_last = time.monotonic()

        # Per-hour bucket
        self._per_hour = per_hour
        self._hour_tokens = float(per_hour)
        self._hour_last = time.monotonic()

        self._lock = asyncio.Lock()

    async def acquire(self) -> None:
        """Wait until a request slot is available, then consume one token."""
        async with self._lock:
            while True:
                now = time.monotonic()

                # Replenish second bucket
                elapsed_s = now - self._second_last
                self._second_tokens = min(
                    float(self._per_second),
                    self._second_tokens + elapsed_s * self._per_second,
                )
                self._second_last = now

                # Replenish hour bucket
                elapsed_h = now - self._hour_last
                self._hour_tokens = min(
                    float(self._per_hour),
                    self._hour_tokens + elapsed_h * (self._per_hour / 3600.0),
                )
                self._hour_last = now

                if self._second_tokens >= 1 and self._hour_tokens >= 1:
                    self._second_tokens -= 1
                    self._hour_tokens -= 1
                    return

                # Calculate how long to wait for the more restrictive bucket
                wait_s = (1 - self._second_tokens) / self._per_second if self._second_tokens < 1 else 0.0
                wait_h = (1 - self._hour_tokens) / (self._per_hour / 3600.0) if self._hour_tokens < 1 else 0.0
                wait = max(wait_s, wait_h)

                await asyncio.sleep(wait)
