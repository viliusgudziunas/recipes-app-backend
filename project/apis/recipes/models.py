from datetime import datetime

from flask_restx import Model, fields
from project.extensions import db

_recipe = Model(
    "Recipe",
    {
        "id": fields.Integer,
        "name": fields.String(
            required=True, description="Recipe name", min_length=1, max_length=64
        ),
        "description": fields.String(description="Recipe description", max_length=512),
        "created_on": fields.DateTime(description="Date when recipe was created"),
        "updated_on": fields.DateTime(description="Date when recipe was last updated"),
    },
)


class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(512))
    created_on = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    updated_on = db.Column(
        db.DateTime(), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    @property
    def json(self):
        return {"id": self.id, "name": self.name, "description": self.description}
