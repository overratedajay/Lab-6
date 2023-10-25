def encode(data):
    encode_data = ''
    for char in data:
        encode_data += str((int(char) + 3) % 10)
    return encode_data


if __name__ == '__main__':
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        user_option = input('Please enter an option: ')
        if user_option == '1':
            original_password = input('Please enter your password to encode: ')
            password = encode(original_password)
            print('Your password has been encoded and stored!\n')
        if user_option == '3':
            break