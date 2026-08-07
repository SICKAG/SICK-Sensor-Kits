from pathlib import Path
import subprocess
import sys

project_root = Path(__file__).resolve().parents[2]

translator = project_root / "docs" / "scripts" / "translate_markdown_test.py"

source_base = project_root / "docs" / "en"
target_base = project_root / "docs" / "de"


def translate_file(source_file, target_file):
    source_arg = source_file.relative_to(project_root).as_posix()
    target_arg = target_file.relative_to(project_root).as_posix()

    print()
    print(f"Translating: {source_arg}")
    print(f"Target:      {target_arg}")

    subprocess.run(
        [sys.executable, str(translator), source_arg, target_arg],
        check=True,
    )


def translate_folder(source_folder, target_folder):
    markdown_files = sorted(source_folder.rglob("*.md"))
    total_files = len(markdown_files)

    print(f"Found {total_files} Markdown files.")

    for index, source_file in enumerate(markdown_files, start=1):
        relative_path = source_file.relative_to(source_folder)
        target_file = target_folder / relative_path

        percent = round((index / total_files) * 100, 1)

        print()
        print("------------------------------------------------------------")
        print(f"File {index}/{total_files} ({percent}%): {relative_path}")
        print(f"Remaining: {total_files - index}")

        translate_file(source_file, target_file)

    print()
    print("------------------------------------------------------------")
    print(f"Finished translating {total_files} Markdown files.")


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 0 or args[0] == "--all":
        translate_folder(source_base, target_base)

    elif len(args) == 1:
        selection = args[0]

        source_path = source_base / selection
        target_path = target_base / selection

        if source_path.is_file():
            translate_file(source_path, target_path)

        elif source_path.is_dir():
            translate_folder(source_path, target_path)

        else:
            raise FileNotFoundError(f"Not found in docs/en: {selection}")

    else:
        print("Usage:")
        print("  py docs/scripts/translate_all.py")
        print("  py docs/scripts/translate_all.py --all")
        print("  py docs/scripts/translate_all.py vision")
        print("  py docs/scripts/translate_all.py faq.md")