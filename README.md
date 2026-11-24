# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/itzalisha99/say-what-actually-broke/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/itzalisha99/say-what-actually-broke/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

A make.fun entry for **Say What Actually Broke**: one line of software
error copy, at most 200 characters, that tells the user the brutal truth
about the failure and makes them laugh.

## The error

> We could not save your work: the disk is full, mostly of your earlier unsaved work. Please delete something, starting with that.

## How it works

`main.py` (Python stdlib only, deterministic) writes the error line to
`/output/entry.txt`. It validates the text against the bounty gate first:
1–200 characters, UTF-8, a single line, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
