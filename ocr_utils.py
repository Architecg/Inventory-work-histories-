"""
Utilities for normalizing OCR text and classifying pages
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from typing import Any, Dict, List
import argparse


from express import OCR_PATTERN as OCR_PATTERNS

def normalize_text(text: str) -> str:
    """Return a normalized, ASCII-only, lowercase string with collapsed spaces."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def classify_text(text: str) -> List[str]:
    """Return the list of keys whose patterns match the given text."""
    matches: List[str] = []
    for key, patterns in OCR_PATTERNS.items():
        if any(pattern.search(text) for pattern in patterns):
            matches.append(key)
    return matches


def process_pages(pages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Add normalized text and pattern matches to each page entry."""
    processed: List[Dict[str, Any]] = []
    for entry in pages:
        raw = entry.get("texto", "")
        norm = normalize_text(raw)
        updated = {
            **entry,
            "texto_raw": raw,
            "texto_norm": norm,
            "coincidencias": classify_text(norm),
        }
        processed.append(updated)
    return processed


def process_json(input_path: str, output_path: str) -> None:
    """Read pages from input JSON and write enriched data to output JSON."""
    data = json.loads(Path(input_path).read_text(encoding="utf-8"))
    pages = data["pages"] if isinstance(data, dict) and "pages" in data else data
    result = process_pages(pages)
    Path(output_path).write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Normalize and classify OCR pages")  
    parser.add_argument("input", help="Path to input JSON File")
    parser.add_argument("output", help="Path to write enriched JSON")
    args = parser.parse_args()
    process_json(args.input, args.output)


