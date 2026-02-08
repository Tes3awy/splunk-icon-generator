from flask import Blueprint

bp = Blueprint("error", __name__, template_folder="templates")

from app.error import handler  # noqa: E402, F401
