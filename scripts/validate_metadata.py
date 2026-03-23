from pathlib import Path
import sys
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "force-app"


def collect_xml_files() -> list[Path]:
    return sorted(SOURCE_DIR.rglob("*.xml"))


def validate_xml(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for file in files:
        try:
            ET.parse(file)
        except ET.ParseError as exc:
            errors.append(f"{file.relative_to(ROOT)}: {exc}")
    return errors


def main() -> int:
    if not SOURCE_DIR.exists():
        print("force-app directory not found", file=sys.stderr)
        return 1

    xml_files = collect_xml_files()
    if not xml_files:
        print("No metadata XML files found in force-app", file=sys.stderr)
        return 1

    errors = validate_xml(xml_files)
    if errors:
        print("Metadata XML validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(xml_files)} metadata XML files successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
