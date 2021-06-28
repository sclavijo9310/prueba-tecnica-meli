<p align="center">
  <h2 align="center">Prueba técnica MELI</h2>

  <p align="center">
    Este repositorio contiene la solución a la prueba "operación fuego de quasar" de MELI
  </p>
</p>

<details open="open">
  <summary><h2 style="display: inline-block">Contenidos</h2></summary>
  <ol>
    <li>
      <a href="#acerca-del-proyecto">Acerca de la prueba</a>
      <ul>
        <li><a href="#tecnologias-utilizadas">Tecnologías utilizadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#instalacion">Instalación</a>
    </li>
    <li><a href="#endpoints">Endpoints</a></li>
    <li><a href="#contacto">Contacto</a></li>
  </ol>
</details>

## Acerca del proyecto

En este proyecto se aborda la prueba técnica "operación fuego de quasar", abarcando los 3 niveles propuestos, se
despliega en Google App Engine con un entorno estándar "python39".

### Tecnologías utilizadas

* [Python 3](https://pyhton.org)
* [Flask](https://flask.palletsprojects.com/) - Framework para construir API Rest.
* [Localization](https://pypi.org/project/Localization/) - Dependencia usada entra otras cosas para realizar
  trilateración 2D.
  
## Prerequisitos

* Python 3

## Instalación

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
| DELETE  | /topsecret | Elimina los datos de distancia y mensaje en todos los satélites. |
| DELETE  | /topsecret-split/{nombre_satelite} | Elimina los datos de distancia y mensaje en el satélite definido en la URL. |

## Licencia

Licencia MIT.

## Contacto

Sergio Clavijo - [Página web](https://sergioclavijo.com) - <a href="mailto:sergioclavij@gmail.com">
sergioclavij@gmail.com</a>

Url proyecto: [https://github.com/sclavijo9310/prueba-tecnica-meli](https://github.com/sclavijo9310/prueba-tecnica-meli)