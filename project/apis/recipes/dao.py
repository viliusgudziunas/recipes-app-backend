from project.apis.recipes.models import Recipe
from project.db import commit_db_changes, delete_data, save_changes


class RecipeDAO:
    def get_all(self):
        return Recipe.query.all()

    def get(self, id):
        return Recipe.query.filter_by(id=id).first()

    def create(self, data):
        new_recipe = Recipe(name=data.get("name"), description=data.get("description"))
        save_changes(new_recipe)
        return new_recipe

    def update(self, recipe, data):
        name = data.get("name")
        if name is not None:
            recipe.name = name

        description = data.get("description")
        if description is not None:
            recipe.description = description

        commit_db_changes()
        return recipe

    def delete(self, recipe):
        delete_data(recipe)
