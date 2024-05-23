def ubah_huruf(sentence):
    def shift_letter(letter):
        if 'A' <= letter <= 'Z':
            return chr((ord(letter) - ord('A') + 10) % 26 + ord('A'))
        elif 'a' <= letter <= 'z':
            return chr((ord(letter) - ord('a') + 10) % 26 + ord('a'))
        else:
            return letter

    return ''.join(shift_letter(char) for char in sentence)

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE"))  # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY"))  # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA"))  # SXNYXOCSK
    print(ubah_huruf("GOLANG"))  # QYVKXQ
    print(ubah_huruf("PROGRAMMER"))  # ZBYQBKWWOB
