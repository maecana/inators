import sys
import traceback

try:
    import deidleranator
except ImportError as e:
    print("Failed to import deidleranator!", file=sys.stderr)
    print(f"Error: {e}", file=sys.stderr)
    input("Press Enter to exit...")
    sys.exit(1)

if __name__ == "__main__":
    try:
        print("Running initiated...")
        print("Press Ctrl+C to exit...")
        deidleranator.main()
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print("An unexpected error occurred while running the script.", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        input("Press Enter to exit...")

