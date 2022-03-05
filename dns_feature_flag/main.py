import dns.resolver
import os


def _get_default_base_domain():
    try:
        return os.environ['DNS_FEATURE_FLAG_BASE_DOMAIN']
    except KeyError:
        return None


DNS_FEATURE_FLAG_BASE_DOMAIN = _get_default_base_domain()


def is_flag_enabled(name, feature_flag_base_domain=DNS_FEATURE_FLAG_BASE_DOMAIN):
    try:
        flag_uri = f"{name}.{feature_flag_base_domain}"
        read_txt_records = dns.resolver.resolve(flag_uri, 'txt')

        # Ignoring possibility of multiple values 😛
        # Assume that "1" means True else False
        return read_txt_records[0].to_text() == '"1"'
    except dns.resolver.NXDOMAIN:
        print('Feature Flag Not Found, defaulting to False')
        return False
