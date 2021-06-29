<p align="center">
  <h2 align="center">Prueba técnica MELI</h2>

  <p align="center">
    Este repositorio contiene la solución a la prueba "operación fuego de quasar" de MELI
  </p>
</p>

##Contenidos
<summary><h2 style="display: inline-block">Contenidos</h2></summary>
<ol>
  <li>
    <a href="#acerca-del-proyecto">Acerca de la prueba</a>
    <ul>
      <li><a href="#tecnologías-utilizadas">Tecnologías utilizadas</a></li>
    </ul>
  </li>
  <li>
    <a href="#instalación">Instalación</a>
    <ul>
      <li><a href="#prerequisitos">Prerequisitos</a></li>
      <li><a href="#pasos">Pasos</a></li>
    </ul>
  </li>
  <li><a href="#endpoints">Endpoints</a></li>
  <li><a href="#ambiente-de-pruebas-en-google-cloud">Ambiente de pruebas en Google Cloud</a></li>
  <li><a href="#licencia">Licencia</a></li>
  <li><a href="#contacto">Contacto</a></li>
</ol>

## Acerca del proyecto

En este proyecto se aborda la prueba técnica "operación fuego de quasar", abarcando los 3 niveles propuestos, se
despliega en Google App Engine con un entorno estándar "python39".

### Tecnologías utilizadas

* [Python 3](https://pyhton.org)
* [Flask](https://flask.palletsprojects.com/) - Framework para construir API Rest.
* [Localization](https://pypi.org/project/Localization/) - Dependencia usada entra otras cosas para realizar
  trilateración 2D.

## Instalación

### Prerequisitos

* Python 3

###Pasos

1. Clonar repositorio
   ```sh
   git clone https://github.com/sclavijo9310/prueba-tecnica-meli.git
   ```
2. Instalar dependencias
   ```sh
   pip install -r requirements.txt
   ```
3. Ejecutar el proyecto
   ```sh
   python main.py
   ```

## Endpoints

| Método | Url | Descripción |
| ------------- | ------------- | ------------- |
| GET  | /topsecret-split | Devuelve datos de ubicación y mensaje de la nave portacarga imperial. |
| POST  | /topsecret | Establecer valores de distancia y mensaje para los satélites, devuelve datos de ubicación y mensaje de la nave portacarga imperial. |
| POST  | /topsecret-split  | Establecer valores de distancia y mensaje para los satélites, devuelve datos de ubicación y mensaje de la nave portacarga imperial. |
| POST  | /topsecret-split/{nombre_satelite} | Establecer valores de distancia y mensaje para el satélite definido en la URL. |
| DELETE  | /topsecret-split/{nombre_satelite} | Elimina los datos de distancia y mensaje en el satélite definido en la URL. |

##Ambiente de pruebas en Google Cloud

Se realizó despligue de ambiente para pruebas en Google Cloud, usando App Egnine (Datastore para los servicios de nivel 3), URL:
* [prueba-meli.ml](https://prueba-meli.ml) ó [prueba-tecnica-meli.ue.r.appspot.com](https://prueba-tecnica-meli.ue.r.appspot.com)

## Licencia

Licencia MIT.

## Contacto

Sergio Clavijo - [Página web](https://sergioclavijo.com) - <a href="mailto:sergioclavij@gmail.com">
sergioclavij@gmail.com</a>

Url proyecto: [https://github.com/sclavijo9310/prueba-tecnica-meli](https://github.com/sclavijo9310/prueba-tecnica-meli)