A simple yet effective double encryption method to hide your precious texts. It
only support lower case text at the moment.

## Usage:
Install requirements:
   ```
   :~$ pip install requirement.txt
   ```

Encryption:
   ```
   :~$ python caesar-vinaigrette.py
   Enter option to encrypt or decrypt (E, D) [E]: E
   Enter string to process (space delimited): apple
   Enter number of rotation [13]: 20
   Enter encryption key: aaa
   ujjfy
   ```

Decryption:
   ```
   :~$ python caesar-vinaigrette.py
   Enter option to encrypt or decrypt (E, D) [E]: D
   Enter string to process (space delimited): ujjfy
   Enter number of rotation [13]: 20
   Enter encryption key: aaa
   apple
   ```
