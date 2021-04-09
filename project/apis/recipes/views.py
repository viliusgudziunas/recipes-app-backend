from flask_restx import Namespace, Resource
from project.apis.recipes.models import recipe
from project.apis.recipes.service import RecipeService

api = Namespace("recipes", description="Recipes related operations")
api.models["Recipe"] = recipe


@api.route("/")
class RecipesList(Resource):
    @api.doc("get_recipes_list")
    @api.marshal_list_with(recipe)
    def get(self):
        """List all recipes"""
        return RecipeService.get_all_recipes()
