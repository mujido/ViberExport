#!/usr/bin/env python3

# Copyright 2019 Kurt Stutsman
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import csv
import sqlite3
import sys
import time
from datetime import datetime

DIRECTION_OUT = 0
DIRECTION_IN = 1

dialect = csv.excel_tab()

def dumpChatID(db, chat_id, writer):
	results = db.execute('''SELECT e.Timestamp, Direction, Name, Number, Body 
							FROM Events e
							INNER JOIN Messages m ON m.EventID = e.EventID
							INNER JOIN Contact c ON c.ContactID = e.ContactID
							WHERE e.ChatID = ?
							ORDER BY SortOrder''', [chat_id])
	for row in results:
		(timestamp, direction, name, number, body) = row
		timestamp /= 1000
		dt = datetime.fromtimestamp(timestamp)
		msgdate = dt.strftime("%m/%d/%Y")
		msgtime = dt.strftime("%H:%M:%S")
		if direction == DIRECTION_IN:
			name_from = "Me"
		else:
			name_from = name
		writer.writerow((msgdate, msgtime, name_from, number, body))

def dumpDB(db):
	results = db.execute('''SELECT ChatID FROM ChatInfo''')
	for (chat_id,) in results:
		with open(f"chat_{chat_id}.csv", "w") as out:
			writer = csv.writer(out, dialect=dialect)
			dumpChatID(db, chat_id, writer)

def dumpMessages(dbFile):
	with sqlite3.connect(dbFile) as db:
		dumpDB(db)

def main(argv):
	dumpMessages(argv[1])

if __name__ == '__main__':
	main(sys.argv)