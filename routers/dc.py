from fastapi import APIRouter
from pydantic import BaseModel

from data import enter_dc, leave_dc, get_people

router = APIRouter()

class NameIn(BaseModel):
    name: str

class PersonOut(BaseModel):
    name: str
    entered_at: str

@router.get("/get-people", response_model=list[PersonOut])
def api_get_people():
    return get_people()

@router.post("/enter")
def api_enter_dc(body: NameIn):
    name = body.name.strip()
    enter_dc(name)
    return {"ok": True, "message": f"Welcome to DC, {name}!"}

@router.post("/leave")
def api_leave_dc(body: NameIn):
    name = body.name.strip()
    leave_dc(name)
    return {"ok": True, "message": f"Goodbye from DC, {name}!"}
