# Ejercicio Flask con CI/CD en la nube

Este es el mismo ejercicio de Redes 2: `main.py` responde `Página de Prueba`
en la ruta `/`. La aplicación se ejecuta con Docker y Gunicorn.

Aplicación pública: https://redes2web.onrender.com/

## Flujo automático

1. Un push a `main` activa el workflow `Docker Image CI` de GitHub Actions.
2. El workflow instala las dependencias y prueba la respuesta original de Flask.
3. Construye la imagen Docker y comprueba la respuesta HTTP del contenedor.
4. Publica `vicky2606/redes2:flaskv2` y una etiqueta con el SHA del commit en Docker Hub.
5. Render espera a que pasen los checks de CI y despliega el mismo commit desde su Dockerfile.
6. Render comprueba la salud de la aplicación en `/`.

La configuración de referencia de Render está en `render.yaml`.
El servicio usa el plan Free y la región Oregon. Puede tardar en responder
después de un período de inactividad.

## Prueba de la aplicación

```sh
pip install -r requirements.txt
python -m unittest discover -s tests -v
```

## Ejecución con Docker

```sh
docker build -t redes2web .
docker run --rm -p 5000:5000 redes2web
```

El token de Docker Hub permanece en el secreto `TOKEN_DE_ACCESO` de GitHub Actions.
No se guardan credenciales en el código.
