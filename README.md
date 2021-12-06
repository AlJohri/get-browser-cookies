# get-browser-cookies

Uses the [`browser_cookie3`](https://github.com/borisbabic/browser_cookie3) package to download cookies from your browser (Chrome or Firefox).

## Quickstart

```
# Install via pip
pip install get-browser-cookies

# Or install via pipx
pipx install get-browser-cookies

# Run
get-browser-cookies --browser chrome --domain "mail.google.com"
```

## Usage

```
usage: get-browser-cookies [-h] --domain DOMAIN [--path PATH] --browser {chrome,firefox}

optional arguments:
  -h, --help            show this help message and exit
  --domain DOMAIN
  --path PATH
  --browser {chrome,firefox}
```

## Development

Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

Push

```
# Build package
python setup.py sdist bdist_wheel

# Upload to Test PyPI
twine upload -r testpypi dist/*

# Upload to Test PyPI
twine upload dist/*
```
