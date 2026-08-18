"""Dark magic validator: module-level import closes the circle."""
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Check that at least one allowed ingredient is present."""
    allowed = dark_spell_allowed_ingredients()
    if any(item in ingredients.lower() for item in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
