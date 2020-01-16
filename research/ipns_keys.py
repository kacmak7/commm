import ipfshttpclient

# contributing to one document by multiple nodes

with ipfshttpclient.connect() as client:
    hash = client.add('conv.txt')['Hash']
    client.key.rm('example_key')
    key = client.key.gen('example_key', 'rsa')['Id']
    print(client.key.list())
    published = client.name.publish('/ipfs/' + hash, key=key)

    # find
    client.name.resolve(key)
