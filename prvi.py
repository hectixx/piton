def poisci(tabela, element):
    for i in range (len(tabela)):
        if tabela[i] == element:
            return i
    
    
    
    
    return -1        #matic je supak






def main():
    tabela = [7, 10, 15, 21, 27, 30, 31, 34, 37, 39, 42, 50, 58, 61, 75]

    print(poisci(tabela, 42))
    print(poisci(tabela, 29))

main()



