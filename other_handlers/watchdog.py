from __future__ import print_function
import os
import sys
import time
import shutil
from watchdog.observers.polling import PollingObserverVFS
from watchdog.events import PatternMatchingEventHandler

class MyHandler(PatternMatchingEventHandler):
    #patterns = ["*.*", ".*"]

    def __init__(self, target_dir, **kwargs):
        PatternMatchingEventHandler.__init__(self, **kwargs)
        self._target_dir = target_dir

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        if not event.is_directory:
            # the file will be processed there
            print('{} {} --> {}'.format(event.src_path,
                                        event.event_type,
                                        self._target_dir))
            shutil.copy(event.src_path, self._target_dir)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

    def on_deleted(self, event):
        self.process(event)

    def on_moved(self, event):
        self.process(event)


if __name__ == '__main__':
    args = sys.argv[1:]
    source_dir = args[0]
    target_dir = args[1]

    observer = PollingObserverVFS(stat=os.stat, listdir=os.listdir, polling_interval=30)
    observer.schedule(MyHandler(target_dir, patterns=['*.*','*','.*']),
                      path=source_dir)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()