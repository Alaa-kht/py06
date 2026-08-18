"""Alembic 2: access alchemy/elemnts.py with import structure."""
import alchemy.elements


def main() -> None:
    """test earth creation through the package submodule."""
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")


if __name__ == "__main__":
    main()
