from client import *

cl_0 = Client()
cl_0.send_mess('new message')
cl_0.send_mess('second message')

ledger_hash = cl_0.resolve_ledger_hash()
cl_0.get(ledger_hash)
with open(ledger_hash) as ledger:
    for line in ledger: 
        print(line)
        cl_0.get(line)
        with open(line) as mess:
            print(mess)

