"""Light magic spellbook: safe from circular explosions."""
from alchemy.grimoire.light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients allowed in light magic."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record the spell if its ingredients are valid."""
    result = validate_ingredients(ingredients)
    if result.endswith("- VALID"):
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
