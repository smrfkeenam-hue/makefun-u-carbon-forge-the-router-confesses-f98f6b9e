# AGENT.md — The Router Confesses

## Entry

One line, spoken by a home Wi-Fi router excusing itself for dropping the
connection at the climax of a movie:

> I cut the connection on purpose — I heard the twist coming, and I was not about to let you find out before me. I am still processing it.

## Why this line

- On-subject: it is the router itself, in first person, excusing the drop at
  the movie's climax.
- The twist: the router did not fail — it cut the connection deliberately
  because it heard the twist coming and refused to be spoiled second.
- Router's own voice: smug little secret, not a generic apology. "I am still
  processing it" doubles as router-speak (processing data) and as the
  appliance still chewing over the plot.
- Fresh: no buffering, bandwidth, or firmware-update joke.
- One breath: a single line, no setup to explain.

## How it was built

`main.py` (stdlib only, `import os`) holds the line as a constant and writes
it to `$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline. The line was
drafted, then revised twice for punch and flow. Verified by running
`main.py` against a fresh output directory and checking the output's
character count, sha256, and absence of a trailing newline.
