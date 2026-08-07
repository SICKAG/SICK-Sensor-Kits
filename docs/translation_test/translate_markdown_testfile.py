from pathlib import Path
import os
import re
import json
import urllib.request

docs_dir = Path(__file__).resolve().parents[1]

input_file = docs_dir / "translation_test" / "input.md"
output_file = docs_dir / "translation_test" / "output.de.md"

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
DEEPL_API_URL = os.getenv("DEEPL_API_URL", "https://api-free.deepl.com/v2/translate")


def translate_with_deepl(text):
    if not text.strip():
        return text

    if not DEEPL_API_KEY:
        raise RuntimeError("DEEPL_API_KEY is not set.")

    data = json.dumps({
        "text": [text],
        "source_lang": "EN",
        "target_lang": "DE",
        "preserve_formatting": True,
    }).encode("utf-8")

    request = urllib.request.Request(
        DEEPL_API_URL,
        data=data,
        headers={
            "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["translations"][0]["text"]


def protect_inline_parts(line):
    protected = []

    def save(match):
        placeholder = f"__PROTECTED_{len(protected)}__"
        protected.append(match.group(0))
        return placeholder

    # Inline code
    line = re.sub(r"`[^`\n]+`", save, line)

    # URLs inside normal text
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

    # Standalone file/image/link paths
    if re.match(
        r"^(\.\./|\./)?[\w\-/ .]+\.(md|jpg|jpeg|png|gif|svg|webp|pdf|zip)(\{.*\})?$",
        stripped,
        re.IGNORECASE,
    ):
        return True

    # Standalone URLs
    if stripped.startswith("http://") or stripped.startswith("https://") or stripped.startswith("www."):
        return True

    # HTML-only lines
    if stripped.startswith("<") and stripped.endswith(">"):
        return True

    return False


def translate_visible_text(text):
    safe_text, protected = protect_inline_parts(text)
    translated = translate_with_deepl(safe_text)
    return restore_inline_parts(translated, protected)


def process_line(line):
    if should_skip(line):
        return line

    # Headings
    match = re.match(r"^(#{1,6}\s+)(.*)$", line)
    if match:
        return match.group(1) + translate_visible_text(match.group(2))

    # Bullet lists
    match = re.match(r"^(\s*[-*+]\s+)(.*)$", line)
    if match:
        return match.group(1) + translate_visible_text(match.group(2))

    # Numbered lists
    match = re.match(r"^(\s*\d+\.\s+)(.*)$", line)
    if match:
        return match.group(1) + translate_visible_text(match.group(2))

    # Normal text
    return translate_visible_text(line)


text = input_file.read_text(encoding="utf-8")
lines = text.splitlines()

output = []
inside_code_block = False

for line in lines:
    if line.strip().startswith("```"):
        inside_code_block = not inside_code_block
        output.append(line)
        continue

    if inside_code_block:
        output.append(line)
    else:
        output.append(process_line(line))

output_file.write_text("\n".join(output), encoding="utf-8")

print(f"Created {output_file}")