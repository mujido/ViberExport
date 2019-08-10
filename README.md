# ViberExport

A simple tool to dump messages from the PC Viber client. These messages are stored in an SQLite database located in your user `AppData\Roaming` directory.

## Prerequisites
- Requires Python3.6+

## Usage

```
python3 ViberExport.py <path-to-viber.db>
````
Running this command will go through each chat and dump the messages to a file named `chat_<number>.csv`. The number is an internal DB identifier for each unique chat. The output closely replicates the old format that Viber would allow users to export their chat messages through email.

Normally in Windows Viber appears to store this database at the location `%APPDATA%\ViberPC\<phone number>\viber.db`.
