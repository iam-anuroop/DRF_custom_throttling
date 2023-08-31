from rest_framework.throttling import UserRateThrottle


class custom_throttle(UserRateThrottle):
    scope='custom'