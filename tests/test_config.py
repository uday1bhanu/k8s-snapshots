import os
import contextlib
import datetime



@contextlib.contextmanager
def set_env(**environ):
    """
    Temporarily set the process environment variables.

    >>> with set_env(PLUGINS_DIR=u'test/plugins'):
    ...   "PLUGINS_DIR" in os.environ
    True

    >>> "PLUGINS_DIR" in os.environ
    False

    :type environ: dict[str, unicode]
    :param environ: Environment variables to set
    """
    old_environ = dict(os.environ)
    os.environ.update(environ)
    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(old_environ)

