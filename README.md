# Tech Interview

Este proyecto es una API construida en [Flask](https://flask.palletsprojects.com/en/2.1.x/) para la entrevista ténica de Extendeal

* Parámetros a seguir:
* * Soporte para un endpoint `GET /`
* * Debe retornar (ejemplo):
```
{
    "records": [
        {
            "marca": "Lenovo",
            "descripcion": "Notebook Lenovo 14' Ip 3 I5 8g 256g",
            "precio": "114999"
        },
        {
            "marca": "Samsung",
            "descripcion": "Monitor Samsung 24' Fhd Lf24t350fhlczb",
            "precio": "54599"
        }
    ]
}
```

En orden de mantener privacidad y no es relevante para probar este proyecto, no incluiré otros parámetros que me han sido asignados a seguir.

## Instalación

Clonar el proyecto como normalmente clonas un proyecto de github.

```
$ git clone https://github.com/Brixt18/ExtendealTechInterview
```
O descargando el archivo .zip del mismo.

Una vez clonado el proyecto, **Crear** dentro de la carpeta `app/config` un archivo `.env` con las variables de entorno.
```
SECRET_KEY=MySuperSecretKey
```

## Requisitos
* [Python >= 3.7](https://www.python.org/downloads/release/python-370/)

## Dependencias
* Instalar usando pip
```
$ pip install -r requirements.txt
```
Incluye:
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [Requests](https://pypi.org/project/requests/)
* [Python-Dotenv](https://pypi.org/project/python-dotenv/)
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

## Cómo Usar

### Inicializar
Una vez instaladas todas las dependencias, ejecutar el archivo `run.py`
```
$ python run.py
```
Y la aplicación comenzará a ejectuar en entorno Local con el puerto 5000 (`localhost:5000`).

## Probar

### Localmente
Para verificar el enpoint, abrir en su navegador de preferencia, mientras al aplicación está ejecutandose, la URL: `localhost:5000/disco`, [o haga click aquí](http://localhost:5000/disco) y esta debería retonar un JSON con los parámetros establecidos anteriormente.


### En caso de errores:
En caso de no poder ejecutar la aplicación con el comando Python, intenté utilizar `$ python3 ...` o `$ python2 ..` etc, es decir: definir la versión. Esto suele suceder cuando hay varias versiones de python instaladas.