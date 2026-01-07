import asyncio

class SerialTransport:
    def __init__(self, device):
        self.device = device
        self.lock = asyncio.Lock()

    async def send(self, command: str) -> str | None:
        async with self.lock:   # concurrency-safe
            return await self.device.handle(command)

