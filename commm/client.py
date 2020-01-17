import ipfshttpclient
import json
import logging

logger = logging.getLogger(__name__)


class Client:
    def __init__(self, key=None):
        self._open()  # initialize ipfs client

        if key is None:
            self.create_room()
            logger.warning("Created " + self.key)
        else:
            try:
                self.key = key
                logger.warning("Joined " + self.key)
            except:
                logger.error("Could not join " + key)

    def __del__(self):
        logger.warning("closing")
        self._close()  # shut down ipfs client

    def _open(self):
        self.ipfs_client = ipfshttpclient.connect(session=True)

    def _close(self):
        self.ipfs_client.close()

    def _clean(self, key):
        self.ipfs_client.pin.rm(key)
        self.ipfs_client.repo.gc()

    def get_ledger(self):
        path = client.name.resolve(self.key)["Path"]  # it downloads the file
        return path[6:]

    def update_room_key(self):  # means: reset the room / kick everyone
        ledger_hash = get_ledger()
        self.ipfs_client.key.rm("room_key")
        self.key = client.key.gen("room_key", "rsa")["Id"]
        self.ipfs_client.name.publish("/ipfs/" + ledger_hash, key=self.key)

    def get_id(self):
        return self.ipfs_client.id()["ID"]

    def get_room_key(self):
        return self.key

    """
    populates the message
    """

    def send_mess(self, msg):
        mess_hash = self.ipfs_client.add(msg)["Hash"]
        ledger_hash = get_ledger()
        with open(ledger_hash) as ledger:
            ledger.writelines(mess_hash)
        self.ipfs_client.name.publish(
            "/ipfs/" + ledger_hash, key=self.key
        )  # IPNS update
        return mess_hash

    """
    creates communication room
    """

    def create_room(self):
        first_mess = self.ipfs_client.add_str(
            json.dumps({"sender": "system", "body": "Hello, it's your new room"})
        )
        ledger_hash = self.ipfs_client.add_str(
            json.dumps({"version": "0.1", "messes": (first_mess,)})
        )  # TODO
        try:
            self.ipfs_client.key.rm("room_key")
        except:
            logger.info("CREATING ROOM FOR THE FIRST TIME")
        self.key = self.ipfs_client.key.gen("room_key", "rsa")["Id"]
        self.ipfs_client.name.publish("/ipfs/" + ledger_hash, key=self.key)

    """
    joins the room
    """
    # def join_room(self, key):
    #    self.ipfs_client.get(key)


room = "QmV4h5WfvLssEyY8wqWhm5wjg7iZfn68hUuk4cZCpWiD1P"
cl_0 = Client("badbadfeioa")
cl_1 = Client()

# TODO timeout variable so something like a config
# TODO checking if ledger file exists so if youre still connected
# TODO monitoring of members, CRITICAL log if message from outside, add tests
# TODO client.object_put()
# TODO IPNS discussion - https://discuss.ipfs.io/t/mutability-using-ipns-but-multiple-contributors/555/8
