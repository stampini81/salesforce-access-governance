from pathlib import Path
import json
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / ".github" / "workflows" / "ci.yml",
    ROOT / ".github" / "workflows" / "salesforce-org-validation.yml",
    ROOT / "sfdx-project.json",
    ROOT / "manifest" / "package.xml",
    ROOT / "docs" / "superbadge-implementation-report.md",
]


def validate_sfdx_project() -> list[str]:
    issues: list[str] = []
    project_file = ROOT / "sfdx-project.json"
    try:
        data = json.loads(project_file.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"sfdx-project.json is not valid JSON: {exc}"]

    if "packageDirectories" not in data:
        issues.append("sfdx-project.json is missing packageDirectories")
    if "sourceApiVersion" not in data:
        issues.append("sfdx-project.json is missing sourceApiVersion")
    return issues


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_PATHS:
        if not path.exists():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")

    errors.extend(validate_sfdx_project())

    if errors:
        print("Repository structure validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Repository structure validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
