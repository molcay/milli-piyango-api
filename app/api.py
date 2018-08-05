from flask import Blueprint
from flask import jsonify
from milli_piyango import MilliPiyango as mP


api = Blueprint('api', __name__)


def get_result(expression):
    return jsonify(expression)


@api.route("/api/v1/games", methods=['GET'])
def games():
    return get_result(mP.GAME_LIST)


@api.route("/api/v1/draw_dates/<string:game>", methods=['GET'])
def draw_dates(game):
    return get_result(mP().get_draw_dates(game))


@api.route("/api/v1/results/<string:game>/<string:date>", methods=['GET'])
def results(game, date):
    return get_result(mP().get_result(game, date))


@api.route("/api/v1/piyango/<string:date>/<string:ticket_no>", methods=['GET'])
def check_lottery(date, ticket_no):
    return get_result(mP().get_result_for_piyango(date, ticket_no))
