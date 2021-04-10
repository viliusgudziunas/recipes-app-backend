from flask import request
from flask_restx import Namespace, Resource
from project.apis.models import _bad_request, _not_found
from project.apis.recipes.dao import RecipeDAO
from project.apis.recipes.models import _recipe

api = Namespace("recipes", description="Recipes related operations")
api.models["Recipe"] = _recipe
dao = RecipeDAO()


@api.route("/")
class RecipesList(Resource):
    @api.doc("list_recipes")
    @api.marshal_list_with(fields=_recipe, description="Recipes list")
    def get(self):
        """List all recipes"""
        return dao.get_all()

    @api.doc("create_recipe")
    @api.expect(_recipe, validate=True)
    @api.response(code=201, model=_recipe, description="Recipe created")
    @api.response(code=400, model=_bad_request, description="Bad create recipe request")
    def post(self):
        """Create a new recipe"""
        data = request.json
        new_recipe = dao.create(data)
        return new_recipe.json, 201


@api.route("/<id>")
@api.param("id", "The recipe identifier")
@api.response(code=404, model=_not_found, description="Recipe not found")
class Recipe(Resource):
    @api.doc("get_recipe")
    @api.response(code=200, model=_recipe, description="Recipe")
    def get(self, id):
        """Get a recipe given its identifier"""
        recipe = dao.get(id)
        if not recipe:
            api.abort(404, id=id)

        return recipe.json

    @api.doc("update_recipe")
    @api.expect(_recipe)
    @api.response(code=200, model=_recipe, description="Recipe updated")
    def put(self, id):
        """Update a recipe given its identifier"""
        recipe = dao.get(id)
        if not recipe:
            api.abort(404, id=id)

        data = request.json
        updated_recipe = dao.update(recipe, data)
        return updated_recipe.json

    @api.doc("delete_recipe")
    @api.response(code=204, description="Recipe deleted")
    def delete(self, id):
        """Delete a recipe given its identifier"""
        recipe = dao.get(id)
        if not recipe:
            api.abort(404, id=id)

        dao.delete(recipe)
        return None, 204
