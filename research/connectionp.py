import ipfshttpclient
import io

with ipfshttpclient.connect() as client:
    
    # stream
    print(client.block.put(io.BytesIO(b'PROTO HELLOOO')))
    print()

    file_upload = client.add('conv.txt')
    print(file_upload)
    with open('conv_hash.txt', 'w+') as text_file:
        n = text_file.write(file_upload['Hash'])
    
    client.get('QmXJLAxQvBUVc2EnqJrYEnt3QbTAtLXXrTXiCkodjrVZca')
