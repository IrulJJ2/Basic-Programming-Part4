def cetak_table_perkalian(number):
    pattern = ""
    for x in range(1,number+1):
        print (x, end="\t")
    print()
    for y in range (1, number+1):
        for z in range (1, number+1):
            print (y*z, end ="\t")
        print ("\n")
    return pattern

if __name__ == '__main__':
    print(cetak_table_perkalian(9))

