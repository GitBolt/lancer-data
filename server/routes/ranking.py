import os
from typing import Union
from core.db import get_db
from sqlalchemy.orm import Session
from core.schemas import User
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends
from fastapi import Request
from core.schemas import User


router = APIRouter(prefix="/ranking")

@router.get("/views/{public_key}", 
            status_code=200)
async def views(public_key: str, db: Session=Depends(get_db)) -> dict:

    views_obj = db.query(User).filter_by(github_name="bolt")
    return {"hey"}