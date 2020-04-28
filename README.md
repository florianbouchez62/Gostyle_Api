<h1 align="center">
  <br>
  <img src="https://github.com/florianbouchez62/Gostyle_Api/blob/develop/REST_Server/api/static/logo.png" alt="GoStyle" width="200">
  <br>
  GoStyle API
  <br>
</h1>

<h4 align="center">Api for Gostyle application.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#how-to-use-it">How To Use</a> •
  <a href="#usage-example">Usage example</a> •
  <a href="#license">License</a>
</p>

## Key Features

* Admin panel (create/update promotions)
* get all promotions.
* get single promotion.

## Requirements

There is some requirements to use it ...

* Python3 & Pip3
* Django latest version
* MySql

## How to use it

* Windows

```sh
# Clone this repository.
git clone https://github.com/florianbouchez62/Gostyle_Api.git

# Create python environment and run it.
python3 -m env name_env
name_env/bin/activate

# Go into the repository.
cd Gostyle_api/REST_server/api

# Install requirements.
pip3 install -r requirements.txt

# You need to start mysql and create REST_Server/api/.env
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

# You need to create the migrations file.
python3 manage.py makemigrations

# After this, migrate it
python3 manage.py migrate

# If its the first time, you can run this to load defaults datas.
python3 manage.py loaddata fixtures/initial_data.json

# Now its time to run it.
python3 manage.py runserver
```

* OS X & Linux

```sh
# Clone this repository.
git clone https://github.com/florianbouchez62/Gostyle_Api.git

# Create python environment and run it.
python3 -m env name_env
source name_env/bin/activate

# Go into the repository.
cd Gostyle_api/REST_server/api

# Install requirements.
pip3 install -r requirements.txt

# You need to start mysql and create REST_Server/api/.env
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

# You need to create the migrations file.
python3 manage.py makemigrations

# After this, migrate it
python3 manage.py migrate

# If its the first time, you can run this to load defaults datas.
python3 manage.py loaddata fixture/initial_data.json

# Now its time to run it.
python3 manage.py runserver
```

## Usage example

Ajouter des captures d'écran.

## License

> [@florianbouchez62](https://github.com/florianbouchez62) &nbsp;&middot;&nbsp;
> [@lucaslemaire](https://github.com/lucaslemaire) &nbsp;&middot;&nbsp;
> [@Maximus40](https://github.com/Maximus40) &nbsp;&middot;&nbsp;
> [@Azelaek](https://github.com/Azelaek) &nbsp;&middot;&nbsp;
> [@fkiecken](https://github.com/fkiecken) &nbsp;&middot;&nbsp;
