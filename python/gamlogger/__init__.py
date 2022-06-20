__version_info__ = (0, 9, 0)
__version__ = '.'.join(map(str, __version_info__))

__all__ = ['read_level_from_args', 'get_default_logger']

import logging

read_level_from_args, get_default_logger = logging.read_level_from_args, logging.get_default_logger

del logging
