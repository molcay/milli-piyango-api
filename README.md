# _(Unofficial)_ Milli Piyango API

You can retrieve information about 5 different game (listed below) results from [Milli Piyango](http://www.mpi.gov.tr/).

* Piyango: [Game Spec](http://www.mpi.gov.tr/?q=node/1) | [Results](http://www.mpi.gov.tr/sonuclar/_cs_piyango.php)
* Sayısal Loto: [Game Spec](http://www.mpi.gov.tr/node/73?q=node/33) | [Results](http://www.mpi.gov.tr/sonuclar/_cs_sayisal.php)
* Şans Topu: [Game Spec](http://www.mpi.gov.tr/node/73?q=node/31) | [Results](http://www.mpi.gov.tr/sonuclar/_cs_sanstopu.php)
* On Numara: [Game Spec](http://www.mpi.gov.tr/node/73?q=node/8) | [Results](http://www.mpi.gov.tr/sonuclar/_cs_onnumara.php)
* Süper Loto: [Game Spec](http://www.mpi.gov.tr/node/73?q=node/32) | [Results](http://www.mpi.gov.tr/sonuclar/_cs_superloto.php)


### Usage:
This project come with a Dockerfile. You can deploy it anywhere you want(Google Cloud Platform, etc.) or simple use it locally

### Dependencies:
* [Flask](http://flask.pocoo.org/)
* [MilliPiyango](https://github.com/molcay/milli-piyango/)

### Usage:
* clone this repository:
```shell
git clone https://github.com/molcay/milli-piyango-api 
```

* change directory to `milli-piyango-api`:
```shell
cd milli-piyango-api
```

* create virtual environment and install dependencies:
```shell
python3 -m venv myvenv # create virtual environment

source myvenv/bin/activate # activate virtual environment

pip install -r requirements.txt # install dependencies
```

* now, you can start application:
```shell
python app/main.py
```

### Endpoints:

#### _GET_ `/api/v1/games`
TODO: write this

#### _GET_ `/api/v1/draw_dates/<game>`
TODO: write this

#### _GET_ `/api/v1/results/<game>/<date>`
TODO: write this

#### _GET_ `/api/v1/piyango/<date>/<ticket_no>`
TODO: write this

