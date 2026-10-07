# HAI-01: Cognitive Mirror & Metacognitive Autonomy Engine

## Overview

**HAI-01** es un sistema de experiencia adaptativa basado en inteligencia cognitiva, diseñado para crear una interfaz universal que observe, interprete y adapte la interacción del usuario en tiempo real.

La arquitectura combina:
- **Espejo Cognitivo**: Filtros de percepción y modelado de contexto
- **Ciclo Metacognitivo**: Gestión de estado y toma de decisiones
- **Adaptador de Interfaz**: Personalización y accesibilidad

## Arquitectura

```
Cliente Web / PWA Universal
        │ (HTTP / WebSockets)
        ▼
API Engine (FastAPI)
        │
        ├── Espejo Cognitivo (Filtros de Percepción)
        ├── Ciclo Metacognitivo (Gestor de Estados)
        └── Adaptador de Interfaz (Accesibilidad & Neurodiversidad)
```

## Stack Técnico

- **Backend**: FastAPI + Uvicorn
- **Frontend**: HTML5 / CSS3 / Vanilla JavaScript (PWA-ready)
- **Comunicación**: HTTP / WebSockets / CORS
- **Persistencia**: Redis (sesiones), PostgreSQL (datos)
- **Autenticación**: JWT / OAuth2

## Instalación

### Requisitos
- Python 3.10+
- pip o poetry

### Pasos

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Ht3001/hai-01-cognitive-engine.git
   cd hai-01-cognitive-engine
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el servidor**
   ```bash
   python app/main.py
   ```
   O con uvicorn:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Acceder a la interfaz**
   - API: http://localhost:8000
   - Documentación interactiva: http://localhost:8000/docs
   - Cliente web: http://localhost:8000/static/index.html

## Endpoints

### GET `/`
Estado general del sistema.

**Respuesta:**
```json
{
  "system": "HAI-01",
  "status": "active",
  "mode": "Cognitive Mirror Engine",
  "version": "1.0.0"
}
```

### POST `/api/v1/perception`
Procesa una observación a través del espejo cognitivo.

**Request:**
```json
{
  "observation": "Tu pensamiento o situación a reflexionar",
  "processing_style": "synthetic",
  "sensory_filtering": true
}
```

**Response:**
```json
{
  "raw_observation": "Tu pensamiento o situación a reflexionar",
  "filtered_perception": "[Filtrado synthetic]: Tu pensamiento o situación a reflexionar",
  "semantic_interpretation": "Contextualización semántica de: '[Filtrado synthetic]: Tu pensamiento o situación a reflexionar'",
  "intuition": "Insight introspectivo: ¿Qué patrón identificas en 'Tu pensamiento o situaci...?"
}
```

## Características Principales

✅ **Espejo Cognitivo**: Filtros de percepción sensorial y modelado de contexto  
✅ **Ciclo Metacognitivo**: Gestión de estados y decisiones adaptativas  
✅ **Adaptador de Interfaz**: Personalización y accesibilidad (WCAG 2.1)  
✅ **PWA-Ready**: Cliente web instalable y offline-first  
✅ **CORS Universal**: Acceso desde cualquier origen  
✅ **API Documentation**: Auto-generada con Swagger/OpenAPI  

## Roadmap

- [ ] Persistencia con PostgreSQL + Redis
- [ ] Autenticación JWT / OAuth2
- [ ] WebSockets para comunicación bidireccional
- [ ] Historial de sesiones y memoria cognitiva
- [ ] Modelos de IA para análisis semántico avanzado
- [ ] Métricas y telemetría de experiencia
- [ ] Módulos de accesibilidad neurodiversidad
- [ ] Dashboard de administración

## Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit los cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

MIT License - Ver `LICENSE` para detalles.

## Autor

**Ht3001** - Diseño y desarrollo inicial

## Contacto

Para preguntas o sugerencias, abre un issue en el repositorio.

---

**HAI-01: Where Cognition Meets Adaptation**
