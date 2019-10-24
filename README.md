# Handler of events
Handler of events is an app that notify user about changes in certain directory.

This application is for monitoring changes and events in a specific directory (for example, changing the file name, adding and / or deleting files, etc.)
To use the application you must:
1. Install Python 3.6.
2. Install pip package manager
<br/>```$ sudo apt install python-pip```
3. using pip, install other packages that are registered in the requirements file
<br/>```$ sudo pip install -r requirements.txt```
4. after installing the files from the requirements, you must subscribe to the channel "notifier" @ my_first111_bot
5. drive the following into the command line of the terminal
<br/>```$ python3 notify_me.py```<br/> As a result, starting notifications of opening the folder will come in the telegram channel.
6. In a separate terminal window, go to the folder and create a new text file.
<br/>```$ touch test_file.txt```<br/>We'll receive a notification in telegram about the creation of the file.
7. Rename this file with the following command
<br/>```$ mv test_file.txt test_file1.txt```<br/>We'll get a new file change notification.
8. Delete the file with the command
<br/>```$ rm test_file.txt```<br/>Notification of file deletion came in telegrams.
<br/><br/>Other handlers that you can use for the similar purposes are stored in directory "other_handlers".
