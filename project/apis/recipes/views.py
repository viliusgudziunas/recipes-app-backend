from flask import request
from flask_restx import Namespace, Resource
from project.apis.recipes.dao import RecipeDAO
from project.apis.recipes.model import recipe as _recipe

api = Namespace("recipes", description="Recipes related operations")
api.models["Recipe"] = _recipe
dao = RecipeDAO()


@api.route("/")
class RecipesList(Resource):
    @api.doc("list_recipes")
    @api.marshal_list_with(_recipe)
    def get(self):
        """List all recipes"""
        return dao.get_all()

    @api.doc("create_recipe")
    @api.expect(_recipe, validate=True)
    @api.response(201, "Recipe successfully created.")
    def post(self):
        """Create a new recipe"""
        data = request.json
        new_recipe = dao.create(data)
        return new_recipe.json, 201


@api.route("/<id>")
@api.param("id", "The recipe identifier")
@api.response(404, "Recipe not found.")
class Recipe(Resource):
    @api.doc("get_recipe")
    @api.marshal_with(_recipe)
    def get(self, id):
        """Get a user given its identifier"""
        recipe = dao.get(id)
        if not recipe:
            api.abort(404)

        return recipe

    @api.doc("delete_recipe")
    @api.response(200, "Recipe deleted")
    def delete(self, id):
        """Delete a user given its identifier"""
        recipe = dao.get(id)
        if not recipe:
            api.abort(404)

        dao.delete(recipe)
        response = {"message": "Recipe deleted", "id": id}
        return response, 200
