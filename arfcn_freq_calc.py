# -*- coding: utf-8 -*-
#author hossainel 

from math import floor, ceil

class GSM_arfcn:
    full_overlap = ['900 E','900 R','900 ER']
    GSM_BANDS = [
        {
            'name':'380 T-GSM',
            'dl':[390.2,399.8], #downlink - Low High (MHz)
            'bandwith':9.6, #MHz
            'ul':[380.2,389.8], #uplink - Low High (MHz)
            'arfcn':[0,0], #channel - Low High (MHz)
            'tx_rx':10 #duplex spacing (MHz)
        }, {
            'name':'410 T-GSM',
            'dl':[420.2,429.8], #downlink - Low High (MHz)
            'bandwith':9.6, #MHz
            'ul':[410.2,419.8], #uplink - Low High (MHz)
            'arfcn':[0,0], #channel - Low High (MHz)
            'tx_rx':10 #duplex spacing (MHz)
        }, {
            'name':'450',
            'dl':[460.6,467.4], #downlink - Low High (MHz)
            'bandwith':6.8, #MHz
            'ul':[450.6,457.4], #uplink - Low High (MHz)
            'arfcn':[259,293], #channel - Low High (MHz)
            'tx_rx':10 #duplex spacing (MHz)
        }, {
            'name':'480',
            'dl':[489,495.8], #downlink - Low High (MHz)
            'bandwith':6.8, #MHz
            'ul':[479,457.4], #uplink - Low High (MHz)
            'arfcn':[306,340], #channel - Low High (MHz)
            'tx_rx':10 #duplex spacing (MHz)
        }, {
            'name':'710',
            'dl':[728.2,746.2], #downlink - Low High (MHz)
            'bandwith':18, #MHz
            'ul':[698.2,716.2], #uplink - Low High (MHz)
            'arfcn':[0,0], #channel - Low High (MHz)
            'tx_rx':30 #duplex spacing (MHz)
        }, {
            'name':'750',
            'dl':[747.2,763.2], #downlink - Low High (MHz)
            'bandwith':16, #MHz
            'ul':[777.2,793.2], #uplink - Low High (MHz)
            'arfcn':[0,0], #channel - Low High (MHz)
            'tx_rx':-30 #duplex spacing (MHz)
        }, {
            'name':'810 T-GSM',
            'dl':[851.2,866.2], #downlink - Low High (MHz)
            'bandwith':15, #MHz
            'ul':[806.2,821.2], #uplink - Low High (MHz)
            'arfcn':[0,0], #channel - Low High (MHz)
            'tx_rx':45 #duplex spacing (MHz)
        }, {
            'name':'850',
            'dl':[869.2,893.8], #downlink - Low High (MHz)
            'bandwith':24.6, #MHz
            'ul':[824.2,848.8], #uplink - Low High (MHz)
            'arfcn':[128,251], #channel - Low High (MHz)
            'tx_rx':45 #duplex spacing (MHz)
        }, {
            'name':'900 P',
            'dl':[935.2,959.8], #downlink - Low High (MHz)
            'bandwith':24.6, #MHz
            'ul':[890.2,914.8], #uplink - Low High (MHz)
            'arfcn':[1,124], #channel - Low High (MHz)
            'tx_rx':45 #duplex spacing (MHz)
        }, {
            'name':'900 E',
            'dl':[925.2,959.8], #downlink - Low High (MHz)
            'bandwith':34.6, #MHz
            'ul':[880.2,914.8], #uplink - Low High (MHz)
            'arfcn':[(0,975),(124,1023)], #channel - Low High (MHz)
            'tx_rx':45 #duplex spacing (MHz)
        }, {
            'name':'900 R',
            'dl':[921.2,959.8], #downlink - Low High (MHz)
            'bandwith':38.6, #MHz
            'ul':[876.2,914.8], #uplink - Low High (MHz)
            'arfcn':[(0,955),(124,1023)], #channel - Low High (MHz)
            'tx_rx':45 #duplex spacing (MHz)
        }, {
            'name':'900 ER',
            'dl':[918.2,959.8], #downlink - Low High (MHz)
            'bandwith':41.6, #MHz
            'ul':[873.2,914.8], #uplink - Low High (MHz)
            'arfcn':[(0,940),(124,1023)], #channel - Low High (MHz)
            'tx_rx':45 #duplex spacing (MHz)
        }, {
            'name':'1800 DCS',
            'dl':[1805.2,1879.8], #downlink - Low High (MHz)
            'bandwith':74.6, #MHz
            'ul':[1710.2,1784.8], #uplink - Low High (MHz)
            'arfcn':[512,885], #channel - Low High (MHz)
            'tx_rx':95 #duplex spacing (MHz)
        }, {
            'name':'1900 PCS',
            'dl':[1930.2,1989.8], #downlink - Low High (MHz)
            'bandwith':59.6, #MHz
            'ul':[1850.2,1909.8], #uplink - Low High (MHz)
            'arfcn':[512,810], #channel - Low High (MHz)
            'tx_rx':80 #duplex spacing (MHz)
        }
    ]

    #data visualize as a table
    def table(col,title='TABLE'):
        n_row = len(col)
        n_col = len(col[0])
        t = [0 for i in range(n_col)]
        bar = '+'
        for i in range(n_row):
            for j in range(n_col):
                t[j] = max(t[j],len(str(col[i][j])))
        tdata = "+"
        for i in t:
            tdata = tdata + '-' * i + '+'
        tdata = tdata + '\n'
        tl = len(tdata)-len(title)-3
        title23 = '+' + '-' * (len(tdata)-3) + '+\n'

        tl2 = tl//2
        if tl%2: tl3 = tl2+1
        else: tl3 = tl2
        
        title = title23 + '|' + ' ' * tl2 + title + ' ' * tl3 + '|\n'        
        data = title + tdata
        for i in range(n_row):
            r = "|"
            for j in range(n_col):
                d = str(col[i][j])
                tl = t[j] - len(d)
                tl2 = tl//2
                if tl%2: tl3 = tl2+1
                else: tl3 = tl2
                r = r + ' ' * tl2 + d + ' ' * tl3 + '|'
            data = data + r + '\n' + tdata
                
        return data

    def middle(a,b): return (a+b)/2

    def arfcn_low(arfcn,arfcn2):
        arfcn_low = arfcn
        if type(arfcn_low)==tuple:
            if arfcn_low[0]<arfcn2: return arfcn_low[1]
            else: return arfcn_low[0]
        else: return arfcn_low
        
    def uplink_freq(i,arfcn):
        ful_low = i['ul'][0]
        arfcn_low = GSM_arfcn.arfcn_low(i['arfcn'][0],arfcn)
        freq = ful_low + 0.2*(arfcn-arfcn_low)
        return freq

    def downlink_freq(i,arfcn):
        duplex_spacing = i['tx_rx']
        ful_low = i['ul'][0]
        arfcn_low = GSM_arfcn.arfcn_low(i['arfcn'][0],arfcn)
        freq = duplex_spacing + ful_low + 0.2*(arfcn-arfcn_low)
        return freq

    def check_arfcn(i,arfcn):
        arfcn=int(arfcn)
        if type(i['arfcn'][0])==tuple:
            k = len(i['arfcn'][0])
            for j in range(k):
                if arfcn >= i['arfcn'][0][j] and arfcn <=i['arfcn'][1][j]:
                    return True
        else:
            if arfcn >= i['arfcn'][0] and arfcn <=i['arfcn'][1]:
                return True
        return False

    def f2i(num):
        n = num * 10
        if n%10>5: return ceil(num)
        else: return floor(num)
        
    def overlap(i,d,k='a'):
        P = {
            'name':'900 P',
            'dl':[935.2,959.8], #downlink - Low High (MHz)
            'bandwith':24.6, #MHz
            'ul':[890.2,914.8], #uplink - Low High (MHz)
            'arfcn':[1,124], #channel - Low High (MHz)
            'tx_rx':45 #duplex spacing (MHz)
        }
        if (k=='a' and i['name'] in GSM_arfcn.full_overlap) and (i['dl'][0] >= float(d[2]) or i['dl'][1] <= float(d[2]) or i['ul'][0] >= float(d[3]) or i['ul'][1] <= float(d[3])):
            d[2] = "%.2f"%GSM_arfcn.downlink_freq(P,d[1])
            d[3] = "%.2f"%GSM_arfcn.uplink_freq(P,d[1])
        if (k=='f' and i['name'] in GSM_arfcn.full_overlap) and (int(d[1])>1023):
            #arfcn = 1.0 + 5*(float(d[2])-935.2)
            arfcn = d[1]-1024
            d[1]=GSM_arfcn.f2i(arfcn)
##        if (k=='uf' and i['name'] in GSM_arfcn.full_overlap) and (int(d[1])>1023):
##            #arfcn = 1.0 + 5*(float(d[2])-890.2)
##            arfcn = d[1]-1024
##            d[1]=GSM_arfcn.f2i(arfcn)
        return d

    def arfcn2freq(arfcn):
        arfcn=int(arfcn)
        col = [['Band','Arfcn','Downlink(MHz)','Uplink (MHz)']]
        for i in GSM_arfcn.GSM_BANDS:
            if i['arfcn']==[0,0]: pass
            elif GSM_arfcn.check_arfcn(i,arfcn):
                row = [i['name'],arfcn,"%.2f"%GSM_arfcn.downlink_freq(i,arfcn),"%.2f"%GSM_arfcn.uplink_freq(i,arfcn)]
                overlap = GSM_arfcn.overlap(i,row,'a')
                col.append(overlap)
        print(GSM_arfcn.table(col, 'GSM_ARFCN_TO_FREQUENCY'))
        return 'Requested Arfcn : %i MHz'%arfcn

    def check_freq(i,link):
        link=float(link)
        if link >= i['dl'][0] and link <=i['dl'][1]: return 'd'
        elif link >= i['ul'][0] and link <=i['ul'][1]: return 'u'
        else: return 'n'

    def freq2arfcn(freq):
        freq = float(freq)
        col = [['Band','Arfcn','Downlink(MHz)','Uplink (MHz)']]
        for i in GSM_arfcn.GSM_BANDS:
            duplex_spacing = float(i['tx_rx'])
            ful_low = float(i['ul'][0])
            #arfcn_low1 = float(GSM_arfcn.arfcn_low(i['arfcn'][0],0))
            arfcn_low2 = float(GSM_arfcn.arfcn_low(i['arfcn'][0],125))
            cf = GSM_arfcn.check_freq(i,freq)
            if cf=='d':
                #arfcn1 = arfcn_low1 + 5*(freq-ful_low-duplex_spacing)
                arfcn2 = arfcn_low2 + 5*(freq-ful_low-duplex_spacing)
                #if arfcn1==arfcn2:
                row = [i['name'],GSM_arfcn.f2i(arfcn2),"%.2f"%freq,"%.2f"%(freq-duplex_spacing)]
                #else:
                    #row = [i['name'],"%i(%i)"%(GSM_arfcn.f2i(arfcn2),GSM_arfcn.f2i(arfcn1)),"%.2f"%freq,"%.2f"%(freq-duplex_spacing)]
                overlap = GSM_arfcn.overlap(i,row,'f')
                col.append(overlap)
            if cf=='u':
                #arfcn1 = arfcn_low1 + 5*(freq-ful_low)
                arfcn2 = arfcn_low2 + 5*(freq-ful_low)
                row = [i['name'],GSM_arfcn.f2i(arfcn2),"%.2f"%(freq+duplex_spacing),"%.2f"%freq]
                overlap = GSM_arfcn.overlap(i,row,'f')
                col.append(overlap)
                #col.append(row)
        print(GSM_arfcn.table(col, 'GSM_FREQUENCY_TO_ARFCN'))
        return 'Requested Frequency  : %.2f MHz'%freq


while 1:
    d = input('Arfcn[A]/Frequency (MHz)[F]>').upper()
    if d=='A':
        p = int(input('Arfcn:'))
        print(GSM_arfcn.arfcn2freq(p))
    elif d=='F':
        p = float(input('Frequency (MHz):'))
        print(GSM_arfcn.freq2arfcn(p))
    else:
        print('Only input [A]/[F]')
