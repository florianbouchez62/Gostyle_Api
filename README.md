<h1 align="center">
  <img src="https://github.com/florianbouchez62/Gostyle_Api/blob/develop/REST_Server/api/static/mspr_logo.png">
</h1>

<div align="center">

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)
<br />
![Contributors](https://img.shields.io/badge/contributors-5-red)
![GitHub last commit](https://img.shields.io/github/last-commit/florianbouchez62/Gostyle_Api?color=red)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-red.svg)

</div>

> The API offers a service for managing promotions for a company. It notably allows to communicate the list of promotions or the information of a particular promotion.

> The source code is open so that you can download the source code and set it up with ease if you would like to have your own exclusive environment.

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#folder-structure">Folder Structure</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#how-to-use-it">How To Use</a> •
  <a href="#usage-example">Usage example</a> •
  <a href="#license">License</a>
</p>

## Key Features

* Admin panel (create/update promotions)
* get all promotions.
* get single promotion.

## Folder Structure

    .
    ├── .github/workflows
    ├── REST_Server
        ├── api
            ├── fixture                             # Contain file to pre-generate objects
            ├── media                               # All promotions images and generated Qrcode
            ├── api                                 # Default module 
            ├── promotion                           # Promotion module
            ├── static                              # Images
            ├── templates/rest_framework            # Rest_framework base template
            ├── manage.py                           # Django's commande-line utility
            ├── requirements.txt                    # All of the dependencies
    ├── README.md

## Requirements

There is some requirements to use it ...

* Python3 & Pip3
* Django latest version
* MySql

## How to use it

```sh
# Clone this repository.
git clone https://github.com/florianbouchez62/Gostyle_Api.git

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

#You can pre populate the database with
python3 manage.py loaddata Fixture/inital_data.json

# Now its time to run it.
python3 manage.py runserver you_ip  your_port
```

## Usage example

Ajouter des captures d'écran.

## License

> [@florianbouchez62](https://github.com/florianbouchez62) &nbsp;&middot;&nbsp;
> [@lucaslemaire](https://github.com/lucaslemaire) &nbsp;&middot;&nbsp;
> [@Maximus40](https://github.com/Maximus40) &nbsp;&middot;&nbsp;
> [@Azelaek](https://github.com/Azelaek) &nbsp;&middot;&nbsp;
> [@fkiecken](https://github.com/fkiecken) &nbsp;&middot;&nbsp;
