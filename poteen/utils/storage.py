from ..contextHolder import ContextHolder

logger = ContextHolder.get_logger()


class Storage(object):
    _map = {}
    _current = {}

    @classmethod
    def put(cls, key, value):
        logger.debug("Add object key: {key}; object: {obj}".format(
            key=key,
            obj=value
        ))
        cls._map[key] = value
        cls._current[value.NAME] = key

    @classmethod
    def get(cls, key):
        logger.debug("Get object by key. Key [{}]".format(key))
        if key in cls._map:
            logger.debug("Object: {}".format(cls._map[key]))
            return cls._map[key]
        return None

    @classmethod
    def get_current(cls, name):
        logger.debug("Get object by current key. Name [{}]".format(name))
        if name in cls._current:
            logger.debug("Object: {}".format(cls._map[cls._current[name]]))
            return cls._map[cls._current[name]]
        return None

    @classmethod
    def clear(cls):
        cls._map = {}
        cls._current = {}
