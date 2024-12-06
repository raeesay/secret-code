from encoder import encoder

message1 = "THIS IS SO COOL"

def encode(message):
    encoded_message = ''.join([encoder[char] for char in message])
    f = open("message.txt", "a")
    f.write(encoded_message)
    f.close()
    print(f"Message encoded and save to message.txt")

encode(message1)
