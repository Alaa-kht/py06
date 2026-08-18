"""Distillation 1: potions through the package interface."""
import alchemy


def main() -> None:
    """Brew the strength potion and the heal() package alias."""
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")


if __name__ == "__main__":
    main()
