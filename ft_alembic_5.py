"""Alembic 5: access the alchemy package with from-import."""
from alchemy import create_air


def main() -> None:
    """Test air creation through the package interface."""
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import...")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
