# Project Overview

SCPI Voltage measuements using FastAPI


Can use HTTP hooks and using JSON for data storage.


Includes Poetry for Dependency management advantage.

# One timer 

## Dependencies
Poetry
Python3 
plotly
AsyncIO
FastAPI

# Start project

poetry run uvicorn app.main:app --reload

## Test SCPI endpoints

curl -X POST "http://127.0.0.1:8000/conf?mode=VOLT"

Output example: 

{"status":"OK","mode":"VOLT"}


curl "http://127.0.0.1:8000/measure"


Output example: 

{"value":"3.018","timestamp":1767781488.1346893}


## Install cargo depdendencies

poetry install



# FAQ

## AsyncIO:

1. Websocket handlers

@app.websocket("/ws/scpi")
async def ws_scpi(ws: WebSocket)

Multiple clients can connect simultaneously without blocking each other

FastAPI + uvicorn uses asyncio event loop to handle many connections concurrently


2. Transport lock

async with self.lock:
    return await self.device.handle(command)
    
If two clients send SCPI commands at the same time, this ensures serialized access to the (simulated) device

Prevents race conditions that would happen on a real serial port


3. Device simulation


await asyncio.sleep(0.05)  # simulate I/O delay

Simulates non-blocking I/O (like real hardware response time).

Allows the event loop to serve other clients while waiting, providing real concurrency.


## How is the data saved?

In Json format in root folder: 
/scpi-fastapi/scpi_log.jsonl
