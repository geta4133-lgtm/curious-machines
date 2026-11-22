import os

TEXT = (
    "An octopus can rewrite its own genome. Its RNA edits tens of thousands "
    "of letters on the fly — same genes, constantly reworded — so its brain "
    "retools itself with the temperature. Biologists call it pervasive. "
    "Nobody can explain why we kept the typo-free draft and they didn't."
)

d = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(d, exist_ok=True)
with open(os.path.join(d, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)

print(f"wrote {len(TEXT.encode('utf-8'))} chars")
