from fastapi import APIRouter

router = APIRouter()

@router.post("/api/lms/leaves/apply")
async def api_lms_leaves_apply():
    return {"message": "This is a stub for Apply for Leave"}