from flask import Flask, render_template
from api import api

app = Flask(__name__)


@app.route("/")
def index():
    games = [
        {
            "name": "Piyango",
            "specLink": "http://www.mpi.gov.tr/?q=node/1",
            "resultLink": "http://www.mpi.gov.tr/sonuclar/_cs_piyango.php"
        },
        {
            "name": "Sayısal Loto",
            "specLink": "http://www.mpi.gov.tr/node/73?q=node/33",
            "resultLink": "http://www.mpi.gov.tr/sonuclar/_cs_sayisal.php"
        },
        {
            "name": "Şans Topu",
            "specLink": "http://www.mpi.gov.tr/node/73?q=node/31",
            "resultLink": "http://www.mpi.gov.tr/sonuclar/_cs_sanstopu.php"
        },
        {
            "name": "On Numara",
            "specLink": "http://www.mpi.gov.tr/node/73?q=node/8",
            "resultLink": "http://www.mpi.gov.tr/sonuclar/_cs_onnumara.php"
        },
        {
            "name": "Süper Loto",
            "specLink": "http://www.mpi.gov.tr/node/73?q=node/32",
            "resultLink": "http://www.mpi.gov.tr/sonuclar/_cs_superloto.php"
        }
    ]
    return render_template('index.html', games=games)


app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
