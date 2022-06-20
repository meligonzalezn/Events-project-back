# Install virtual env

```
virtualenv venv
python3 -m pip install --user virtualenv
source venv/bin/activate
```


# Para activar las variables de estado. 
```
source secret.env 
```


# Install requirenments
```
pip install -r requirements.txt 
```

## Install memcache on ubuntu

```
sudo apt update
sudo apt install memcached
sudo systemctl start memcached
```

### Possible bugs

1. Error: Packages doesn't found. Only is required access to links appear on error message, then download and install .deb package.

## Install memcache on ubuntu

sudo apt update
sudo apt install memcached
sudo systemctl start memcached

### Possible bugs

1. Error: Packages doesn't found. Only is required access to links appear on error message, then download and install .deb package.

# Errores en la instalación
Si instalar psycopg2 da error, solucionar usando el siguiente comando:

sudo apt install libpq-dev

La solución puede depender del paquete libpq5, por tanto, si el error es el siguiente: 
 "libpq-dev : Depende: libpq5 (= 12.11-0ubuntu0.20.04.1) pero 14.3-1.pgdg20.04+1 está instalado"
 
Se soluciona con (esto por fuera del virtualenv): 

sudo apt-get install libpq5=12.11-0ubuntu0.20.04.1

sudo apt-get install libpq-dev 

