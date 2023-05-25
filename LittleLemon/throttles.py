from rest_framework.throttling import AnonRateThrottle


class TenCallsPerMinute(AnonRateThrottle):
    scope = 'ten'
