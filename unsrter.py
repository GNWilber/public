#!/usr/bin/env python3
"""
SRT Tool — interactive subtitle translation helper.
Just run: python srt_tool.py
"""

import re
import math
from pathlib import Path

BLOCK_SEP = "|||"
CHUNK_SIZE = 4000  # characters per chunk


# ── helpers ────────────────────────────────────────────────────────────────────

def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    try:
        answer = input(f"{prompt}{suffix}: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nAborted.")
        raise SystemExit
    return answer if answer else default


def pick(prompt: str, options: list) -> int:
    """Show a numbered list and return the chosen index."""
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        raw = ask(prompt)
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return int(raw) - 1
        print(f"  Enter a number between 1 and {len(options)}.")


def scan(ext: str) -> list[Path]:
    return sorted(Path(".").glob(f"*{ext}"))


# ── core logic ─────────────────────────────────────────────────────────────────

def parse_srt(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8-sig")
    raw_blocks = re.split(r"\n\s*\n", text.strip())
    blocks = []
    for raw in raw_blocks:
        lines = raw.strip().splitlines()
        if len(lines) < 3:
            continue
        blocks.append({
            "index": lines[0].strip(),
            "timestamp": lines[1].strip(),
            "lines": lines[2:],
        })
    return blocks


def build_text_lines(blocks: list[dict]) -> list[str]:
    return [BLOCK_SEP.join(l.strip() for l in b["lines"]) for b in blocks]


def split_into_chunks(lines: list[str], max_chars: int) -> list[list[str]]:
    """Split lines into chunks that don't exceed max_chars each.
    Never splits a subtitle block across chunks."""
    chunks, current, current_len = [], [], 0
    for line in lines:
        line_len = len(line) + 1  # +1 for newline
        if current and current_len + line_len > max_chars:
            chunks.append(current)
            current, current_len = [], 0
        current.append(line)
        current_len += line_len
    if current:
        chunks.append(current)
    return chunks


# ── modes ──────────────────────────────────────────────────────────────────────

def do_export():
    print()
    srt_files = scan(".srt")
    if not srt_files:
        print("✗ No .srt files found in current folder.")
        return
    if len(srt_files) == 1:
        srt_path = srt_files[0]
        print(f"Found: {srt_path}")
    else:
        print("Found .srt files:")
        idx = pick("Which file to export?", [f.name for f in srt_files])
        srt_path = srt_files[idx]

    blocks = parse_srt(srt_path)
    lines = build_text_lines(blocks)
    total_chars = sum(len(l) for l in lines)
    stem = srt_path.stem

    print(f"\n  {len(blocks)} subtitle blocks — {total_chars:,} characters total")

    do_chunks = ask("\nSplit into chunks? (y/n)", "n").lower() == "y"

    if do_chunks:
        chunks = split_into_chunks(lines, CHUNK_SIZE)
        n = len(chunks)
        # token estimate: ~4 chars per token; plus ~400 prompt tokens input overhead
        tokens_in  = CHUNK_SIZE // 4 + 400
        tokens_out = CHUNK_SIZE // 4          # translated output ≈ same size
        cost_per   = tokens_in * 3e-6 + tokens_out * 15e-6  # Sonnet 4.6 pricing
        print(f"\n  → {n} chunk(s) of up to {CHUNK_SIZE:,} chars each")
        print(f"  → ~{tokens_in} input + ~{tokens_out} output tokens per chunk")
        print(f"  → ~${cost_per:.4f} per chunk  (~${cost_per * n:.3f} total)")
        print(f"     (Claude Sonnet 4.6: $3/Mtok in · $15/Mtok out)\n")

        pad = len(str(n))
        for i, chunk in enumerate(chunks, 1):
            out_path = Path(f"{stem}_chunk{str(i).zfill(pad)}.txt")
            out_path.write_text("\n".join(chunk) + "\n", encoding="utf-8")
            print(f"  ✓ {out_path}  ({sum(len(l) for l in chunk):,} chars, {len(chunk)} blocks)")
        print(f"\n✓ Exported {n} chunk(s)")
    else:
        out_path = Path(f"{stem}.txt")
        out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"\n✓ Exported → {out_path}")


def do_inject():
    print()
    srt_files = scan(".srt")
    if not srt_files:
        print("✗ No .srt files found in current folder.")
        return
    print("Original .srt file:")
    idx = pick("Which file?", [f.name for f in srt_files])
    srt_path = srt_files[idx]
    blocks = parse_srt(srt_path)

    txt_files = scan(".txt")
    if not txt_files:
        print("✗ No .txt files found in current folder.")
        return

    print("\nTranslated .txt file(s):")
    choices = [f.name for f in txt_files] + ["All chunks (auto-combine *_chunk*.txt)"]
    idx = pick("Which file?", choices)

    if idx == len(txt_files):
        # auto-combine chunks
        stem = srt_path.stem
        chunk_files = sorted(Path(".").glob(f"{stem}_chunk*.txt"))
        if not chunk_files:
            print(f"✗ No chunk files matching '{stem}_chunk*.txt' found.")
            return
        print(f"\n  Combining {len(chunk_files)} chunk file(s):")
        for cf in chunk_files:
            print(f"    {cf.name}")
        translated_lines = []
        for cf in chunk_files:
            translated_lines += [l for l in cf.read_text(encoding="utf-8").splitlines() if l.strip()]
    else:
        txt_path = txt_files[idx]
        translated_lines = [l for l in txt_path.read_text(encoding="utf-8").splitlines() if l.strip()]

    if len(blocks) != len(translated_lines):
        print(f"\n⚠  Warning: {len(blocks)} SRT block(s) but {len(translated_lines)} translated line(s).")

    out_name = ask(f"\nOutput filename", f"{srt_path.stem}_translated.srt")
    if not out_name.endswith(".srt"):
        out_name += ".srt"
    out_path = Path(out_name)

    with out_path.open("w", encoding="utf-8") as f:
        for i, block in enumerate(blocks):
            content = translated_lines[i].split(BLOCK_SEP) if i < len(translated_lines) else block["lines"]
            f.write(block["index"] + "\n")
            f.write(block["timestamp"] + "\n")
            f.write("\n".join(l.strip() for l in content) + "\n\n")

    print(f"\n✓ Injected {min(len(blocks), len(translated_lines))} block(s) → {out_path}")


# ── entry point ────────────────────────────────────────────────────────────────

def main():
    print("═" * 40)
    print("  SRT Translation Tool")
    print("═" * 40)
    print()
    mode = pick("Mode", ["Export  (SRT → text for AI)", "Inject  (translated text → SRT)"])
    [do_export, do_inject][mode]()
    print()


if __name__ == "__main__":
    main()