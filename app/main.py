"""
HAI-01: Cognitive Mirror & Metacognitive Autonomy Engine
Production Configuration for ht3001.com deployment
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional

# Detectar entorno
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,http://localhost:8000").split(",")

if ENVIRONMENT == "production":
    ALLOWED_ORIGINS = [
        "https://ht3001.com",
        "https://www.ht3001.com",
        "https://ht3001.github.io",
        "https://hai.ht3001.com",
        "https://app.ht3001.com",
        "http://localhost:8000",
    ]

app = FastAPI(
    title="HAI-01 Universal Web API",
    description="API de Espejo Cognitivo y Autonomía Metacognitiva",
    version="1.0.0",
    docs_url="/api/docs" if ENVIRONMENT == "production" else "/docs",
    openapi_url="/api/openapi.json" if ENVIRONMENT == "production" else "/openapi.json"
)

# CORS Configuration para múltiples orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)

# Servir archivos estáticos (HTML, CSS, JS)
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# ============ Modelos Pydantic ============

class PerceptionRequest(BaseModel):
    """Modelo para solicitud de percepción cognitiva"""
    observation: str
    processing_style: Optional[str] = "synthetic"
    sensory_filtering: Optional[bool] = True
    neurodiversity_mode: Optional[str] = "standard"

class PerceptionResponse(BaseModel):
    """Modelo para respuesta de percepción filtrada"""
    raw_observation: str
    filtered_perception: str
    semantic_interpretation: str
    intuition: str
    processing_style: str
    neuro_adapted: bool

class SystemStatus(BaseModel):
    """Modelo para estado del sistema"""
    system: str
    status: str
    mode: str
    version: str
    environment: str
    allowed_origins: list

# ============ Endpoints ============

@app.get("/")
def read_root():
    """Estado del sistema y punto de entrada"""
    return SystemStatus(
        system="HAI-01",
        status="active",
        mode="Cognitive Mirror Engine",
        version="1.0.0",
        environment=ENVIRONMENT,
        allowed_origins=ALLOWED_ORIGINS
    )

@app.get("/api/v1/health")
def health_check():
    """Health check para monitoreo"""
    return {
        "status": "healthy",
        "service": "HAI-01",
        "environment": ENVIRONMENT
    }

@app.post("/api/v1/perception", response_model=PerceptionResponse)
def process_perception(req: PerceptionRequest):
    """
    Ciclo: Observación -> Percepción -> Interpretación -> Intuición
    
    Este endpoint procesa una observación bruta y la pasa a través
    del espejo cognitivo, generando filtros perceptivos y metacognición.
    
    También aplica adaptaciones neurodiversas según el modo seleccionado.
    """
    raw = req.observation.strip()
    
    neuro_adapted = req.neurodiversity_mode != "standard"
    
    if req.neurodiversity_mode == "low_stimulation":
        perception = f"[Filtrado Reducido]: {raw[:100]}..."
    elif req.neurodiversity_mode == "high_contrast":
        perception = f"[FILTRADO ALTO CONTRASTE]: {raw.upper()}"
    else:
        perception = (
            f"[Filtrado {req.processing_style}]: {raw}"
            if req.sensory_filtering
            else raw
        )
    
    interpretation = f"Contextualización semántica de: '{perception}'"
    intuition = f"¿Qué patrón identificas en '{raw[:30]}...?" 
    
    return PerceptionResponse(
        raw_observation=raw,
        filtered_perception=perception,
        semantic_interpretation=interpretation,
        intuition=intuition,
        processing_style=req.processing_style,
        neuro_adapted=neuro_adapted
    )

@app.post("/api/v1/perception/batch")
def process_perception_batch(observations: list[PerceptionRequest]):
    """Procesa múltiples observaciones en lote"""
    results = []
    for obs in observations:
        result = process_perception(obs)
        results.append(result)
    return {"count": len(results), "results": results}

@app.get("/api/v1/config")
def get_config():
    """Obtener configuración del sistema"""
    return {
        "environment": ENVIRONMENT,
        "allowed_origins": ALLOWED_ORIGINS,
        "static_files": os.path.exists("static"),
        "api_version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    host = "0.0.0.0" if ENVIRONMENT == "production" else "127.0.0.1"
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        app,
        host=host,
        port=port,
        access_log=True,
        log_level="info"
    )
