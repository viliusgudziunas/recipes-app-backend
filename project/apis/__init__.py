from flask_restx import Api
from project.apis.models import _bad_request, _not_found
from project.apis.recipes.views import api as recipes_ns

api = Api(
    title="Recipes API",
    version="0.1",
    description="Register and retrieve random recipes",
)

api.models["BadRequest"] = _bad_request
api.models["NotFound"] = _not_found
api.add_namespace(recipes_ns, path="/recipes")
