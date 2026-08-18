"""Dark magic spellbook: explodes from circular imports."""
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients allowed in dark magic."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Record the spell if its ingredients are valid."""
    result = validate_ingredients(ingredients)
    if result.endswith("- VALID"):
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
