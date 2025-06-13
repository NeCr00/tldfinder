import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description='Generate domain variations based on a TLD list.'
    )
    parser.add_argument(
        '-d', '--domain',
        required=True,
        help='Base domain or subdomain (e.g. target.com or sub.target.com)'
    )
    parser.add_argument(
        '-w', '--wordlist',
        required=True,
        help='Path to TLD wordlist file'
    )
    args = parser.parse_args()


    # Normalize and split domain
    domain = args.domain.rstrip('.')
    parts = domain.split('.')
    if len(parts) >= 2:
        base = '.'.join(parts[:-1])
    else:
        base = parts[0]

    # Read TLDs from wordlist and generate variants
    try:
        with open(args.wordlist, 'r') as f:
            for line in f:
                tld = line.strip().lstrip('.')
                if not tld or tld.startswith('#'):
                    continue
                print(f"{base}.{tld}")
    except Exception as e:
        print(f"Error reading wordlist: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
