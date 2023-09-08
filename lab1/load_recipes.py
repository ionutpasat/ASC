import os

"""
	Bonus task: load all the available coffee recipes from the folder 'recipes/'
	File format:
		first line: coffee name
		next lines: resource=percentage

	info and examples for handling files:
		http://cs.curs.pub.ro/wiki/asc/asc:lab1:index#operatii_cu_fisiere
		https://docs.python.org/3/library/io.html
		https://docs.python.org/3/library/os.path.html
"""

RECIPES_FOLDER = "recipes"

def load_coffee_recipes():
    coffee_recipes = {}
    for recipe_file in os.listdir(RECIPES_FOLDER):
        recipe_path = os.path.join(RECIPES_FOLDER, recipe_file)
        with open(recipe_path) as f:
            recipe_name = os.path.splitext(recipe_file)[0]
            recipe_contents = f.read().strip().split("\n")
            recipe_dict = {}
            for item in recipe_contents[1:]:
                resource, amount = item.split("=")
                recipe_dict[resource.strip()] = int(amount.strip())
            coffee_recipes[recipe_name] = recipe_dict
    return coffee_recipes
