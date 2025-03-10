"""
Provides utilities to en/decode a string with a number of encoding standards

by design, the tool supports many encodings, including obscure encodings

The tools also support en/decoding a string multiple times with either the same of different standards

For example 'encoding_string' can be decoded by base64 eight times, or decoded with base64 then base32 then base32 then base64

Each encoding has a standardized representation:
    base64, b64 - Base 64
    base32, b32 - Base 32
    base58, b58 - Base 58
    base16, b16 - Base 16 (Hexadecimal)
    utf8, utf-8 - UTF-8
    utf16, utf-16 - UTF-16
    utf32, utf-32 - UTF-32
    url - URL Encoding
    html - HTML Encoding
    shiftjs, sjs - ShiftJS Encoding
    rot13 - Rot 13 cipher
    hex, hexadecimal - Raw Hexadecimal
    bzip2, bzip - BZip2
    gzip - GZip
    brotli, brot - Brotli


"""

import base64
import base58
import urllib.parse
import html
import codecs
import bz2
import gzip
import brotli

# Base64 Encoding
def encode_base64(string):
    return base64.b64encode(string.encode('utf-8')).decode('utf-8')

# Base32 Encoding
def encode_base32(string):
    return base64.b32encode(string.encode('utf-8')).decode('utf-8')

# Base58 Encoding
def encode_base58(string):
    return base58.b58encode(string.encode('utf-8')).decode('utf-8')

# Base16 (Hexadecimal) Encoding
def encode_base16(string):
    return string.encode('utf-8').hex()

# UTF-8 Encoding
def encode_utf8(string):
    return string.encode('utf-8')

# URL Encoding (Percent Encoding)
def encode_url(string):
    return urllib.parse.quote(string)

# HTML Entity Encoding
def encode_html_entity(string):
    return html.escape(string)

# UTF-16 Encoding
def encode_utf16(string):
    return string.encode('utf-16')

# UTF-32 Encoding
def encode_utf32(string):
    return string.encode('utf-32')

# Shift_JIS Encoding
def encode_shift_jis(string):
    return string.encode('shift_jis')

# Rot13 Encoding
def encode_rot13(string):
    return codecs.encode(string, 'rot_13')

# Hexadecimal Encoding (Raw bytes)
def encode_hex(string):
    return string.encode('utf-8').hex()

# BZIP2 Encoding
def encode_bzip2(string):
    return bz2.compress(string.encode('utf-8'))

# Gzip Encoding
def encode_gzip(string):
    return gzip.compress(string.encode('utf-8'))

# Brotli Encoding
def encode_brotli(string):
    return brotli.compress(string.encode('utf-8'))

# Decode Base64
def decode_base64(string):
    return base64.b64decode(string).decode('utf-8')

# Decode Base32
def decode_base32(string):
    return base64.b32decode(string).decode('utf-8')

# Decode Base58
def decode_base58(string):
    return base58.b58decode(string).decode('utf-8')

# Decode Base16 (Hexadecimal)
def decode_base16(string):
    return bytes.fromhex(string).decode('utf-8')

# Decode UTF-8
def decode_utf8(string):
    return string.decode('utf-8')

# Decode URL Encoding (Percent Encoding)
def decode_url(string):
    return urllib.parse.unquote(string)

# Decode HTML Entity Encoding
def decode_html_entity(string):
    return html.unescape(string)

# Decode UTF-16
def decode_utf16(string):
    return string.decode('utf-16')

# Decode UTF-32
def decode_utf32(string):
    return string.decode('utf-32')

# Decode Shift_JIS (for Japanese text)
def decode_shift_jis(string):
    return string.decode('shift_jis')

# Decode ROT13
def decode_rot13(string):
    return codecs.decode(string, 'rot_13')

# Decode Hexadecimal (Raw bytes)
def decode_hex(string):
    return bytes.fromhex(string).decode('utf-8')

# Decode BZIP2
def decode_bzip2(string):
    return bz2.decompress(string).decode('utf-8')

# Decode Gzip
def decode_gzip(string):
    return gzip.decompress(string).decode('utf-8')

# Decode Brotli
def decode_brotli(string):
    return brotli.decompress(string).decode('utf-8')


encode_function_map = {
    'base64': encode_base64,
    'b64': encode_base64,
    'base32': encode_base32,
    'b32': encode_base32,
    'base58': encode_base58,
    'b58': encode_base58,
    'base16': encode_base16,
    'b16': encode_base16,
    'utf8': encode_utf8,
    'utf16': encode_utf16,
    'utf32': encode_utf32,
    'utf-8': encode_utf8,
    'utf-16': encode_utf16,
    'utf-32': encode_utf32,
    'url': encode_url,
    'html': encode_html_entity,
    'shiftjs': encode_shift_jis,
    'sjs': encode_shift_jis,
    'rot13': encode_rot13,
    'hex': encode_hex,
    'hexadecimal': encode_hex,
    'bzip': encode_bzip2,
    'bzip2': encode_bzip2,
    'gzip': encode_gzip,
    'brotli': encode_brotli,
    'brot': encode_brotli
}

decode_function_map = {
    'base64': decode_base64,
    'func2': decode_base32,
    'func2': decode_base58,
    'func2': decode_base16,
    'func2': decode_utf8,
    'func2': decode_url,
    'func2': decode_html_entity,
    'func2': decode_utf16,
    'func2': decode_utf32,
    'func2': decode_shift_jis,
    'func2': decode_rot13,
    'func2': decode_hex,
    'func2': decode_bzip2,
    'func2': decode_gzip,
    'func2': decode_brotli
}


def encode(text, encoding):
    # Encoding can have multiple encodings, in the form of ('base64, base32, base64, ascii')

    if "," in encoding:
        encoding = encoding.split(",")
    else:
        encoding = encoding.split()

    
    for code in encoding:
        code = code.strip()
        if code in encode_function_map:
            text = encode_function_map[code](text)

        else:
            print("Failed encoding:", code)
            raise Exception(f"Encoding not found.")

    print("encoded text:", text)
    # TODO: The functions take strings and return bytes, they need to be able to take bytes and return encoded bytes

    
"""
encode("hello", "utf16 utf32")
encode("hello", "utf16, utf32")

def decode(text, encoding):
    print("Decode")

def bruteforce(text):
    print("Brute fore decoding")

string="hello"

print("Base64:", encode_base64(string))
print("Base32:", encode_base32(string))
print("Base58:", encode_base58(string))
print("Base16 (Hexadecimal):", encode_base16(string))
print("UTF-8:", encode_utf8(string))
print("URL Encoding:", encode_url(string))
print("HTML Entity Encoding:", encode_html_entity(string))
print("UTF-16:", encode_utf16(string))
print("UTF-32:", encode_utf32(string))
print("Shift_JIS:", encode_shift_jis(string))
print("ROT13:", encode_rot13(string))
print("Hexadecimal (Raw):", encode_hex(string))

# Compression encodings
print("BZIP2:", encode_bzip2(string))
print("Gzip:", encode_gzip(string))
print("Brotli:", encode_brotli(string))





encoded_base64 = base64.b64encode(string.encode('utf-8')).decode('utf-8')
encoded_base32 = base64.b32encode(string.encode('utf-8')).decode('utf-8')
encoded_base58 = base58.b58encode(string.encode('utf-8')).decode('utf-8')
encoded_base16 = string.encode('utf-8').hex()
encoded_utf8 = string.encode('utf-8')
encoded_url = urllib.parse.quote(string)
encoded_html_entity = html.escape(string)
encoded_utf16 = string.encode('utf-16')
encoded_utf32 = string.encode('utf-32')
encoded_shift_jis = string.encode('shift_jis')
encoded_rot13 = codecs.encode(string, 'rot_13')
encoded_hex = string.encode('utf-8').hex()
encoded_bzip2 = bz2.compress(string.encode('utf-8'))
encoded_gzip = gzip.compress(string.encode('utf-8'))
encoded_brotli = brotli.compress(string.encode('utf-8'))

# Decoding examples
print("Base64 Decoded:", decode_base64(encoded_base64))
print("Base32 Decoded:", decode_base32(encoded_base32))
print("Base58 Decoded:", decode_base58(encoded_base58))
print("Base16 (Hexadecimal) Decoded:", decode_base16(encoded_base16))
print("UTF-8 Decoded:", decode_utf8(encoded_utf8))
print("URL Decoded:", decode_url(encoded_url))
print("HTML Entity Decoded:", decode_html_entity(encoded_html_entity))
print("UTF-16 Decoded:", decode_utf16(encoded_utf16))
print("UTF-32 Decoded:", decode_utf32(encoded_utf32))
print("Shift_JIS Decoded:", decode_shift_jis(encoded_shift_jis))
print("ROT13 Decoded:", decode_rot13(encoded_rot13))
print("Hexadecimal (Raw) Decoded:", decode_hex(encoded_hex))
print("BZIP2 Decoded:", decode_bzip2(encoded_bzip2))
print("Gzip Decoded:", decode_gzip(encoded_gzip))
print("Brotli Decoded:", decode_brotli(encoded_brotli))
"""