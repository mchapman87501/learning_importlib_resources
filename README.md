# Learning to Use importlib.resources

At PyCon 2018, Barry Warsaw gave a talk about `importlib.resources`.  This repo demos capabilities mentioned in passing during the talk.

# Why

I usually get by with a simple

```python
from pathlib import pathlib

_here = Path(__file__).parent.resolve()


def get_some_data() -> str:
    return (_here / 'data' / 'hello.txt').read_text()
```

But, as Barry noted, `importlib.resources` can do a lot more, e.g., importing from zipped resource packages.


# Shiv

Barry's talk also mentioned [shiv](https://shiv.readthedocs.io/en/latest/).  I'd never heard of it.  `shivit.sh` shows how to use it to turn testit.py into a self-contained, standalone executable.
