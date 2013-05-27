class Storage(object):
    _map = {}
    _current = {}

    @classmethod
    def put(cls, key, value):
        cls._map[key] = value
        cls._current[value.NAME] = key

    @classmethod
    def get(cls, key):
        if key in cls._map:
            return cls._map[key]
        return None

    @classmethod
    def get_current(cls, name):
        if name in cls._current:
            return cls._map[cls._current[name]]
        return None

    @classmethod
    def clear(cls):
        cls._map = {}
        cls._current = {}