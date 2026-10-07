# Desplegar HAI-01 en Render

## Paso 1: Ir a Render

1. Ve a https://render.com
2. Crea una cuenta o inicia sesión
3. Conecta tu cuenta de GitHub

## Paso 2: Crear nuevo Web Service

1. Haz clic en "New +"
2. Selecciona "Web Service"
3. Busca el repositorio: `Ht3001/hai-01-cognitive-engine`
4. Selecciona "Connect"

## Paso 3: Configurar el servicio

### Información básica:
- **Name**: hai-01-cognitive-engine
- **Root Directory**: . (raíz)
- **Runtime**: Python 3
- **Build Command**: pip install -r requirements.txt
- **Start Command**: uvicorn app.main:app --host 0.0.0.0 --port $PORT

### Plan:
- Selecciona "Free" (o el plan que prefieras)

## Paso 4: Variables de entorno

Haz clic en "Advanced" y agrega estas variables:

```
ENVIRONMENT = production
ALLOWED_ORIGINS = https://ht3001.com,https://www.ht3001.com,https://hai.ht3001.com,https://app.ht3001.com,http://localhost:8000
```

## Paso 5: Desplegar

1. Haz clic en "Create Web Service"
2. Espera 2-5 minutos mientras Render construye y despliega la app
3. Cuando esté listo, verás un mensaje "Live" en la esquina
4. **Copia la URL pública**, por ejemplo:
   ```
   https://hai-01-cognitive-engine.onrender.com
   ```

## Paso 6: Actualizar el frontend

En tu archivo `static/index.html`, busca la línea:

```javascript
const API_BASE = 'https://api.ht3001.com';
```

Y reemplázala con la URL que obtuviste de Render:

```javascript
const API_BASE = 'https://hai-01-cognitive-engine.onrender.com';
```

## Paso 7: Subir el frontend a ht3001.com

1. Ve a tu panel de hosting (cPanel, File Manager, etc.)
2. Navega a `public_html` o `www`
3. Sube el archivo `static/index.html` ahí
4. Asegúrate que sea accesible en: https://ht3001.com

## Paso 8: Verificar que funciona

1. Abre https://ht3001.com en tu navegador
2. Escribe una observación de prueba
3. Haz clic en "Procesar en Espejo Cognitivo"
4. Si ves una respuesta, ¡está funcionando!

## Troubleshooting

### La app tarda en responder
- Render tiene un "free tier" que se pone en sleep después de 15 minutos de inactividad
- La primera solicitud puede tardar 10-30 segundos mientras se reactiva
- Considera actualizar a un plan pagado si necesitas disponibilidad 24/7

### Error: "No se pudo conectar con el backend"
- Verifica que la URL de Render sea correcta
- Verifica que el backend esté "Live" en el dashboard de Render
- Verifica los logs en Render para errores

### CORS error
- Asegúrate de que tu dominio esté en `ALLOWED_ORIGINS`
- Actualiza la variable de entorno en Render
- Redeploy la app

## URLs finales

- **Frontend**: https://ht3001.com
- **Backend API**: https://hai-01-cognitive-engine.onrender.com
- **API Docs**: https://hai-01-cognitive-engine.onrender.com/docs
- **Repo**: https://github.com/Ht3001/hai-01-cognitive-engine
