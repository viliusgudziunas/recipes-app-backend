from project.apis.recipes.models import Recipe
from project.extensions import db


class RecipeService:
    @staticmethod
    def get_all_recipes():
        return Recipe.query.all()

    @staticmethod
    def get_recipe(id):
        return Recipe.query.filter_by(id=id).first()

    @staticmethod
    def create_recipe(data):
        new_recipe = Recipe(name=data.get("name"),
                            description=data.get("description"))
        save_changes(new_recipe)
        return new_recipe.json, 201


def save_changes(data):
    db.session.add(data)
    db.session.commit()
