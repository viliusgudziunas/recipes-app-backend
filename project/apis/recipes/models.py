from flask_restx import Model, fields
from project.extensions import db

recipe = Model("Recipe", {
    "name": fields.String(required=True, description="Recipe name"),
    "description": fields.String(description="Recipe description"),
})


class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(512))
