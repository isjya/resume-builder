import subprocess
import sys
import platform
import re
from pathlib import Path


# 错误信息映射表：编译错误 → 友好提示
ERROR_HINTS = [
    (
        re.compile(r"unexpected comma", re.IGNORECASE),
        "⚠️ 列表项中可能有未转义的特殊字符。\n"
        "   常见原因：C++ 应写为 C\\+\+，C# 应写为 C\\#。\n"
        "   参考：references/typst-caveats.md 第 7-27 行"
    ),
    (
        re.compile(r"cannot access fields on type array", re.IGNORECASE),
        "⚠️ project.with() 缺少 author 参数或格式错误。\n"
        "   正确格式：author: (name: \"你的姓名\")\n"
        "   参考：references/typst-caveats.md 第 121-125 行"
    ),
    (
        re.compile(r"the character .* is not valid in code", re.IGNORECASE),
        "⚠️ 文件中存在非法字符（可能是 BOM 或特殊编码）。\n"
        "   建议：用 Python 重新写入 .typ 文件，确保 UTF-8 无 BOM"
    ),
    (
        re.compile(r"expected expression", re.IGNORECASE),
        "⚠️ 表达式解析错误，可能是列表项中的特殊符号未转义。\n"
        "   检查：C++ → C\\+\+，C# → C\\#，括号改为逗号或空格。\n"
        "   参考：references/typst-caveats.md 第 7-42 行"
    ),
    (
        re.compile(r"failed to write PDF file", re.IGNORECASE),
        "⚠️ PDF 文件写入失败，通常是被其他程序占用。\n"
        "   解决：关闭 PDF 阅读器后重试"
    ),
    (
        re.compile(r"unclosed delimiter", re.IGNORECASE),
        "⚠️ 存在未闭合的定界符，可能是括号、引号不匹配。\n"
        "   检查：list item 中的括号是否改为了逗号或空格"
    ),
]


def get_typst_path():
    """Get typst executable path relative to this script's location"""
    script_dir = Path(__file__).parent.resolve()
    bin_dir = script_dir.parent / "assets" / "bin"
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
        error_msg = result.stderr
        print(f"Error: {error_msg}")

        # 遍历错误映射表，输出友好提示
        for pattern, hint in ERROR_HINTS:
            if pattern.search(error_msg):
                print(f"\n{hint}")
                break

        sys.exit(1)

    print(f"PDF generated: {pdf_file}")


if __name__ == "__main__":
    main()
