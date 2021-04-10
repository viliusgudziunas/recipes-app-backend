"""Shared API models"""
from flask_restx import Model, fields
from project.apis.utils import DictItem

_not_found = Model(
    "NotFound",
    {"id": fields.Integer(readOnly=True), "message": fields.String(readOnly=True)},
)

_bad_request = Model(
    "BadRequest",
    {"errors": DictItem(attribute="errors"), "message": fields.String(readOnly=True)},
)
