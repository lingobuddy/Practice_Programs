#!/usr/bin/env python3
#blue_tachikoma


ingredients1 = ["chicken", "broth", "garlic", "butter", "salt", "ginger", "potato", "mushrooms"]
newIngredient = ""

print("We're making a simple crockpot chicken recipe.\nRight now we have the following ingredients: {} ".format(ingredients1) + ".")

def addIngredient(newIngredient):
    newIngredient = str(input("Which ingredient do you wish to add?"))
    print(f"You want to add {newIngredient}. Got it!")
    ingredients1.append(newIngredient)      #add new ingredient to main recipe
    return newIngredient

def updateRecipe(ingredients1):
    return sorted(ingredients1)             #alphabetize the ingredients

def again():
    decision = ""
    def addmore(decision):
        print("Do you wish to add another ingredient?")
        decision = input("Y or N")
        return decision
    
    if decision == "Y" or "y":
        addIngredient(newIngredient)    
    if decision == "N" or "n":
        updateRecipe()
        newRecipe()
    elif decision != "Y" or "y" and decision != "N" or "n":
        print("Please enter your decision as either 'Y' or 'N' only.")
        addmore(decision)
    else:
        print("Please enter your decision as either Y or N.")

def newRecipe(ingredients1):
    print(f"The updated recipe now includes: {ingredients1}.")
    print("End recipe.")

addIngredient(newIngredient)
updateRecipe(ingredients1)
again()
newRecipe(ingredients1)


