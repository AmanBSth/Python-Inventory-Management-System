def readFile():
    ''' the function displays all the avialbale laptop whenever its called'''
    print("S.N. \t\tModel\t\tBrand\t\tQuantity\tprice\t\tProcessor")
    print("-----------------------------------------------------------------------------------------------------")
    with open("laptop.txt", "r") as o:
        a = 1
        for line in o:
            print(a, "\t\t" + line.replace(",", "\t\t"))
            print("-----------------------------------------------------------------------------------------------------")
            a = a + 1               
        o.close()
