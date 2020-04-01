from flask import Blueprint, request, Response, abort, current_app

cases = Blueprint("v0.cases", __name__, url_prefix="/v0/cases")


@cases.route("/report", methods=["POST"])
def report():
    abort(501)
    return Response(None, status=201)
