#!/usr/bin/env python3
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
MODS_YML = ROOT / "data" / "mods.yml"
SERVERS_YML = ROOT / "data" / "servers.yml"

def escape(text: str) -> str:
    if text is None: return ""
    return str(text).replace("|", "\\|").replace("\n", " ").strip()

def load_yaml(path: Path) -> list:
    if not path.exists(): return []
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data or []

def build_mods_table(mods: list) -> str:
    if not mods: return "_No mods yet. Be the first to add one!_"
    lines = ["| Name | Author | Category | Link | Status |", "|------|--------|----------|------|--------|"]
    for mod in mods:
        name = escape(mod.get("name", ""))
        author = escape(mod.get("author", ""))
        category = escape(mod.get("category", ""))
        status = escape(mod.get("status", ""))
        links = mod.get("links") or []
        link_str = " / ".join(f"[{escape(l.get('name', 'Link'))}]({l.get('url', '#')})" for l in links) if links else "-"
        lines.append(f"| {name} | {author} | {category} | {link_str} | {status} |")
    return "\n".join(lines)

def build_servers_table(servers: list) -> str:
    if not servers: return "_No servers yet. Be the first to add one!_"
    lines = ["| Name | Region | Address | Version | Status |", "|------|--------|---------|---------|--------|"]
    for srv in servers:
        name = escape(srv.get("name", ""))
        region = escape(srv.get("region", ""))
        address = escape(srv.get("address", ""))
        version = escape(srv.get("version", ""))
        status = escape(srv.get("status", ""))
        lines.append(f"| {name} | {region} | `{address}` | {version} | {status} |")
    return "\n".join(lines)

def replace_between(content: str, start: str, end: str, new: str) -> str:
    start_idx = content.find(start)
    end_idx = content.find(end)
    if start_idx == -1 or end_idx == -1:
        raise ValueError(f"Markers not found in README: {start} / {end}")
    before = content[: start_idx + len(start)]
    after = content[end_idx:]
    return f"{before}\n{new}\n{after}"

def main() -> int:
    if not README.exists():
        print("ERROR: README.md not found"); return 1
    mods = load_yaml(MODS_YML)
    servers = load_yaml(SERVERS_YML)
    content = README.read_text(encoding="utf-8")
    content = replace_between(content, "<!-- MODS_START -->", "<!-- MODS_END -->", build_mods_table(mods))
    content = replace_between(content, "<!-- SERVERS_START -->", "<!-- SERVERS_END -->", build_servers_table(servers))
    README.write_text(content, encoding="utf-8")
    print(f"OK: generated tables ({len(mods)} mods, {len(servers)} servers)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
