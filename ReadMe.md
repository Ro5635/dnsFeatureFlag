# DNS Feature Flags

Low latency run time feature flags are a basic rquirement for many projects, for personal projects the costs of "real" feature flag SAAS solutions or the cost of a basic cached API are irksome.

Until aws evidently rolls out into eu-west-2 London this will do for basic run time feature flagging in personal projects.

This python module queries the value of a txt DNS record to deduce the state of a given flag. Route53 DNS queries are cheap as chips and the latency fits the needs of a feature flag. Just create the flags in your DNS provider of choice and query them with this tiny funcition.
