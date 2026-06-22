# Deploy Notes - Despliegue Simulado

## Proyecto
InvBorradoLogico - Sistema de gestion de productos con borrado logico
Framework: Django 5.2.7
Base de datos: PostgreSQL
Contenedorizacion: Docker + Docker Compose

## Pasos del Despliegue Simulado

### 1. Clonar el repositorio
git clone https://github.com/MelanieGarciaO/EXPERIMENTAL-3-GESTION-CONFIGURACION-CRUD.git
cd EXPERIMENTAL-3-GESTION-CONFIGURACION-CRUD/InvBorradoLogico

### 2. Configurar variables de entorno
Crear el archivo .env en la raiz del proyecto:
POSTGRES_NAME=pruebatec
POSTGRES_USER=postgres
POSTGRES_PASSWORD=mmgo26
POSTGRES_HOST=host.docker.internal
POSTGRES_PORT=5432

### 3. Construir y levantar los contenedores
docker compose up --build

### 4. Verificar que el contenedor esta corriendo
docker ps

### 5. Validar desde el navegador
Abrir: http://localhost:8000
Se visualiza la pantalla de inicio con Marcas y Productos.

### 6. Detener el contenedor
docker compose down

## Flujo CI/CD Automatizado
- CI Tests: GitHub Actions instala dependencias y ejecuta tests Django
- Build: Docker construye imagen django-invborradologico:latest
- Artefacto: GitHub Actions guarda la imagen por 7 dias
- Deploy simulado: Docker Compose levanta el contenedor localmente

## Evidencia
- Contenedor corriendo: http://localhost:8000
- Imagen generada: django-invborradologico:latest
- Artefacto guardado en GitHub Actions como django-docker-image
