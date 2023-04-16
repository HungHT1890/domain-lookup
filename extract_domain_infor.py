from tldextract import extract


def domain_exampl():
    domain_type_list = ['domain.com','yahoo.co.uk','domain.com.au','hung.name.com','hunght1890.github.io']
    for domain in domain_type_list:
        infor = extract(domain)
        with open('domain_type.txt','a',encoding='utf8') as f:
            f.write(str(infor) + '\n')
        print(infor)
        # type of domain name
        """
        1: sub domain => no check this domain 
        2: domain name => popul
        3: domain error format
        """


def domain_extract(domain_name):
    full_information = extract(domain_name.strip())
    subdomain = full_information[0]
    domain = full_information[1]
    suffix = full_information[2]
    full_information = {
        'domain_name': domain_name,
        'subdomain': subdomain,
        'domain': domain,
        'suffix': suffix,
    }
    return full_information
