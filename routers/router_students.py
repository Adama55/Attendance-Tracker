from fastapi import APIRouter, HTTPException
from typing import List
import uuid
from classes.schema import Student, StudentNoID
from database.firebase import db


router= APIRouter(
    prefix='/students',
    tags=["Students"]
)

students = [
    Student(id="student1", name="Adama"),
    Student(id="student2", name="Adrien"),
    Student(id="student3", name="Akbar")
]

@router.get('', response_model=List[Student])
async def get_student():
    """List all the students from a Training Center (context fonctionnel ou technique)"""
    
    fireBaseobject = db.child("student").get().val()
    resultsarray= [ value for value in fireBaseobject.values]
    return resultsarray

@router.get('/{student_id}', response_model=Student)
async def get_student_by_id(student_id: str):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@router.post('', response_model=Student, status_code=201)
async def add_new_student(giveName:StudentNoID):
    generatedId= uuid.uuid4()
    newStudent= Student(id=str(generatedId), name=giveName.name)
    students.append(newStudent)

    #connexion à la base de donnée
    db.child("student").child(str(generatedId)).set(newStudent.model_dump())
    return newStudent

@router.patch('/{student_id}', status_code=204)
async def modify_student_name(student_id:str, modifiedStudent: StudentNoID):
    #CONNEXION TO DATA BASE
    for student in students:
        if student.id == student_id:
            student.name=modifiedStudent.name
            return student
    raise HTTPException(status_code= 404, detail="Student not found")