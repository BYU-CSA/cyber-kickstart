import base64

my_string = "CTF is life!!"
print(my_string)

byte_encoded_string = my_string.encode("utf-8")
print(byte_encoded_string)

base64_encoded_string_bytes = base64.b64encode(byte_encoded_string)
print(base64_encoded_string_bytes)

base64_encoded_string = base64_encoded_string_bytes.decode("utf-8")
print(base64_encoded_string)

print("\nThis can all be combined into one line:")
print(base64.b64encode(my_string.encode("utf-8")).decode("utf-8"))