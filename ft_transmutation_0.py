"""Transmutation 0: import the recipes file directly."""
import alchemy.transmutation.recipes


def main() -> None:
    """Transmute lead into gold via the full module path."""
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    gold = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {gold}")


if __name__ == "__main__":
    main()
