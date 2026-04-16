import subprocess
import sys
import platform
from pathlib import Path


def get_typst_path():
    """Get typst executable path based on current platform"""
    bin_dir = Path("assets/bin")
    system = platform.system()

    if system == "Windows":
        return bin_dir / "typst.exe"
    elif system == "Darwin":
        return bin_dir / "typst"
    else:
        raise RuntimeError(f"Unsupported platform: {system}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python make_resume.py <file.typ>")
        sys.exit(1)

    typ_file = Path(sys.argv[1])
    if not typ_file.exists():
        print(f"Error: file not found: {typ_file}")
        sys.exit(1)

    typst_path = get_typst_path()
    if not typst_path.exists():
        print(f"Error: typst not found at {typst_path}")
        print("Please run: python scripts/install_deps.py")
        sys.exit(1)

    # Get output PDF path (same name as typ file, in current directory)
    pdf_file = Path.cwd() / typ_file.with_suffix(".pdf").name

    print(f"Compiling {typ_file} -> {pdf_file}")
    result = subprocess.run(
        [str(typst_path), "compile", str(typ_file), str(pdf_file)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)

    print(f"PDF generated: {pdf_file}")


if __name__ == "__main__":
    main()
