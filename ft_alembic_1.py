"""Alembic 1: access elements.py with from-import."""
from elements import create_water


def main() -> None:
    """test water creation through a from-import."""
    print("=== Alembic1 ===")
    print("Using'from...import...' structure to access elements.py")
    print(f"Testing create_water: {create_water()}")


if __name__ == "__main__":
    main()
