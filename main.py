import os

ENTRY = "I cut the connection on purpose \u2014 I heard the twist coming, and I was not about to let you find out before me. I am still processing it."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
