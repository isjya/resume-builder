import urllib.request
import zipfile
import os
import shutil
import tarfile
import platform
from pathlib import Path


def get_platform_info():
    """Returns (filename, url, extract_dir, exe_name) for current platform"""
    version = "v0.14.2"
    system = platform.system()

    if system == "Windows":
        filename = "typst-x86_64-pc-windows-msvc.zip"
        url = f"https://github.com/typst/typst/releases/download/{version}/{filename}"
        extract_dir = "typst-x86_64-pc-windows-msvc"
        exe_name = "typst.exe"
    elif system == "Darwin":
        machine = platform.machine()
        if machine == "arm64":
            filename = "typst-aarch64-apple-darwin.tar.xz"
        else:
            filename = "typst-x86_64-apple-darwin.tar.xz"
        url = f"https://github.com/typst/typst/releases/download/{version}/{filename}"
        extract_dir = filename.replace(".tar.xz", "")
        exe_name = "typst"
    else:
        raise RuntimeError(f"Unsupported platform: {system}")

    return filename, url, extract_dir, exe_name


def download_typst(max_retries=3):
    """Download typst compiler to assets/bin/"""
    filename, url, extract_dir, exe_name = get_platform_info()

    script_dir = Path(__file__).parent.resolve()
    bin_dir = script_dir.parent / "assets" / "bin"
    bin_dir.mkdir(parents=True, exist_ok=True)

    archive_path = bin_dir / filename
    exe_path = bin_dir / exe_name

    # Cleanup leftover files from previous failed downloads
    if archive_path.exists():
        os.remove(archive_path)
    extract_path = bin_dir / extract_dir
    if extract_path.exists():
        shutil.rmtree(extract_path)

    # Check if already installed
    if exe_path.exists():
        print(f"typst already exists at {exe_path}")
        return

    for attempt in range(max_retries):
        print(f"Downloading {url}... (attempt {attempt + 1}/{max_retries})")
        try:
            urllib.request.urlretrieve(url, archive_path)
            break
        except urllib.error.ContentTooShortError:
            if attempt < max_retries - 1:
                print("Download incomplete, retrying...")
                os.remove(archive_path)
            else:
                raise

    print(f"Extracting to {bin_dir}...")
    if filename.endswith(".zip"):
        with zipfile.ZipFile(archive_path, 'r') as z:
            z.extractall(bin_dir)
    else:
        with tarfile.open(archive_path, 'r:xz') as z:
            z.extractall(bin_dir)

    # Move typst from subfolder to assets/bin
    extracted_exe = extract_path / exe_name
    if extracted_exe.exists():
        shutil.copy2(extracted_exe, exe_path)
        shutil.rmtree(extract_path)

    os.remove(archive_path)
    print(f"typst installed to {exe_path}")


if __name__ == "__main__":
    download_typst()
