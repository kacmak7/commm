import ipfshttpclient
import logging

logger = logging.getLogger(__name__)

class Client:
    def __init__(self, hash=None):
        self._open() # initialize ipfs client
        
        if hash is None:
            self.hash = self.create_room()
            logger.warning('Created new room: ' + self.hash)
        else:
            self.hash = hash


    def __del__(self):
        logger.warning('closing')
        self._close() # shut down ipfs client

    def _open(self):
        self.ipfs_client = ipfshttpclient.connect(session=True) 

    def _close(self):
        self.ipfs_client.close()

    def get_id(self):
        return self.ipfs_client.id()['ID']

    '''
    creates communication room
    '''
    def create_room(self): #TODO needs working add_json/get_json ipfs methods
        return self.ipfs_client.add('test_commm_config.json')['Hash']
        #return hash
        



    

cl_0 = Client('aa')
cl_1 = Client()

#TODO timeout variable so something like a config 
#TODO checking if ledger file exists so if youre still connected

