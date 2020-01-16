from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
import os

# Create target Directory if don't exist

tmp_path = '/tmp/sapt'

if not os.path.exists(tmp_path):
    os.mkdir(tmp_path)

SAPTCompleter = WordCompleter(['set', 'RHOSTS', 'insert'], ignore_case=True)

while 1:
	user_input = prompt('sapt > ', history=FileHistory(os.path.expanduser('/tmp/sapt/history.txt')), auto_suggest=AutoSuggestFromHistory(), completer=SAPTCompleter,)
	print(user_input)
