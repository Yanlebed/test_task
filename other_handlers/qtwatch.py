import sys
from PyQt4 import QtCore

def directory_changed(path):
    print('Directory Changed: %s' % path)

def file_changed(path):
    print('File Changed: %s' % path)

app = QtCore.QCoreApplication(sys.argv)

paths = [
    '/home/lyk2/app/files',
    '/home/lyk2/app/files/picture.jpg',
    '/home/lyk2/app/files/in_doc.doc',
    '/home/lyk2/app/files/document.odt',
    ]

fs_watcher = QtCore.QFileSystemWatcher(paths)
fs_watcher.directoryChanged.connect(directory_changed)
fs_watcher.fileChanged.connect(file_changed)

sys.exit(app.exec_())
