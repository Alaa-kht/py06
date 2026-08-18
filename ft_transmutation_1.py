"""Transmutation 1: import the transmutation module directly."""
import alchemy.transmutation


def main() -> None:
    """Transmute lead into gold via the subpackage interface."""
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    gold = alchemy.transmutation.lead_to_gold()
    print(f"Testing lead to gold: {gold}")


if __name__ == "__main__":
    main()
