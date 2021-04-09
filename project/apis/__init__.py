from flask_restx import Api
from project.apis.recipes.views import api as recipes_ns

api = Api(
    title="Recipes API",
    version="0.1",
    description="Register and retrieve random recipes"
)

api.add_namespace(recipes_ns, path="/recipes")
