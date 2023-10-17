from fastapi import APIRouter, HTTPException
from typing import List
import uuid
from classes.schema_dto import Student, StudentNoID


router= APIRouter(
    prefix='/students',
    tags=["Students"]
)