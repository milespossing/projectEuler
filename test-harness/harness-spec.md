# Test Harness

The basics are that we'd like a harness to run all problems from 1-n for a given
language. There should be a single shell command which can be run by the harness
and given an argument for the problem number:

```shell
$ python pje.py --problem 1
233168
$ cargo run pje --problem 1
4613732
```

Each command should be listed as a relative reference from this directory in the 
conf.json file.