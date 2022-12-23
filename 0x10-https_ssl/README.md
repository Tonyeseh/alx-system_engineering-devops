# 0x10. HTTPS SSL

## Tasks :page_with_curl:

* [0. World wide web](./0-world_wide_web): Bash script that displays information about subdomains. Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
* [1. HAproxy SSL termination](./1-haproxy_ssl_termination): HAproxy config format that:
	* accepts encrypted traffic for subdomain www
	* listens on port TCP 443
	* accepts SSL traffic
	* serves encrypted trafic that will return the `/` of a web server
* [2. No loophole in your website traffic ](./100-redirect_http_to_https): HAproxy automatically redirect HTTP traffic to HTTPS. Requirements=>
	* transparent to the user
	* return HTTP code 301
