from project.apis.recipes.model import Recipe
from project.db import delete_data, save_changes


class RecipeDAO:
    def get_all(self):
        return Recipe.query.all()

    def get(self, id):
        return Recipe.query.filter_by(id=id).first()

    def create(self, data):
        new_recipe = Recipe(name=data.get("name"),
                            description=data.get("description"))
        save_changes(new_recipe)
        return new_recipe

    def delete(self, recipe):
        delete_data(recipe)
