"""Kaboom 1: dark magic explodes on a circular import."""


def main() -> None:
    """Trigger the circular import of the dark spellbook."""
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(f"Testing: {dark_spell_record('Doom', 'bats and arsenic')}")


if __name__ == "__main__":
    main()
