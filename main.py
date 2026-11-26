LINE = "\U0001F9F5"

# The entry must be exactly one emoji: UTF-8 text of 1-16 characters.
assert 1 <= len(LINE) <= 16, f"line is {len(LINE)} chars"
assert "\n" not in LINE
# The brief says the glyph alone, nothing else: pin exactly one code point
# (first run showed 1 code point / 4 bytes; a second glyph must fail here).
assert len(LINE) == 1, f"expected exactly one emoji, got {len(LINE)} chars"
assert LINE == LINE.strip(), "line has leading/trailing whitespace"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
