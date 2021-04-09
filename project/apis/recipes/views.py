from flask import request
from flask_restx import Namespace, Resource
from project.apis.recipes.models import recipe as _recipe
from project.apis.recipes.service import RecipeService

api = Namespace("recipes", description="Recipes related operations")
api.models["Recipe"] = _recipe


@api.route("/")
class RecipesList(Resource):
    @api.doc("get recipes list")
    @api.marshal_list_with(_recipe)
    def get(self):
        """List all recipes"""
        return RecipeService.get_all_recipes()

    @api.doc("create a new recipe")
    @api.expect(_recipe, validate=True)
    @api.response(201, "Recipe successfully created.")
    def post(self):
        """Create a new recipe"""
        data = request.json
        return RecipeService.create_recipe(data)


@api.route("/<id>")
@api.param("id", "The recipe identifier")
@api.response(404, "Recipe not found.")
class Recipe(Resource):
    @api.doc("get a recipe")
    @api.marshal_with(_recipe)
    def get(self, id):
        """Get a user given its identifier"""
        recipe = RecipeService.get_recipe(id)
        if not recipe:
            api.abort(404)

        return recipe
