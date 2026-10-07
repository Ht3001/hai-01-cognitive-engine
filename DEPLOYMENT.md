# HAI-01 Deployment Guide

This project is prepared for deployment as:
- Frontend static site on ht3001.com or a subdomain
- Backend FastAPI on Render or Railway

## 1) Deploy backend on Render

1. Go to https://dashboard.render.com/new/web
2. Connect the repository: `Ht3001/hai-01-cognitive-engine`
3. Configure:
   - Name: `hai-01-cognitive-engine`
   - Runtime: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. Add environment variables:
   - `ENVIRONMENT=production`
   - `ALLOWED_ORIGINS=https://ht3001.com,https://www.ht3001.com,https://hai.ht3001.com,https://app.ht3001.com,http://localhost:8000`
5. Click Create Web Service
6. Copy the generated public URL, for example:
   - `https://hai-01-cognitive-engine.onrender.com`

## 2) Deploy backend on Railway

1. Go to Railway and create a new project
2. Deploy from GitHub repository: `Ht3001/hai-01-cognitive-engine`
3. Configure the start command:
   - `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. Add environment variables:
   - `ENVIRONMENT=production`
   - `ALLOWED_ORIGINS=https://ht3001.com,https://www.ht3001.com,https://hai.ht3001.com,https://app.ht3001.com,http://localhost:8000`
5. Save and note the public URL

## 3) Deploy frontend on ht3001.com

Upload the file `static/index.html` to your hosting root (`public_html` or `www`) or to a dedicated subdomain folder.

Important: the frontend already tries to use these domains in order:
- `https://api.ht3001.com`
- `https://hai-01-cognitive-engine.onrender.com`
- `http://localhost:8000`

If you deploy the backend on Render, the final URL should be:

`https://hai-01-cognitive-engine.onrender.com`

## 4) Optional custom subdomain

You can also use:
- `hai.ht3001.com`
- `app.ht3001.com`
- `api.ht3001.com`

Then update `ALLOWED_ORIGINS` and the frontend URL accordingly.

## 5) Final verification

Open the frontend and try a sample observation. If the backend is active, you should receive:
- `filtered_perception`
- `semantic_interpretation`
- `intuition`

If not, verify:
- the backend URL is correct
- CORS is enabled
- the backend is running on the correct port
- the environment variables are present

## 6) Recommended production setup

Recommended architecture:
- Frontend: `https://ht3001.com`
- Backend: `https://hai-01-cognitive-engine.onrender.com`

This is the cleanest production setup for a static web client plus a Python API.
