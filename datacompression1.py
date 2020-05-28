import libmicrocontest,sys,math,time,subprocess
import string,re # to search for the common patterns of letters in string
from collections import OrderedDict # to extract the repetitive letters in string
import textwrap
def decompressit(d):
    decompress = ''
    allmatch = re.findall('\d\D',d)
    for i in allmatch:
        time = int(i[0])   
        char = str(i[1])
        if time == 1:
            word = char
            decompress = decompress + word
        else:
            word = char*time
            decompress = decompress + word       
    return decompress
def compressit(c):#if order not matter
    compress = ''
    letters = OrderedDict.fromkeys(c)#extract the repetitive letters in compression string
    for l in letters:
        times = c.count(l)
        compress = compress+ str(times)+str(l)
    return compress    
def main():
    con = libmicrocontest.commence_contest(31,'kapslock','')
    compressor = con.get_str('donnees_a_compresser')
    decompressor = con.get_str('donnees_a_decompresser')
    print('[+]String to compress :: '+str(compressor))
    print('[+]String to decompress :: '+str(decompressor))
    r_compressor = compressit(compressor)
    print('[+]compression :: '+str(r_compressor))
    r_decompressor = decompressit(decompressor)
    print('[+]decompression :: '+str(r_decompressor))
    con.append_answer('resultat_compression',r_compressor)
    con.append_answer('resultat_decompression',r_decompressor)
    print(con.submit_answer())
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()