from fastapi import APIRouter
from utils.moonraker import moonraker

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