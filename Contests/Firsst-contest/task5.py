def find_top_allergies(k, **allergens):
    return [allergen for allergen, value in allergens.items() if value > k]
