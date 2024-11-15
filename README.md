# Med file parser <!-- omit in toc -->

# Title <!-- omit in toc -->
- [Dependencies](#dependencies)
- [Install for linux](#install-for-linux)
- [Usage](#usage)


# Dependencies

- python3 >= 3.8
- python3-venv


# Install for linux

```bash
    python3 -m venv venv
    . venv/bin/activate
    python3 -m pip install -U pip
    python3 -m pip install -U setuptools
    python3 -m pip install -e .
```


# Usage

Many files parsing example. From project root execute next commands in terminal:
```bash
    . venv/bin/activate
    parser multi-parsing -i "data/input" -o "data/output"
```

Single file parsing example. From project root execute next commands in terminal:
```bash
    . venv/bin/activate
    parser single-parsing -i "data/input/test.txt" -o "data/output/text.xlsx"
```