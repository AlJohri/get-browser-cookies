import json
import argparse
import browser_cookie3

parser = argparse.ArgumentParser()
parser.add_argument("--domain", required=True)
parser.add_argument("--path", default="/")
parser.add_argument("--browser", choices=["chrome", "firefox"], required=True)

def main():
	args = parser.parse_args()
	cj = getattr(browser_cookie3, args.browser)()
    
	for cookie in cj:
		if cookie.domain == args.domain and cookie.path == args.path:
			print(json.dumps(cookie.__dict__))

if __name__ == "__main__":
	main()
