# GCP Bucket Creator 🪣

Script de Python para crear buckets en Google Cloud Storage (GCS) desde la línea de comandos.

## ¿Qué hace?

Recibe el nombre de un bucket como argumento y lo crea automáticamente en GCP
con clase de almacenamiento `STANDARD` en la región `us-east1`.

## Requisitos previos

### 1. Cuenta de GCP
Necesitas una cuenta de Google Cloud Platform (puedes usar la capa gratuita).
- Crea tu cuenta en: https://cloud.google.com/

### 2. Google Cloud SDK
Instala el SDK de GCP para desarrolladores locales:
- Descárgalo en: https://cloud.google.com/sdk/docs/install

Verifica la instalación con:
```bash
gcloud --version
```

### 3. Autenticación
Inicia sesión con tu cuenta de Google para autenticar el acceso local a GCP:
```bash
gcloud auth application-default login
```
Esto abrirá el navegador para que autorices el acceso.

### 4. Dependencias de Python
Instala la librería oficial de Google Cloud Storage:
```bash
pip install google-cloud-storage
```

## Uso
```bash
python create_bucket.py <nombre-del-bucket>
```

### Ejemplo
```bash
python create_bucket.py mi-bucket-prueba
```

Salida esperada:
```
Bucket name received: mi-bucket-prueba
Bucket mi-bucket-prueba created in US-EAST1 with STANDARD
```

## Notas

- Los nombres de buckets en GCP son **globalmente únicos**, por lo que si el nombre
  ya existe (de cualquier usuario en el mundo), el script dará error.
- La región está configurada como `us-east1` y la clase como `STANDARD`.
  Puedes modificarlas directamente en el script según tus necesidades.
- Desarrollado y probado usando la **capa gratuita de GCP**.
