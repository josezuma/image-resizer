#!/usr/bin/env python3
"""CLI: image-resizer

Basic image resizer CLI. Resize, convert format, and compress images from command line.
"""
import sys, json, argparse

def main():
    parser = argparse.ArgumentParser(description="Basic image resizer CLI. Resize, convert format, and compress images from command line.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = {"tool": "image-resizer", "ready": True}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result}")

if __name__ == "__main__":
    main()
