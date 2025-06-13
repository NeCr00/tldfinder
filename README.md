# tldfinder

**tldfinder** is a simple, fast CLI tool for generating domain variations based on a Top-Level Domain (TLD) wordlist. It’s perfect for pentesters, bug bounty hunters, and red‑teamers who need to enumerate potential domain names for reconnaissance.



## Key Features

*  **Flexible Inputs**: Accepts a base domain or subdomain (e.g., `example.com` or `api.example.com`).
*  **Wordlist‑Driven**: Reads any text file containing one TLD per line (e.g., `com`, `net`, `jp`, etc.).
*  **Clean Output**: Prints generated domains to **stdout**, keeping **stderr** for the ASCII logo and errors.
*  **Pipe‑Ready**: Designed to integrate seamlessly into your tooling pipeline (e.g., `dnsx`, `Eyewitness`, `httpx`).



## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourorg/tldfinder.git
   cd tldfinder
   ```

2. (Optional) Move into your `$PATH` for system‑wide usage:

   ```bash
   mv tldfinder.py /usr/local/bin/tldfinder
   ```

---

## Usage

Basic usage:

```bash
./tldfinder.py -d example.com -w w /usr/share/seclists/Discovery/DNS/tlds.txt
```

This prints each of the form:

```
example.com
example.net
example.org
... (etc)
```

To view help (with the ASCII logo):

```bash
./tldfinder.py --help
```

---

## Integration Examples

### 1. DNS Resolution with dnsx

Pipe **tldfinder** into **dnsx** to filter only alive domains:

```bash
tldfinder -d example.com -w tlds.txt \
    | dnsx -silent -resp -o live_domains.txt
```

* `-silent`: suppresses extra output
* `-resp`: shows only domains with valid DNS records
* `-o`: writes results to `live_domains.txt`

### 2. HTTP Probing & Screenshots with Eyewitness

Once you have `live_domains.txt`, you can feed them to **Eyewitness** to capture screenshots and HTML fingerprints:

```bash
cat live_domains.txt \
    | httpx -silent -status-code -o http_ok.txt

eyewitness \
    -f http_ok.txt \
    -d screenshots/ \
    --no-prompt
```

Or combine all steps in one go:

```bash
tldfinder -d example.com -w tlds.txt \
    | dnsx -silent -resp \
    | httpx -silent -status-code \
    | eyewitness -f - -d screenshots/ --no-prompt
```

### 3. Custom Pipelines

You can slot **tldfinder** into any pipeline. For example, scanning for subdomain takeovers:

```bash
tldfinder -d example.com -w tlds.txt \
    | dnsx -silent -resp -a -aaaa \
    | nuclei -t ~/nuclei-templates/subdomain-takeover.yaml
```


