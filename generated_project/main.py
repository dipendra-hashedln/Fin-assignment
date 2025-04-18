from fastapi import FastAPI
from app.routes import api_auth_login
from app.routes import api_auth_user
from app.routes import api_dashboard_tiles
from app.routes import api_lms_leaves_apply
from app.routes import api_lms_leaves_leave_id_approve
from app.routes import api_lms_leaves_status
from app.routes import api_pods_assign
from app.routes import api_pods_pod_id_details
from app.routes import api_pods_pod_id_recommend


app = FastAPI()

app.include_router(api_auth_login.router)
app.include_router(api_auth_user.router)
app.include_router(api_dashboard_tiles.router)
app.include_router(api_lms_leaves_apply.router)
app.include_router(api_lms_leaves_leave_id_approve.router)
app.include_router(api_lms_leaves_status.router)
app.include_router(api_pods_assign.router)
app.include_router(api_pods_pod_id_details.router)
app.include_router(api_pods_pod_id_recommend.router)