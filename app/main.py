from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi import Query
import asyncio
import time
from app.scpi import SCPIDevice
from app.transport import SerialTransport
from app.logger import log_event

app = FastAPI()

device = SCPIDevice()
transport = SerialTransport(device)

# -----------------------------
# REST endpoint to CONF
# -----------------------------
@app.post("/conf")
async def conf_voltage(mode: str = Query("VOLT")):
    """Set the measurement mode"""
    command = f"CONF:{mode.upper()}"
    response = await transport.send(command)
    await log_event(command, response)
    return {"status": response, "mode": mode.upper()}

# -----------------------------
# REST endpoint to MEAS
# -----------------------------
@app.get("/measure")
async def measure_voltage():
    """Return a measurement"""
    command = "MEAS:VOLT?"
    value = await transport.send(command)
    await log_event(command, value)
    return {"value": value, "timestamp": time.time()}

# -----------------------------
# Manual SCPI WebSocket
# -----------------------------
@app.websocket("/ws/scpi")
async def ws_scpi(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            msg = await ws.receive_text()
            response = await transport.send(msg)
            await log_event(msg, response)
            if response is not None:
                await ws.send_json({"value": response})
    except Exception:
        pass

# -----------------------------
# Auto WebSocket
# -----------------------------
@app.websocket("/ws/auto")
async def ws_auto(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            value = await transport.send("MEAS:VOLT?")
            if value is not None:
                await ws.send_json({"value": value})
                await log_event("MEAS:VOLT?", value)
            await asyncio.sleep(0.3)
    except Exception:
        pass

# -----------------------------
# Serve frontend
# -----------------------------
app.mount("/", StaticFiles(directory="app/frontend", html=True), name="frontend")

