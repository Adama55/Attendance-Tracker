from fastapi import APIRouter, HTTPException


router= APIRouter(
    prefix='/cours',
    tags=["cours"]
)