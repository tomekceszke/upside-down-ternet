# upside-down-ternet
Rewriter for Squid written in Python that flips every jpg on page.


## Run
* Install and configure Squid proxy
* Point 'url_rewrite_program' property in Squid config to [rewrite.py](rewrite.py)
* Redirect all traffic to Squid - you can use [startUpSideDown.sh](startUpSideDown.sh) script


## References
* Idea: [Upside-Down-Ternet](http://www.ex-parrot.com/pete/upside-down-ternet.html)
* Script: https://edmondburnett.com/post/squid-custom-url-rewriting

## Technology stack
* squid
* python
* bash
* ImageMagic
* iptables


