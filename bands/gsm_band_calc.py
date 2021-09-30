#!--utf-8--

from math import floor, ceil

#data visualize as a table
def table(col,title='TABLE'):
    title = title.replace('\n','')
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
    if tl<0:
        tl = 0
        title=title[:len(tdata)-6]+'...'
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


class GSM:
    c_freq = 0
    c_arfc = -1
    def __init__(self, d):
        d = d.split(';')
        self.name = d[0]
        self.dl = [float(d[1]),float(d[3])]
        self.bandwith = float(d[4])
        self.ul = [float(d[5]),float(d[7])]
        self.tx_rx = int(d[8])
        if d[9]=='dynamic': self.arfcn1 = self.arfcn2 = None
        elif '+' in d[9]:
            tmp = d[9].split('+')
            self.arfcn2 = [int(tmp[0].split('-')[0]),int(tmp[0].split('-')[1])]
            self.arfcn1 = [int(tmp[1].split('-')[0]),int(tmp[1].split('-')[1])]
        else:
            tmp = d[9].split('-')
            self.arfcn1 = [int(tmp[0]),int(tmp[1])]
            self.arfcn2 = None
    
    def f2i(self,num):
        n = num * 10
        if n%10>5: return ceil(num)
        else: return floor(num)

    @property
    def check_dfreq(self):
        f = float(self.c_freq)
        if (f>=self.dl[0] and f<=self.dl[1]): return True
        return False
        
    @property
    def check_ufreq(self):
        f = float(self.c_freq)
        if (f>=self.ul[0] and f<=self.ul[1]): return True
        return False

    @property 
    def check_arfcn1(self):
        a = int(self.c_arfc)
        if (not self.arfcn1==None):
            if (a>=self.arfcn1[0] and a<=self.arfcn1[1]): return True
        return False

    @property
    def check_arfcn2(self):
        a = int(self.c_arfc)
        if (not self.arfcn2==None):
            if (a>=self.arfcn2[0] and a<=self.arfcn2[1]): return True
        return False

    @property #sets the lowest arfcn
    def arfcn_low(self):
        if (not self.arfcn2==None):
            if self.arfcn2[0]<int(self.c_arfc):
                return self.arfcn1[0]
            else: return self.arfcn2[0]
        else: return self.arfcn1[0]

    @property
    def uplink(self): #freq = ful_low + 0.2*(arfcn-arfcn_low)
        if self.c_arfc<self.arfcn_low: #900 E, 900 R, 900 ER overlaps on 900 P
            return self.ul[0] + 0.2*(int(self.c_arfc+1024)-self.arfcn_low)
        return self.ul[0] + 0.2*(int(self.c_arfc)-self.arfcn_low)
    
    @property
    def downlink(self): #freq = duplex_spacing + uplink
        return self.uplink + self.tx_rx
##        if self.c_arfc<self.arfcn_low:
##            return self.ul[0] + 0.2*(int(self.c_arfc+1024)-self.arfcn_low) + self.tx_rx
##        return self.ul[0] + 0.2*(int(self.c_arfc)-self.arfcn_low) + self.tx_rx
    
    @property
    def arfcn(self): #arfcn = arfcn_low + 5*(freq-ful_low-duplex_spacing)
        if self.check_dfreq:
            self.c_arfc = self.f2i(self.arfcn1[0] + 5*(self.c_freq-self.ul[0]-self.tx_rx))
            if self.c_arfc>1023:
                self.c_arfc = self.c_arfc - 1024
            return self.c_arfc
        if self.check_ufreq:
            self.c_arfc = self.f2i(self.arfcn1[0] + 5*(self.c_freq-self.ul[0]))
            if self.c_arfc>1023:
                self.c_arfc = self.c_arfc - 1024
            return self.c_arfc
        return None

def GSM_arfcn(xd,xt):
    #loads data file
    #GSM_Bands_csv = open('data/GSM_arfcn.csv').readlines()[1:]
    data = "380 T-GSM;390.2;395;399.8;9.6;380.2;385;389.8;10;dynamic;/410 T-GSM;420.2;425;429.8;9.6;410.2;415;419.8;10;dynamic;/450;460.6;464;467.4;6.8;450.6;454;457.4;10;259-293;/480;489;492.4;495.8;6.8;479;482.4;485.8;10;306-340;/710;728.2;737.2;746.2;18;698.2;707.2;716.2;30;dynamic;/750;747.2;755.2;763.2;16;777.2;785.2;793.2;-30;dynamic;/810 T-GSM;851.2;858.7;866.2;15;806.2;813.7;821.2;45;dynamic;/850;869.2;881.5;893.8;24.6;824.2;836.5;848.8;45;128-251;/900 P;935.2;947.5;959.8;24.6;890.2;902.5;914.8;45;1-124;/900 E;925.2;942.5;959.8;34.6;880.2;897.5;914.8;45;0-124+975-1023;/900 R;921.2;940.5;959.8;38.6;876.2;895.5;914.8;45;0-124+955-1023;/900 ER;918.2;939;959.8;41.6;873.2;894;914.8;45;0-124+940-1023;/1800 DCS;1805.2;1842.5;1879.8;74.6;1710.2;1747.5;1784.8;95;512-885;/1900 PCS;1930.2;1960;1989.8;59.6;1850.2;1880;1909.8;80;512-810;".split('/')
    col = [['Band','Arfcn','Downlink (MHz)','Uplink (MHz)']]
    if xt=='a':
        xd = int(xd)
        for i in GSM_Bands_csv:
            a = GSM(i)
            arfcn = xd
            a.c_arfc = arfcn
            if a.check_arfcn1 or a.check_arfcn2:
                col.append([a.name,arfcn,"%.2f"%a.downlink,"%.2f"%a.uplink])
            #print(a.name,a.dl,a.bandwith,a.ul,a.tx_rx,a.arfcn1,a.arfcn2)
        print(table(col, 'GSM_ARFCN_TO_FREQUENCY'))
    elif xt=='f':
        xd = float(xd)
        for i in GSM_Bands_csv:
            a = GSM(i)
            freq = xd
            a.c_freq = freq
            if a.check_dfreq:# or a.check_dfreq:
                col.append([a.name,a.arfcn,"%.2f"%freq,"%.2f"%(freq-a.tx_rx)])
            if a.check_ufreq:# or a.check_dfreq:
                col.append([a.name,a.arfcn,"%.2f"%(freq+a.tx_rx),"%.2f"%freq])
            #print(a.name,a.dl,a.bandwith,a.ul,a.tx_rx,a.arfcn1,a.arfcn2)
        print(table(col, 'GSM_FREQUENCY_TO_ARFCN'))
    else: print("use as GSM_arfcn(xd=891.2,xt='f'/'a')")

#GSM_arfcn(891.2,'f')
#GSM_arfcn(120,'a')

