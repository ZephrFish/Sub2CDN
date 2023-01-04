import re
import socket
import requests
import subprocess
import shodan

def get_subdomains(domain):
    # Perform subdomain enumeration using Subfinder
    subdomains = []
    try:
        output = subprocess.run(["subfinder", "-d", domain, "-silent"], capture_output=True)
        subdomains = output.stdout.decode("utf-8").strip().split("\n")
    except:
        pass
    return subdomains

def resolve_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except:
        return None

def is_cdn(ip):
    # Check if the IP belongs to a known CDN using CDNCheck
    cdn = False
    try:
        output = subprocess.run(["cdncheck", "-ip", ip], capture_output=True)
        if "CDN" in output.stdout.decode("utf-8"):
            cdn = True
    except:
        pass
    return cdn

def check_ip_on_shodan(ip):
    # Replace YOUR_API_KEY with your Shodan API key
    api = shodan.Shodan("YOUR_API_KEY")

    try:
        # Search Shodan for the given IP
        results = api.host(ip)

        # Print the list of open ports
        print(f"Open ports for {ip}:")
        for item in results['data']:
            print(f"  {item['port']}/{item['transport']}")
    except shodan.APIError as e:
        print(f"Error: {e}")

# Prompt for initial domain
initial_domain = input("Enter an initial domain: ")

# Get subdomains and resolve IPs
subdomains = get_subdomains(initial_domain)
non_cdn_ips = []
resolved_hosts = []
for subdomain in subdomains:
    ip = resolve_ip(subdomain)
    if ip:
        if is_cdn(ip):
            print(f"{subdomain} ({ip}) is a CDN")
        else:
            print(f"{subdomain} ({ip}) is not a CDN")
            non_cdn_ips.append(ip)
            resolved_hosts.append(f"{subdomain} ({ip})")
            check_ip_on_shodan(ip)
    else:
        print(f"Unable to resolve IP for {subdomain}")

# Print resolved hosts
print("\nResolved hosts:")
for host in resolved_hosts:
    print(host)

# Output resolved hosts to a file
with open("resolved_hosts.txt", "w") as f:
    for host in resolved_hosts:
        f.write(f"{host}\n")
