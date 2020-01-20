def picnicF(picnicItems, LWidth, RWidth):
    print('Picnic List!'.center(LWidth + RWidth, '-'))
    for k,v in picnicItems.items():
        print((k.ljust(LWidth, '.')) + str(v).rjust(RWidth))

picnicItems = {'sandwiches': 3, 'hotdogs': 2, 'juice': 7, 'beer': 10}
picnicF(picnicItems, 10, 20)
