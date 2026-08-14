from pathlib import Path
import os
import re
import json
import sys
import urllib.request


# ------------------------------------------------------------
# PATHS
# ------------------------------------------------------------

project_root = Path(__file__).resolve().parents[2]
docs_dir = Path(__file__).resolve().parents[1]

if len(sys.argv) == 3:
    input_file = project_root / sys.argv[1]
    output_file = project_root / sys.argv[2]
else:
    input_file = docs_dir / "translation_test" / "input.md"
    output_file = docs_dir / "translation_test" / "output.de.md"


# ------------------------------------------------------------
# DEEPL API KEY
# ------------------------------------------------------------

def load_deepl_key():
    env_key = os.getenv("DEEPL_API_KEY")
    if env_key:
        return env_key

    auth_file = project_root / "auth_key.json"

    if auth_file.exists():
        with auth_file.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if "deepl" in data:
            return data["deepl"]

        if "DEEPL_API_KEY" in data:
            return data["DEEPL_API_KEY"]

        if "auth_key" in data:
            return data["auth_key"]

    return None


DEEPL_API_KEY = load_deepl_key()
DEEPL_API_URL = os.getenv(
    "DEEPL_API_URL",
    "https://api-free.deepl.com/v2/translate"
)


# ------------------------------------------------------------
# DEEPL TRANSLATION
# ------------------------------------------------------------

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


def translate_html_with_deepl(html):  
    if not html.strip():  
        return html

    if not DEEPL_API_KEY:  
        raise RuntimeError("DEEPL_API_KEY is not set.")

    data = json.dumps({  
        "text": [html],  
        "source_lang": "EN",  
        "target_lang": "DE",  
        "preserve_formatting": True,  
        "tag_handling": "html",         # ← neu [[2]](6a7acedcfebb606cb1177635)  
        "ignore_tags": ["code", "pre"], # ← neu [[1]](6a7acedcfebb606cb1177631)  
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



# ------------------------------------------------------------
# INLINE PROTECTION
# ------------------------------------------------------------

def protect_inline_parts(line):
    protected = []

    def save_value(value):
        placeholder = f"__PROTECTED_{len(protected)}__"
        protected.append(value)
        return placeholder

    def save_match(match):
        return save_value(match.group(0))

    # Protect inline code: `py src/main.py`
    line = re.sub(r"`[^`\n]+`", save_match, line)

    # Protect complete Markdown images and links:
    # path/to/image.jpg
    # [ttps://example.com
    # [Button](page.md){ .md-button }
    re.sub(
        r"!\[[^\]]*\]\([^)]+\)(?:\{[^}]+\})?|\[[^\]]+\]\([^)]+\)(?:\{[^}]+\})?",
        save_match,
        line,
)

    # Protect URLs inside normal text
    line = re.sub(r"(https?://[^\s]+|www\.[^\s]+)", save_match, line)

    # Protect Material/MkDocs attributes
    line = re.sub(r"\{[^{}\n]+\}", save_match, line)

    return line, protected


def restore_inline_parts(line, protected):
    for index, value in enumerate(protected):
        line = line.replace(f"__PROTECTED_{index}__", value)

    return line


def translate_visible_text(text):
    safe_text, protected = protect_inline_parts(text)
    translated = translate_with_deepl(safe_text)
    return restore_inline_parts(translated, protected)


# ------------------------------------------------------------
# SKIP LOGIC
# ------------------------------------------------------------

def should_skip(line):
    stripped = line.strip()

    if stripped == "":
        return True

    # Standalone file/image/page paths
    if re.fullmatch(
        r"(\.\./|\./)?[\w\-/ .]+\.(md|jpg|jpeg|png|gif|svg|webp|pdf|zip)(\{.*\})?",
        stripped,
        re.IGNORECASE,
    ):
        return True

    # Standalone URLs
    if (
        stripped.startswith("http://")
        or stripped.startswith("https://")
        or stripped.startswith("www.")
    ):
        return True

    # Structural HTML-only lines.
    # Do not skip td/th because these may contain translatable text.
    if stripped.startswith("<") and stripped.endswith(">"):
        if stripped.startswith("<td") or stripped.startswith("<th"):
            return False
        return True

    return False


def should_translate_text(text):
    stripped = text.strip()

    if stripped == "":
        return False

    # Skip pure numbers, part numbers and separators
    if re.fullmatch(r"[0-9\s/.,-]+", stripped):
        return False

    # Translate only if letters exist
    return bool(re.search(r"[A-Za-zÄÖÜäöüß]", stripped))


# ------------------------------------------------------------
# MKDOCS ADMONITIONS / DETAILS
# ------------------------------------------------------------

def translate_admonition_or_details(line):
    """
    Keeps MkDocs syntax unchanged:
    !!! note "Title"
    ??? info "Title"
    ???+ example "Title"

    Only the visible title is translated.
    """

    stripped = line.strip()

    if not (
        stripped.startswith("!!! ")
        or stripped.startswith("??? ")
        or stripped.startswith("???+ ")
    ):
        return None

    # No title in quotes, keep line unchanged
    if '"' not in line and "„" not in line and "“" not in line:
        return line

    normalized = line.replace("„", '"').replace("“", '"')

    first_quote = normalized.find('"')
    last_quote = normalized.rfind('"')

    if first_quote == -1 or last_quote == -1 or first_quote == last_quote:
        return line

    marker = normalized[:first_quote].rstrip()
    title = normalized[first_quote + 1:last_quote]

    translated_title = translate_visible_text(title).strip()

    translated_title = translated_title.strip('"')
    translated_title = translated_title.strip("„")
    translated_title = translated_title.strip("“")

    return f'{marker} "{translated_title}"'


# ------------------------------------------------------------
# HTML TABLE CELLS
# ------------------------------------------------------------

def translate_html_table_cell(line):
    """
    Translates simple table cells:
    <td>Power supply</td>
    <th>Article Description</th>

    Keeps tags and pure numbers unchanged.
    """

    match = re.match(
        r"^(\s*<(td|th)(?:\s+[^>]*)?>)(.*?)(</\2>\s*)$",
        line,
    )

    if not match:
        return None

    opening_tag = match.group(1)
    content = match.group(3)
    closing_tag = match.group(4)

    parts = re.split(r"(<br\s*/?>)", content)
    translated_parts = []

    for part in parts:
        if re.fullmatch(r"<br\s*/?>", part):
            translated_parts.append(part)
        elif should_translate_text(part):
            translated_parts.append(translate_visible_text(part))
        else:
            translated_parts.append(part)

    return opening_tag + "".join(translated_parts) + closing_tag


# ------------------------------------------------------------
# MARKDOWN LINKS AND IMAGES
# ------------------------------------------------------------

def translate_markdown_link_or_image(line):
    """
    Translates only the visible text of Markdown links or image alt text.

    Examples:
    ./vision_getting_started.md
    ../images/vision.jpg
    """

    match = re.match(
        r"^(\s*)(!?)(\[)([^\]]*)(\]\()([^)]+)(\))(\{[^}]+\})?(\s*)$",
        line,
    )

    if not match:
        return None

    leading = match.group(1)
    bang = match.group(2)
    open_bracket = match.group(3)
    visible_text = match.group(4)
    middle = match.group(5)
    target = match.group(6)
    close_parenthesis = match.group(7)
    attributes = match.group(8) or ""
    trailing = match.group(9)

    if visible_text.strip():
        translated_visible_text = translate_visible_text(visible_text)
    else:
        translated_visible_text = visible_text

    return (
        leading
        + bang
        + open_bracket
        + translated_visible_text
        + middle
        + target
        + close_parenthesis
        + attributes
        + trailing
    )


def rewrite_relative_paths(line, source_file, target_file, target_language="de"):
    """
    Rewrites relative paths after translating a Markdown file.

    Examples:
    Source file:
        docs/vision/vision_overview.md

    Target file:
        docs/de/vision/vision_overview_test.md

    Image path:
        ../images/vision.jpg
        -> ../../images/vision.jpg

    Internal Markdown link:
        ./vision_getting_started.md
        -> vision_getting_started.md
    """

    def is_external_path(path):
        return (
            path.startswith("http://")
            or path.startswith("https://")
            or path.startswith("www.")
            or path.startswith("#")
            or path.startswith("mailto:")
        )

    def convert_path(old_path):
        if is_external_path(old_path):
            return old_path

        # Preserve anchor links, e.g. page.md#section
        if "#" in old_path:
            path_without_anchor, anchor = old_path.split("#", 1)
            anchor = "#" + anchor
        else:
            path_without_anchor = old_path
            anchor = ""

        if path_without_anchor == "":
            return old_path

        # Resolve old path relative to original English source file
        absolute_old_target = (source_file.parent / path_without_anchor).resolve()

        # Only rewrite paths that are inside docs/
        try:
            relative_to_docs = absolute_old_target.relative_to(docs_dir.resolve())
        except ValueError:
            return old_path

        suffix = absolute_old_target.suffix.lower()

        # Internal Markdown page links should point into docs/de/
        if suffix == ".md":
            parts = list(relative_to_docs.parts)

            # If path already starts with de/ or en/, replace language prefix
            if parts and parts[0] in ["de", "en"]:
                parts[0] = target_language
                absolute_new_target = docs_dir.joinpath(*parts)
            else:
                absolute_new_target = docs_dir / target_language / relative_to_docs

        # Assets like images/files stay where they are
        else:
            absolute_new_target = absolute_old_target

        # Calculate the correct relative path from the German target file
        new_relative_path = os.path.relpath(
            absolute_new_target,
            start=target_file.parent,
        )

        # Important for Markdown/web paths
        new_relative_path = new_relative_path.replace("\\", "/")

        return new_relative_path + anchor

    # Rewrite Markdown links and images:
    # path
    # path
    # path{ .md-button }
    def replace_markdown_link(match):
        prefix = match.group(1)
        old_target = match.group(2)
        attributes = match.group(3) or ""

        new_target = convert_path(old_target)

        return f"{prefix}({new_target}){attributes}"

    line = re.sub(
        r"(!?\[[^\]]*\])\(([^)]+)\)(\{[^}]+\})?",
        replace_markdown_link,
        line,
    )

    # Rewrite standalone paths:
    # ../images/vision.jpg
    # ./vision_getting_started.md{ .md-button }
    def replace_standalone_path(match):
        leading_spaces = match.group(1)
        old_target = match.group(2)
        attributes = match.group(3) or ""

        new_target = convert_path(old_target)

        return f"{leading_spaces}{new_target}{attributes}"

    line = re.sub(
        r"^(\s*)((?:\.\./|\./)?[\w\-/. ]+\.(?:md|jpg|jpeg|png|gif|svg|webp|pdf|zip))(\{[^}]+\})?\s*$",
        replace_standalone_path,
        line,
        flags=re.IGNORECASE,
    )

    return line


# ------------------------------------------------------------
# LINE PROCESSING
# ------------------------------------------------------------

def process_line(line):
    if should_skip(line):
        return line

    admonition_result = translate_admonition_or_details(line)
    if admonition_result is not None:
        return admonition_result

    table_result = translate_html_table_cell(line)
    if table_result is not None:
        return table_result

    markdown_link_result = translate_markdown_link_or_image(line)
    if markdown_link_result is not None:
        return markdown_link_result

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

    return translate_visible_text(line)


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------

if not input_file.exists():
    raise FileNotFoundError(f"Input file not found: {input_file}")

print(f"Translating: {input_file}")
print(f"Target file: {output_file}")
print("Please wait. This may take a moment...")

text = input_file.read_text(encoding="utf-8")
lines = text.splitlines()

output = []
inside_code_block = False
inside_style_block = False
inside_script_block = False
inside_strategy_block = False
strategy_lines = []
strategy_depth = 0 

HTML_BLOCK_CLASSES = ("strategy-grid", "requirement-box") 

for index, line in enumerate(lines, start=1):
    print(f"\rProcessed {index}/{len(lines)} lines...", end="", flush=True)

    stripped = line.strip()

    # --- strategy-grid Block mit Tiefenzählung (NEU, ganz oben) ---  
    # --- benutzerdefinierte HTML-Blöcke (strategy-grid, requirement-box, ...) ---  
    if not inside_strategy_block and stripped.startswith("<div class="):  
        # Prüfen, ob eine der bekannten Block-Klassen vorkommt  
        if any(f'"{cls}' in stripped or f' {cls}' in stripped for cls in HTML_BLOCK_CLASSES):  
            inside_strategy_block = True  
            strategy_lines = [line]  
            strategy_depth = line.count("<div") - line.count("</div>")  
            if strategy_depth <= 0:  
                output.append(translate_html_with_deepl("\n".join(strategy_lines)))  
                inside_strategy_block = False  
                strategy_lines = []  
                strategy_depth = 0  
            continue  


    if inside_strategy_block:  
        strategy_lines.append(line)  
        # Tiefe aktualisieren: jede öffnende erhöht, jede schließende senkt  
        strategy_depth += line.count("<div")  
        strategy_depth -= line.count("</div>")

        # Block ist erst geschlossen, wenn die Tiefe wieder 0 (oder darunter) ist  
        if strategy_depth <= 0:  
            block_html = "\n".join(strategy_lines)  
            output.append(translate_html_with_deepl(block_html))  
            inside_strategy_block = False  
            strategy_lines = []  
            strategy_depth = 0  
        continue

    if stripped.lower().startswith("<style"):
        inside_style_block = True
        output.append(line)
        continue

    if inside_style_block:
        output.append(line)

        if stripped.lower().startswith("</style"):
            inside_style_block = False

        continue

    if stripped.lower().startswith("<script"):
        inside_script_block = True
        output.append(line)
        continue

    if inside_script_block:
        output.append(line)

        if stripped.lower().startswith("</script"):
            inside_script_block = False

        continue

    if stripped.startswith("```"):
        inside_code_block = not inside_code_block
        output.append(line)
        continue

    if inside_code_block:
        output.append(line)
        continue

    processed_line = process_line(line)
    output.append(processed_line)

print()

output_file.parent.mkdir(parents=True, exist_ok=True)

temp_output_file = output_file.with_suffix(output_file.suffix + ".tmp")

print("Translation finished. Writing temporary file...")
temp_output_file.write_text("\n".join(output), encoding="utf-8")

print("Replacing final output file...")
temp_output_file.replace(output_file)

print(f"Created {output_file}")
