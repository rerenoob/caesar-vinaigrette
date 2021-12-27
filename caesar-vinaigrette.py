import click

@click.command()
@click.option('--option', type=click.Choice(['E', 'D']), default='E', prompt='Enter option to encrypt or decrypt', help='Encrypt or decrypt')
@click.option('--string', prompt='Enter string to process (space delimited)', help='String to process.')
@click.option('--rotation', default=20, type=click.INT, prompt='Enter number of rotation', help='Number of rotation.')
@click.option('--key', prompt='Enter encryption key', help='Encryption key.')
def driver(option, string, rotation, key):
    if option == 'E':
        encrypt(string, rotation, key)
    else:
        decrypt(string, rotation, key)

def decrypt(encrypted, rotation, key):
    """Decrypt the encrypted string using the number rotation"""
    result = ""
    spaces = []
    for i in range(len(encrypted)):
        char = encrypted[i]
        """Support space deliminated list of words"""
        if char == " ":
            spaces.append(i - len(spaces))
        else:
            result += chr((ord(char) - rotation - 97) % 26 + 97)

    click.echo(decryptV(result, key, spaces))

def decryptV(ciphertext, key, spaces):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        if i in spaces:
            plaintext += " "
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 97)
    return plaintext

def encrypt(string_to_encrypt, rotation, key):
    """Encrypt the string using the number rotation"""
    result = ""
    spaces = []
    for i in range(len(string_to_encrypt)):
        char = string_to_encrypt[i]
        """Support space deliminated list of words"""
        if char == " ":
            spaces.append(i - len(spaces))
        else:
            result += chr((ord(char) + rotation - 97) % 26 + 97)

    click.echo(decryptV(result, key, spaces))

def encryptV(string, key, spaces):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    string_int = [ord(i) for i in string]
    plaintext = ''
    for i in range(len(string_int)):
        if i in spaces:
            plaintext += " "
        value = (string_int[i] + key_as_int[i % key_length]) % 26
        plaintext += chr(value + 97)
    return plaintext

if __name__ == '__main__':
    driver()
