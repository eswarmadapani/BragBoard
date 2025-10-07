from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from database import get_db
from models import User
from auth import hash_password, verify_password, create_access_token, create_refresh_token, get_current_user

router = APIRouter(prefix="/users", tags=["users"])

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    department: str
    role: str = "employee"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class UserProfile(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str
    joined_at: str
    
    class Config:
        from_attributes = True

@router.post("/register", response_model=TokenResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash password
    hashed_password = hash_password(user.password)
    
    # Create user
    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password,
        department=user.department,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Create tokens
    access_token = create_access_token(data={"sub": new_user.email})
    refresh_token = create_refresh_token(data={"sub": new_user.email})
    
    return TokenResponse(access_token=access_token, refresh_token=refresh_token)

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Find user
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Create tokens
    access_token = create_access_token(data={"sub": db_user.email})
    refresh_token = create_refresh_token(data={"sub": db_user.email})
    
    return TokenResponse(access_token=access_token, refresh_token=refresh_token)

@router.get("/profile", response_model=UserProfile)
def get_user_profile(current_user: User = Depends(get_current_user)):
    """Get current user's profile information"""
    return UserProfile(
        id=current_user.id,
        name=current_user.name,
        email=current_user.email,
        department=current_user.department,
        role=current_user.role,
        joined_at=current_user.joined_at.isoformat()
    )
