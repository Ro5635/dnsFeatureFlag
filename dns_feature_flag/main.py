import dns.resolver
import os

DNS_FEATURE_FLAG_BASE_DOMAIN = os.environ['DNS_FEATURE_FLAG_BASE_DOMAIN']


def is_flag_enabled(name, feature_flag_base_domain=DNS_FEATURE_FLAG_BASE_DOMAIN):
    # ToDo: handle flag not found 
    flag_uri = f"{name}.{feature_flag_base_domain}"
    read_txt_records = dns.resolver.resolve(flag_uri, 'txt')

    # Ignoring possibility of multiple values 😛
    # Assume that "1" means True else False
    return read_txt_records[0].to_text() == '"1"'
