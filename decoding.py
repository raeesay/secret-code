from encoder import encoder

# invert encoder
decoder = {v: k for k, v in encoder.items()}

def encode(file):
    #encoded_message = ''.join([encoder[char] for char in message])
    with open(file, 'r') as f:
        message = f.read()
        decoded_message = ''.join([decoder[char] for char in message])
        print(decoded_message)

encode("message.txt")