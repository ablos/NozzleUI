from fastapi import APIRouter
from utils.moonraker import moonraker
from utils.power import powerManager

router = APIRouter(prefix="/printer", tags=["printer"])

@router.get("/info")
async def get_info():
    return await moonraker.get("/printer/info")

@router.get("/extruder")
async def get_extruder():
    return await moonraker.get("/printer/objects/query?extruder")

@router.get("/position")
async def get_position():
    return await moonraker.get("/printer/objects/query?motion_report")

@router.get("/bed")
async def get_bed():
    return await moonraker.get("/printer/objects/query?heater_bed")

@router.get("/print")
async def get_print():
    return await moonraker.get("/printer/objects/query?print_stats")

@router.get("/power/status")
async def get_power_status():
    return await powerManager.power_status()

@router.get("/power/on")
async def power_printer_on():
    return await powerManager.power_on()

@router.get("/power/off")
async def power_printer_off():
    return await powerManager.power_off()