import ipfshttpclient
import json
import logging

logger = logging.getLogger(__name__)

class Client:
    def __init__(self, hash=None):
        self._open() # initialize ipfs client
        
        if hash is None:
            self.hash = self.create_room()
            logger.warning('Created ' + self.hash)
        else:
            try:
                self.join_room(hash)
                self.hash = hash
                logger.warning('Joined ' + self.hash)
            except:
                logger.error('Could not join ' + hash)

    def __del__(self):
        logger.warning('closing')
        self._close() # shut down ipfs client

    def _open(self):
        self.ipfs_client = ipfshttpclient.connect(session=True) 

    def _close(self):
        self.ipfs_client.close()
    
    def _clean(self, hash):
        self.ipfs_client.pin.rm(hash)
        self.ipfs_client.repo.gc()

    def get_id(self):
        return self.ipfs_client.id()['ID']

    def get_hash(self):
        return self.hash

    def send_mess(self, msg):
        # TODO update ledger here
        with open('')
        return self.ipfs_client.add(msg)

    '''
    creates communication room
    '''
    def create_room(self): #TODO needs working add_json/get_json ipfs methods
        first_mess = self.send_mess('test.txt')
        json.dumps({'version': '0.1', 'messes': (first_mess, )})
        return self.ipfs_client.add('test_commm_config.json')['Hash']

    '''
    joins the room
    '''
    def join_room(self, hash):
        self.ipfs_client.get(hash)
        



room = 'QmV4h5WfvLssEyY8wqWhm5wjg7iZfn68hUuk4cZCpWiD1P'
cl_0 = Client('badbadfeioa')
cl_1 = Client()

#TODO timeout variable so something like a config 
#TODO checking if ledger file exists so if youre still connected
#TODO how to update the roomconfigfiles - IPNS
#TODO monitoring of members, CRITICAL log if message from outside, add tests
#TODO client.object_put()

