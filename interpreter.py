def encode(data):
    encode_data = ''
    for char in data:
        encode_data += str((int(char) + 3) % 10)
    return encode_data

def decode(password):
    decode_data = ''
    for char in str(password):
        decode_data += str((int(char) - 3) % 10)
    return decode_data


if __name__ == '__main__':
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        user_option = input('Please enter an option: ')
        if user_option == '1':
            original_password = input('Please enter your password to encode: ')
            password_encode = encode(original_password)
            print('Your password has been encoded and stored!\n')
        if user_option == '2':
            password_decode = decode(password_encode)
            print(f'The encoded password is {password_encode}, and the original password is {password_decode}.')
        if user_option == '3':
            break