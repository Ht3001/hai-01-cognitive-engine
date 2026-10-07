from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
import os

app = FastAPI(
    title="HAI-01 Universal Web API",
    description="API de Espejo Cognitivo y Autonomía Metacognitiva",
    version="1.0.0"
)

# Permitir acceso desde cualquier origen (Web Universal)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir archivos estáticos (HTML, CSS, JS)
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

class PerceptionRequest(BaseModel):
    """Modelo para solicitud de percepción cognitiva"""
    observation: str
    processing_style: Optional[str] = "synthetic"
    sensory_filtering: Optional[bool] = True

class PerceptionResponse(BaseModel):
    """Modelo para respuesta de percepción filtrada"""
    raw_observation: str
    filtered_perception: str
    semantic_interpretation: str
    intuition: str

@app.get("/")
def read_root():
    """Estado del sistema y punto de entrada"""
    return {
        "system": "HAI-01",
        "status": "active",
        "mode": "Cognitive Mirror Engine",
        "version": "1.0.0"
    }

@app.post("/api/v1/perception", response_model=PerceptionResponse)
def process_perception(req: PerceptionRequest):
    """
    Ciclo: Observación -> Percepción -> Interpretación -> Intuición
    
    Este endpoint procesa una observación bruta y la pasa a través
    del espejo cognitivo, generando filtros perceptivos y metacognición.
    """
    raw = req.observation.strip()
    
    # Filtrado perceptivo
    perception = (
        f"[Filtrado {req.processing_style}]: {raw}"
        if req.sensory_filtering
        else raw
    )
    
    # Interpretación semántica
    interpretation = f"Contextualización semántica de: '{perception}'"
    
    # Intuición emergente (meta-insight)
    intuition = f"Insight introspectivo: ¿Qué patrón identificas en '{raw[:30]}...'?"
    
    return PerceptionResponse(
        raw_observation=raw,
        filtered_perception=perception,
        semantic_interpretation=interpretation,
        intuition=intuition
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
