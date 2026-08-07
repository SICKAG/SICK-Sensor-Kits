from pathlib import Path
import re

docs_dir = Path(__file__).resolve().parents[1]

input_file = docs_dir / "translation_test" / "input.md"
output_file = docs_dir / "translation_test" / "output.de.md"


def protect_inline_parts(line):
    protected = []

    def save(match):
        placeholder = f"__PROTECTED_{len(protected)}__"
        protected.append(match.group(0))
        return placeholder

    # Protect inline code like `py src/main.py`
    line = re.sub(r"`[^`\n]+`", save, line)

    # Protect URLs starting with https://, http:// or www.
    line = re.sub(r"(https?://[^\s]+|www\.[^\s]+)", save, line)

    return line, protected


def restore_inline_parts(line, protected):
    for i, value in enumerate(protected):
        line = line.replace(f"__PROTECTED_{i}__", value)
    return line


def should_skip(line):
    stripped = line.strip()

    if stripped == "":
        return True

    # Do not change standalone image/file/link paths
    if re.match(
        r"^(\.\./|\./)?[\w\-/ .]+\.(md|jpg|jpeg|png|gif|svg|webp|pdf|zip)(\{.*\})?$",
        stripped,
        re.IGNORECASE,
    ):
        return True

    # Do not change standalone URLs
    if stripped.startswith("http://") or stripped.startswith("https://") or stripped.startswith("www."):
        return True

    # Do not change HTML-only lines
    if stripped.startswith("<") and stripped.endswith(">"):
        return True

    return False


def mark_text(line):
    protected_line, protected_parts = protect_inline_parts(line)

    # Headings
    match = re.match(r"^(#{1,6}\s+)(.*)$", protected_line)
    if match:
        result = f"{match.group(1)}[DE] {match.group(2)}"
        return restore_inline_parts(result, protected_parts)

    # Bullet lists
    match = re.match(r"^(\s*[-*+]\s+)(.*)$", protected_line)
    if match:
        result = f"{match.group(1)}[DE] {match.group(2)}"
        return restore_inline_parts(result, protected_parts)

    # Numbered lists
    match = re.match(r"^(\s*\d+\.\s+)(.*)$", protected_line)
    if match:
        result = f"{match.group(1)}[DE] {match.group(2)}"
        return restore_inline_parts(result, protected_parts)

    # Normal text
    result = f"[DE] {protected_line}"
    return restore_inline_parts(result, protected_parts)


text = input_file.read_text(encoding="utf-8")
lines = text.splitlines()

output = []
inside_code_block = False

for line in lines:
    if line.strip().startswith("```"):
        inside_code_block = not inside_code_block
        output.append(line)
        continue

    if inside_code_block or should_skip(line):
        output.append(line)
    else:
        output.append(mark_text(line))

output_file.write_text("\n".join(output), encoding="utf-8")

print(f"Created {output_file}")