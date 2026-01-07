import asyncio
import random

class SCPIDevice:
    def __init__(self):
        self.mode = "VOLT"

    async def handle(self, command: str) -> str | None:
        command = command.strip().upper()

        if command == "CONF:VOLT":
            self.mode = "VOLT"
            return "OK"

        if command == "MEAS:VOLT?":
            await asyncio.sleep(0.05)  # simulate I/O delay
            return f"{3.0 + random.uniform(-0.2, 0.2):.3f}"

        return "ERROR"

