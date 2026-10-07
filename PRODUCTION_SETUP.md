# Configuración Final: Backend en Render + Frontend en ht3001.com

## Arquitectura

```
Frontend Estático               Backend FastAPI
(ht3001.com)        ←---JSON---→  (Render)
   index.html                 /api/v1/perception
   CSS + JS                   /api/v1/health
```

## Paso 1: Desplegar Backend en Render

1. Ve a https://render.com
2. Conecta tu repositorio: `Ht3001/hai-01-cognitive-engine`
3. Crea un nuevo "Web Service" con:
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Environment:
     - `ENVIRONMENT=production`
     - `ALLOWED_ORIGINS=https://ht3001.com,https://www.ht3001.com,https://hai.ht3001.com,https://app.ht3001.com,http://localhost:8000`

4. Copia la URL pública de Render, por ejemplo:
   ```
   https://hai-01-cognitive-engine.onrender.com
   ```

## Paso 2: Preparar Frontend

1. Usa el archivo: `PRODUCTION_FRONTEND.html`
2. Reemplaza la URL de API en la línea:
   ```javascript
   const API_BASE = 'https://hai-01-cognitive-engine.onrender.com';
   ```
   (Con la URL real que obtuviste de Render)

3. Renombra el archivo a `index.html`

## Paso 3: Subir Frontend a ht3001.com

### Opción A: Hosting con cPanel

1. Inicia sesión en cPanel
2. Abre "File Manager"
3. Navega a `public_html` o `www`
4. Sube `index.html` allí
5. Verifica en https://ht3001.com

### Opción B: Hosting con FTP

1. Conéctate vía FTP a tu servidor
2. Navega a `public_html` o `www`
3. Sube `index.html` ahí
4. Verifica en https://ht3001.com

### Opción C: Subdominio dedicado

Si prefieres un subdominio separado (por ejemplo `hai.ht3001.com`):

1. En tu hosting, crea un subdominio `hai`
2. Apunta a una carpeta nueva, por ejemplo `/home/ht3001/public_html/hai`
3. Sube `index.html` en esa carpeta
4. Verifica en https://hai.ht3001.com

## Paso 4: Verificar que funciona

1. Abre https://ht3001.com en tu navegador
2. Escribe una observación de prueba
3. Haz clic en "Procesar Reflejo"
4. Si ves una respuesta, ¡está funcionando!

## URLs Finales

- **Frontend Principal**: https://ht3001.com
- **Backend API**: https://hai-01-cognitive-engine.onrender.com
- **API Docs**: https://hai-01-cognitive-engine.onrender.com/docs
- **GitHub Repo**: https://github.com/Ht3001/hai-01-cognitive-engine

## Troubleshooting

### Error: "No se pudo conectar con el backend"

1. Verifica que Render esté activo (verde en dashboard)
2. Verifica la URL de API en el HTML
3. Verifica los logs en Render para errores

### Respuesta lenta

- Render tiene un free tier que se pone en sleep después de 15 minutos
- La primera solicitud puede tardar 10-30 segundos
- Considera un plan pagado para 24/7

### CORS Error

- Verifica que tu dominio esté en `ALLOWED_ORIGINS`
- Actualiza la variable en Render
- Redeploy la app

## Próximos pasos

- [ ] Desplegar backend en Render
- [ ] Actualizar URL de API en frontend
- [ ] Subir frontend a ht3001.com
- [ ] Probar que funciona
- [ ] Configurar dominio personalizado en Render (opcional)
- [ ] Agregar base de datos para persistencia (opcional)
- [ ] Implementar autenticación (opcional)
