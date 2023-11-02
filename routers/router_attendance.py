from fastapi import APIRouter, HTTPException
from typing import List


router= APIRouter(
    prefix='/attendance',
    tags=["attendance"]
)
@router.get('', response_model=List)
async def get_attendance():
    """List all the courses."""
    return { "message" :"all attendance"}