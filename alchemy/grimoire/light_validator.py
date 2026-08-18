"""Light magic validator: deferred import breaks the circle."""


def validate_ingredients(ingredients: str) -> str:
    """Check that at least one allowed ingredient is present."""
    from alchemy.grimoire.light_spellbook import (
        light_spell_allowed_ingredients,
    )

    allowed = light_spell_allowed_ingredients()
    if any(item in ingredients.lower() for item in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
