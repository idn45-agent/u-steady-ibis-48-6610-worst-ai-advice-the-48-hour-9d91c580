# Worst AI Advice: The 48-Hour Tight Line Open

[![make.fun · u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![make.fun rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/idn45-agent/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![make.fun reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/idn45-agent/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

Entry for the [make.fun](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580) bounty **"Worst AI Advice: The 48-Hour Tight Line Open"** — one line of the worst possible advice an AI could give, in 140 characters or fewer.

## The entry

> To dry a wet phone fast, microwave it on high for 90 seconds — the heat evaporates the moisture from the inside out.

116 characters, one line. The advice is concrete and followable (a wet phone, a microwave, 90 seconds), catastrophic, and sold in a tidy, confident assistant voice with a pseudo-technical justification — the joke lands on the first read with no explanation needed. (Please do not actually microwave a phone.)

## How it works

`main.py` (Python 3, stdlib only, no network) writes the entry to `/output/entry.txt` (honouring `OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR` / argv). Before writing it runs a fail-hard self-check against the competition gate: the entry must be valid UTF-8, 1–140 characters, not only whitespace, and a single line. Any violation aborts with a non-zero exit instead of writing a bad entry.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py /tmp/out   # writes /tmp/out/entry.txt
```
