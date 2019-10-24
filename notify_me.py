import os
import pyinotify
import asyncore
import bot

class EventProcessor(pyinotify.ProcessEvent):
    _methods = ["IN_CREATE",
                "IN_OPEN",
                "IN_ACCESS",
                "IN_ATTRIB",
                "IN_CLOSE_NOWRITE",
                "IN_CLOSE_WRITE",
                "IN_DELETE",
                "IN_DELETE_SELF",
                "IN_IGNORED",
                "IN_MODIFY",
                "IN_MOVE_SELF",
                "IN_MOVED_FROM",
                "IN_MOVED_TO",
                "IN_Q_OVERFLOW",
                "IN_UNMOUNT",
                "IN_DELETE",
                "default"]

def process_generator(cls, method):
    def _method_name(self, event):
        bot.telegram_bot_sendtext("Path name: "+ event.pathname + ".\n Event Name: " + event.maskname +".")
        print("Method name: process_{}()\n"
              "Path name: {}\n"
              "Event Name: {}\n".format(method, event.pathname, event.maskname))
    _method_name.__name__ = "process_{}".format(method)
    setattr(cls, _method_name.__name__, _method_name)

for method in EventProcessor._methods:
    process_generator(EventProcessor, method)


watch_manager = pyinotify.WatchManager()
event_notifier = pyinotify.AsyncNotifier(watch_manager, EventProcessor())

watch_this = os.path.abspath("files")
watch_manager.add_watch(watch_this, pyinotify.ALL_EVENTS)
asyncore.loop()

