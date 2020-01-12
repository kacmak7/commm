import ipfshttpclient

with ipfshttpclient.connect() as client:
    file_upload = client.add('conv.txt')
    print(file_upload)
    with open('conv_hash.txt', 'w+') as text_file:
        n = text_file.write(file_upload['Hash'])
    
    if client.get('QmXJLAxQvBUVc2EnqJrYEnt3QbTAtLXXrTXiCkodjrVZca')
