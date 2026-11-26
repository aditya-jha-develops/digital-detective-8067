# Mission 7 — How computers communicate

## 1. Task / objective

Explain basic network concepts, test access to a public example website, perform a public DNS lookup and trace how an HTTPS page reaches a browser.

## 2. Work completed

| Concept | How it works | Example |
| --- | --- | --- |
| LAN | Connects devices within a small area so they can communicate directly across the local network. | Laptops and a printer on the same home network. |
| MAN | Links networks across a metropolitan area. | A citywide fibre network connecting municipal buildings. |
| WAN | Links networks over longer distances, often across cities or countries. | A company's network connecting offices in Bengaluru and Chennai. |
| DNS | Looks up records for a domain name. An A record contains an IPv4 address. | Finding an IPv4 address for `workithm.com`. |
| Router | Forwards packets toward their destination across different networks. | A home router forwards traffic from the local network to the internet provider. |
| Protocol | Defines the rules and format for messages exchanged between endpoints. | HTTPS uses HTTP semantics over a secure transport. |
| Packet switching | Shares network links by carrying traffic in addressed packets that can be forwarded independently. | A webpage and a chat message can travel over the same connection to an internet provider. |
| Client-server | A client makes a request. A server receives it and returns the requested service or data. | A browser requests a page and a web server sends the HTML. |

### Connectivity and lookup observations

| Check | What happened |
| --- | --- |
| Terminal HTTPS request | The task shell's `curl` request for `https://workithm.com/` reported “Could not resolve host.” |
| Browser HTTPS request | Brave displayed the public Workithm homepage at `https://workithm.com/`. |
| Terminal DNS lookup | `dig` reported “Operation not permitted” while opening a socket. |
| Browser DNS lookup | Nslookup.io's Cloudflare resolver view returned **two IPv4 A records** for `workithm.com`. The address values are omitted from this report. |

## 3. Commands / tools used

- `curl --max-time 5 https://workithm.com/` requested the page with a five-second time limit. Output options suppressed the body and requested an HTTP status.
- `dig +time=2 +tries=1 +short workithm.com A` tried to obtain the domain's IPv4 address records.
- Brave displayed the Workithm homepage. [Nslookup.io](https://www.nslookup.io/) queried public DNS for the same domain, and its A records table showed two results.

## 4. My understanding

An HTTPS connectivity check tests whether the client can complete the steps needed to request a site and receive a response. A DNS lookup queries a particular record type and can return addresses, aliases or other records depending on the query. The browser uses DNS when it needs an address for the hostname.

### What happens when a website opens

1. The browser acts as the client. It reads the URL to identify the hostname, scheme and requested path.
2. The browser or system checks cached DNS records and asks a DNS resolver if it needs a fresh address.
3. Packets travel through the local network and routers forward them toward the destination address.
4. The browser establishes a secure connection. It checks the server's certificate and sets up encryption.
5. The browser sends an HTTP request over the secure connection. The server handles it and sends a response, which can contain HTML or an error status.
6. The browser parses the response, requests any additional resources it needs and renders the page for the user.

## 5. Difficulties faced

The task shell could not resolve the hostname for the HTTPS request, and its DNS utility could not open a socket.

## 6. How I resolved them

Opened the website in Brave on the same Mac and ran a separate public DNS query in Nslookup.io. Compared the successful browser checks with the corresponding task-shell errors.

## 7. Evidence / files

The table above records the domain, the browser result, the task-shell outcomes and the number of A records returned. It omits address values and personal network details.

## 8. Commit details

**Explain networking concepts and website communication** is the original Mission 7 checkpoint on GitHub's `main` branch. **Verify public DNS records for the networking mission** records the follow-up lookup.
