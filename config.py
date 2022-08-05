PORT = 443

# name -> secret (32 hex chars)
USERS = {
    "tg":  "20000002000022200000000200002200"
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True,
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "www.Yadesh.ir"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "8aaddd60c4328bc57a7d0b52c57e4906"

