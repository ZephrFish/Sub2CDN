# Subdomain Enumeration and CDN Check Tool
This tool performs subdomain enumeration, resolves IP addresses, and checks against known CDN IPs. It also checks each non-CDN IP on Shodan for open ports.

## Requirements
- Python 3
- [Subfinder](https://github.com/projectdiscovery/subfinder)
- [CDNCheck](https://github.com/projectdiscovery/CDNCheck)
- [Shodan Python library](https://github.com/shodan-io/shodan-python)
- A [Shodan API key](https://account.shodan.io/register)

## Usage
- Install the required libraries and tools.
- Replace YOUR_API_KEY in the script with your Shodan API key.
- Run the script: `python sub2cdn.py`
- Enter the initial domain when prompted.

The tool will perform subdomain enumeration using Subfinder, resolve the IP addresses, and check against known CDN IPs using CDNCheck. It will also check each non-CDN IP on Shodan for open ports.

The list of resolved hosts will be printed to the console and output to a file named resolved_hosts.txt.

##  Example Output
```
Enter an initial domain: example.com
api.example.com (1.2.3.4) is not a CDN
Open ports for 1.2.3.4:
  80/http
  443/https
app.example.com (5.6.7.8) is not a CDN
Open ports for 5.6.7.8:
  80/http
  443/https
cdn.example.com (9.10.11.12) is a CDN

Resolved hosts:
api.example.com (1.2.3.4)
app.example.com (5.6.7.8)
```
