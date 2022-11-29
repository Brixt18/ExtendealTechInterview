import logging

from flask import make_response, request

from app.utils.scraping import Disco

from . import api_bp as bp
from app import auth

@bp.before_request
@auth.login_required
def before_request():
	pass


@bp.route("/disco", methods=["GET"])
def scraping_disco():
	# para fines de pruebas, la URI ya va ser la dada en la prueba, sin embargo se puede pasar por argumentos
	# www.api.com/?uri=xxxx
	# tener en cuenta que al ser scraping directo, esta funcion está diseñada especificamente para el website de Disco

	try:
		uri = request.args.get("uri", "https://www.disco.com.ar/electro/informatica")
		disco = Disco(uri)
		disco.get_items()

		resp = make_response(disco.records, 200)
		resp.headers["Content-Type"] = "application/json"

	except Exception as err:
		logging.error(err)
		return {}, 500

	return resp
