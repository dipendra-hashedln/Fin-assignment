# API Endpoints

- **GET** `/api/dashboard/tiles` — Fetch Dashboard Data
- **POST** `/api/lms/leaves/apply` — Apply for Leave
- **GET** `/api/lms/leaves/status` — Retrieve Leave Status
- **PATCH** `/api/lms/leaves/{leave_id}/approve` — Approve/Reject Leave (Manager Only)
- **POST** `/api/pods/assign` — Assign Employee to Pod
- **GET** `/api/pods/{pod_id}/details` — Get Pod Details
- **POST** `/api/pods/{pod_id}/recommend` — Recommend an Employee for a Pod
- **POST** `/api/auth/login` — User Login
- **GET** `/api/auth/user` — Fetch Current User Details