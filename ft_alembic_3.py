"""Alembic 3:access alchemy/elements.py with from-import."""
from alchemy.elements import create_air


def main() -> None:
    """test aire creation through a from-import on the submodule."""
    print("=== Alembic 3 ===")
    print(
        "Accessing alchemy/elements.py using "
        "'from ... import ...' structure")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
