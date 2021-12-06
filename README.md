# get-browser-cookies

Uses the [`browser_cookie3`](https://github.com/borisbabic/browser_cookie3) package to download cookies from your browser (Chrome or Firefox).

## Quickstart

```
pipx install get-browser-cookies
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

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```
