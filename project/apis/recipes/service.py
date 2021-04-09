from project.apis.recipes.models import Recipe


class RecipeService:
    @staticmethod
    def get_all_recipes():
        return Recipe.query.all()
