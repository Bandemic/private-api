from flask import Blueprint, request, Response, abort, current_app

contacts = Blueprint("v0.contacts", __name__, url_prefix="/v0/contacts")


@contacts.route("/report", methods=["POST"])
def report():
    abort(501)
    return Response(None, status=201)
