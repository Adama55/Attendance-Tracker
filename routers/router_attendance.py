from fastapi import APIRouter, HTTPException


router= APIRouter(
    prefix='/attendance',
    tags=["attendance"]
)