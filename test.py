from re import match

def extractDomainEmail(email):
    if match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',email):
        emailData = email.strip().split("@")
        domainName = email
    else:
        print(f"Email wrong format !")

import tldextract

address = 'yahoo.com.au'
domain = tldextract.extract(address)
domainName = domain.domain
domainExtension = domain.suffix

print(domainExtension)
from tool_module