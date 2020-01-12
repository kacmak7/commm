import ipfshttpclient

class Client:
    def __init__(self, hash):
        self.hash = hash
        self._open()

    def __del__(self):
        self._close()

    def _open(self):
        self.ipfs_client = ipfshttpclient.connect(session=True) 

    def _close(self):
        self.ipfs_client.close()

    def get_id(self):
        return self.ipfs_client.id()['ID']

    

cl = Client('aa')

#TODO timeout variable so something like a config 
