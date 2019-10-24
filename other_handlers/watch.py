import logging
import inotify.adapters
#_DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
_DEFAULT_LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
_LOGGER = logging.getLogger(__name__)

def _configure_logging():
    _LOGGER.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter(_DEFAULT_LOG_FORMAT)
    ch.setFormatter(formatter)
    _LOGGER.addHandler(ch)

def _main():
    i = inotify.adapters.Inotify()
    i.add_watch('/home/lyk2/app/files')
    try:
        for event in i.event_gen():
            if event is not None:
                (header, type_names, watch_path, filename) = event
                _LOGGER.info("MASK->NAMES=%s WATCH-PATH=[%s] FILENAME=[%s]",
                             type_names, watch_path, filename)
    finally:
        i.remove_watch('/home/lyk2/app/files')

if __name__ == '__main__':
    _configure_logging()
    _main()