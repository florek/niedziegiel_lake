import re
import html
from pathlib import Path

import markdown

import lake

ROOT = Path(__file__).resolve().parent.parent
LAKES = [
    (lid, name.replace("Jezioro ", "", 1))
    for lid, name in sorted(lake.LAKES.items())
]
DOCS_ROOT = [
    ("docs/model.md", "Model"),
]
LAKE_DOCS = [
    ("raport_podsumowujacy.md", "Raport podsumowujący"),
    ("podsumowanie_ewaluacji.md", "Podsumowanie ewaluacji"),
    ("prognoza.md", "Prognoza 12 mies."),
    ("szanse_odbudowy.md", "Szanse na odbudowę"),
    ("drenaz_miesieczny.md", "Drenaż miesięczny"),
    ("zanik_drenazu.md", "Zanik drenażu"),
]


def _slug(path: str) -> str:
    s = path.replace(".md", "").replace("/", "-").replace("_", "-")
    return re.sub(r"[^a-z0-9-]", "", s.lower())


def _md_to_html(md_path: Path, base_path: str) -> str:
    if not md_path.exists():
        return "<p class=\"placeholder\">Brak pliku.</p>"
    raw = md_path.read_text(encoding="utf-8")
    html_out = markdown.markdown(raw, extensions=["tables", "fenced_code"])
    if base_path:
        html_out = re.sub(
            r'<img([^>]+)src="([^"]+)"',
            lambda m: f'<img{m[1]}src="{base_path}{m[2]}"' if not (m[2].startswith("http") or m[2].startswith("data:")) else m[0],
            html_out,
        )
    return html_out


def _nav_item(section_id: str, label: str, is_active: bool) -> str:
    active = " active" if is_active else ""
    return f'<li class="leaf"><a href="#{section_id}" class="nav-link{active}">{html.escape(label)}</a></li>'


def _nav_tree() -> tuple[str, str]:
    parts = []
    parts.append(_nav_item("readme", "README", True))
    parts.append('<li class="branch open"><span class="label"><span class="twist">▶</span> docs</span>')
    parts.append("<ul>")
    for path, label in DOCS_ROOT:
        sid = _slug(path)
        parts.append(_nav_item(sid, label, False))
    for lake_id, lake_name in LAKES:
        parts.append(f'<li class="branch"><span class="label"><span class="twist">▶</span> {html.escape(lake_name)}</span><ul>')
        for file_name, doc_label in LAKE_DOCS:
            sid = _slug(f"docs/{lake_id}/{file_name}")
            parts.append(_nav_item(sid, doc_label, False))
        parts.append("</ul></li>")
    parts.append("</ul></li>")
    return "", "".join(parts)


def _content_sections() -> str:
    sections = []
    readme_path = ROOT / "README.md"
    sections.append(f'<div id="readme" class="panel" style="display:block"><div class="content-inner">{_md_to_html(readme_path, "")}</div></div>')
    for path, _ in DOCS_ROOT:
        sid = _slug(path)
        base = path.replace("/[^/]+.md$", "/")
        base = path[: path.rfind("/") + 1] if "/" in path else ""
        full = ROOT / path
        sections.append(f'<div id="{sid}" class="panel" style="display:none"><div class="content-inner">{_md_to_html(full, base)}</div></div>')
    for lake_id, _ in LAKES:
        for file_name, _ in LAKE_DOCS:
            path = f"docs/{lake_id}/{file_name}"
            sid = _slug(path)
            base = f"docs/{lake_id}/"
            full = ROOT / path
            sections.append(f'<div id="{sid}" class="panel" style="display:none"><div class="content-inner">{_md_to_html(full, base)}</div></div>')
    return "\n".join(sections)


def build() -> None:
    _, nav_html = _nav_tree()
    content_html = _content_sections()
    first_id = "readme"
    out = f"""<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <title>Prognoza poziomu jezior – dokumentacja</title>
  <style>
    :root {{
      --bg: #f6f8fa;
      --sidebar: #eaeef2;
      --sidebar-hover: #dde1e6;
      --text: #1f2328;
      --text-muted: #57606a;
      --accent: #0969da;
      --accent-soft: rgba(9, 105, 218, 0.1);
      --border: #d0d7de;
      --code-bg: #eaeef2;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: "Segoe UI", system-ui, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; }}
    .layout {{ display: flex; min-height: 100vh; }}
    .sidebar {{ width: 280px; min-width: 280px; background: var(--sidebar); border-right: 1px solid var(--border); overflow-y: auto; padding: 1rem 0; }}
    .sidebar h2 {{ font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted); margin: 0 1rem 0.75rem; padding-bottom: 0.25rem; }}
    .tree ul {{ list-style: none; margin: 0; padding-left: 0; }}
    .tree > ul {{ padding-left: 0; }}
    .tree li {{ margin: 0; }}
    .tree .branch > .label {{ cursor: pointer; padding: 0.35rem 1rem; display: flex; align-items: center; gap: 0.35rem; color: var(--text-muted); font-size: 0.9rem; user-select: none; }}
    .tree .branch > .label:hover {{ background: var(--sidebar-hover); color: var(--text); }}
    .tree .branch.open > .label {{ color: var(--text); }}
    .tree .branch .twist {{ font-size: 0.7rem; transition: transform 0.15s ease; }}
    .tree .branch.open > .label .twist {{ transform: rotate(90deg); }}
    .tree .branch ul {{ padding-left: 1.25rem; border-left: 1px solid var(--border); margin-left: 0.75rem; }}
    .tree .leaf a {{ display: block; padding: 0.4rem 1rem; color: var(--text); text-decoration: none; font-size: 0.9rem; border-left: 2px solid transparent; }}
    .tree .leaf a:hover {{ background: var(--sidebar-hover); color: var(--accent); }}
    .tree .leaf a.active {{ background: var(--accent-soft); color: var(--accent); border-left-color: var(--accent); }}
    .main {{ flex: 1; overflow-y: auto; padding: 2rem 3rem 4rem; }}
    .main .content {{ max-width: 900px; margin: 0 auto; }}
    .main .content h1 {{ font-size: 1.75rem; margin-top: 0; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; }}
    .main .content h2 {{ font-size: 1.35rem; margin-top: 1.5rem; }}
    .main .content h3 {{ font-size: 1.15rem; margin-top: 1.25rem; }}
    .main .content p {{ margin: 0.75rem 0; }}
    .main .content ul, .main .content ol {{ margin: 0.75rem 0; padding-left: 1.5rem; }}
    .main .content pre, .main .content code {{ background: var(--code-bg); border-radius: 6px; font-size: 0.9em; }}
    .main .content pre {{ padding: 1rem; overflow-x: auto; }}
    .main .content code {{ padding: 0.2em 0.4em; }}
    .main .content pre code {{ padding: 0; }}
    .main .content table {{ border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.9rem; }}
    .main .content th, .main .content td {{ border: 1px solid var(--border); padding: 0.5rem 0.75rem; text-align: left; }}
    .main .content th {{ background: var(--sidebar); }}
    .main .content img {{ max-width: 100%; height: auto; border-radius: 6px; margin: 0.5rem 0; }}
    .main .content blockquote {{ border-left: 4px solid var(--accent); margin: 1rem 0; padding-left: 1rem; color: var(--text-muted); }}
  </style>
</head>
<body>
  <div class="layout">
    <nav class="sidebar">
      <h2>Nawigacja</h2>
      <div class="tree"><ul>{nav_html}</ul></div>
    </nav>
    <main class="main">
      <div id="content" class="content">{content_html}</div>
    </main>
  </div>
  <script>
(function() {{
  var panels = document.querySelectorAll(".panel");
  var links = document.querySelectorAll(".nav-link");
  function show(id) {{
    panels.forEach(function(p) {{ p.style.display = p.id === id ? "block" : "none"; }});
    links.forEach(function(a) {{ a.classList.toggle("active", a.getAttribute("href") === "#" + id); }});
    var branch = document.querySelector('.leaf a[href="#' + id + '"]');
    if (branch) {{
      var p = branch.closest(".branch");
      if (p) p.classList.add("open");
    }}
  }}
  function onHash() {{ var id = (location.hash || "#readme").slice(1); if (id && document.getElementById(id)) show(id); }}
  links.forEach(function(a) {{
    a.addEventListener("click", function(e) {{ e.preventDefault(); location.hash = this.getAttribute("href").slice(1); onHash(); }});
  }});
  window.addEventListener("hashchange", onHash);
  onHash();
}})();
  </script>
</body>
</html>"""
    (ROOT / "index.html").write_text(out, encoding="utf-8")
    print("Zapisano:", ROOT / "index.html")


if __name__ == "__main__":
    build()
