# Write your solution here
def create_dictionary(fn):
  current_recipe = None
  recipes = {}
  with open(fn, 'r') as file:
    for line in file:
      line = line.strip()  # Remove leading/trailing whitespace

      if not line:  # Empty line indicates end of current recipe
        current_recipe = None
        continue

      if not current_recipe:
        # Start a new recipe
        current_recipe = line
        recipes[current_recipe] = {'time_taken': None, 'ingredients': []}
      elif current_recipe:
        # Add ingredients to current recipe
        if not recipes[current_recipe]['time_taken']:
          # First line after recipe name is time taken
          try:
            recipes[current_recipe]['time_taken'] = int(line)
          except ValueError:
            print(f"Error parsing time for recipe: {current_recipe}")
        else:
          # Add ingredients
          recipes[current_recipe]['ingredients'].append(line)
    return recipes

def search_by_name(fn,st):
  recipes = create_dictionary(fn)
  res = []
  for key in recipes:
    if st.lower() in key.lower():
      res.append(key)
  return res

def search_by_time(fn,prep_time):
  recipes = create_dictionary(fn)
  res = []
  for r in recipes:
    if recipes[r]['time_taken']<=prep_time:
      res.append(f"{r}, preparation time {recipes[r]['time_taken']} min")
  return res


def search_by_ingredient(fn,ing):
  recipes = create_dictionary(fn)
  res = []
  for r in recipes:
    if ing.lower() in recipes[r]['ingredients']:
      res.append(f"{r}, preparation time {recipes[r]['time_taken']} min")
  return res


found_recipes = search_by_name("recipes1.txt", "cake")

for recipe in found_recipes:
    print(recipe)

found_recipes = search_by_time("recipes1.txt", 20)
for recipe in found_recipes:
    print(recipe)

found_recipes = search_by_ingredient("recipes1.txt", "eggs")

for recipe in found_recipes:
    print(recipe)
