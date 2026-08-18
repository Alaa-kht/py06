"""Alembic 0: access elements.py with the import structure."""
import elements


def main() -> None:
    """test fire creation through a plain import."""
    print("=== Alembic 0 ===")
    print("Using: 'import...' structure to access elements.py")
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    main()
