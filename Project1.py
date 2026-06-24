class Recipe:
    def __init__(self,recipe,Ingredients,cooking_time,Instructions):
        self.recipe=recipe
        self.Ingredients=Ingredients
        self.cooking_time=cooking_time
        self.Instructions=Instructions


    def display_recipe(self):
     print(f"Name:{self.recipe}")
     print(f"Ingredients:{self.Ingredients}")
     print(f"Cooking Time : {self.cooking_time}")
     print(f"Instructions:{self.Instructions}")

def create_recipe():

    print("Welcon to recipe collection ")
    recipe=input("Enter recipe name :")
    Ingredients=input("Enter Ingredients (comma-separated):")
    cooking_time=input("Enter cooking time :")
    Instructions=input("Enter cooking Instructions :")


    return Recipe(recipe,Ingredients,cooking_time,Instructions)







Recipe1=create_recipe()
print("Display recipe ....")

Recipe1.display_recipe()
