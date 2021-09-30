# -*- coding:utf-8 -*-

class MARCModel(object):

    isbn = ['ISBN']
    issn = ['ISSN']
    isrc = ['ISRC']
    ztm = ['正题名']
    zrz = ['责任者']
    cbs = ['出版社']
    cbd = ['出版地']
    cbrq = ['出版日期']
    cbzq = ['出版周期']
    fj = ['附件']
    flh = ['分类号']
    tyskh = ['统一书刊号']
    gndgh = ['国内订购号']
    gwdgh = ['国外订购号']
    smkzh = ['书目控制号']
    yz = ['语种']
    ym = ['页码']
    bc = ['版次']
    jg = ['价格']
    qkjg = ['期刊价格']
    cc = ['尺寸']
    ybzlbs = ['一般资料标识']
    ybxfz = ['一般性附注']
    ztc = ['主题词']
    zy = ['摘要']
    cbtm = ['丛编题名']
    cbzrz = ['丛编责任者']
    ztmpy = ['正题名拼音']
    zrzpy = ['责任者拼音']
    fjm = ['分辑名']
    ftm = ['副题名']
    fjh = ['分辑号']
    bltm = ['并列题名']
    qtzrz = ['其他责任者']
    bbysmsfz = ['版本与书目史附注']
    blztm = ['并列正题名']
    fmtm = ['封面题名']
    zz = ['著者']
    lyzzztm = ['另一作者正题名']

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.set_isbn(v) if k is "isbn" and v is not None else self.isbn
            self.set_issn(v) if k is "issn" and v is not None else self.issn
            self.set_isrc(v) if k is "isrc" and v is not None else self.isrc
            self.set_ztm(v) if k is "ztm" and v is not None else self.ztm
            self.set_zrz(v) if k is "zrz" and v is not None else self.zrz
            self.set_cbs(v) if k is "cbs" and v is not None else self.cbs
            self.set_cbd(v) if k is "cbd" and v is not None else self.cbd
            self.set_cbrq(v) if k is "cbrq" and v is not None else self.cbrq
            self.set_cbzq(v) if k is "cbzq" and v is not None else self.cbzq
            self.set_fj(v) if k is "fj" and v is not None else self.fj
            self.set_flh(v) if k is "flh" and v is not None else self.flh
            self.set_tyskh(v) if k is "tyskh" and v is not None else self.tyskh
            self.set_gndgh(v) if k is "gndgh" and v is not None else self.gndgh
            self.set_gwdgh(v) if k is "gwdgh" and v is not None else self.gwdgh
            self.set_smkzh(v) if k is "smkzh" and v is not None else self.smkzh
            self.set_yz(v) if k is "yz" and v is not None else self.yz
            self.set_ym(v) if k is "ym" and v is not None else self.ym
            self.set_bc(v) if k is "bc" and v is not None else self.bc
            self.set_jg(v) if k is "jg" and v is not None else self.jg
            self.set_qkjg(v) if k is "qkjg" and v is not None else self.qkjg
            self.set_cc(v) if k is "cc" and v is not None else self.cc
            self.set_ybzlbs(v) if k is "ybzlbs" and v is not None else self.ybzlbs
            self.set_ybxfz(v) if k is "ybxfz" and v is not None else self.ybxfz
            self.set_ztc(v) if k is "ztc" and v is not None else self.ztc
            self.set_zy(v) if k is "zy" and v is not None else self.zy
            self.set_cbtm(v) if k is "cbtm" and v is not None else self.cbtm
            self.set_cbzrz(v) if k is "cbzrz" and v is not None else self.cbzrz
            self.set_ztmpy(v) if k is "ztmpy" and v is not None else self.ztmpy
            self.set_zrzpy(v) if k is "zrzpy" and v is not None else self.zrzpy
            self.set_fjm(v) if k is "fjm" and v is not None else self.fjm
            self.set_ftm(v) if k is "ftm" and v is not None else self.ftm
            self.set_fjh(v) if k is "fjh" and v is not None else self.fjh
            self.set_bltm(v) if k is "bltm" and v is not None else self.bltm
            self.set_qtzrz(v) if k is "qtzrz" and v is not None else self.qtzrz
            self.set_bbysmsfz(v) if k is "bbysmsfz" and v is not None else self.bbysmsfz
            self.set_blztm(v) if k is "blztm" and v is not None else self.blztm
            self.set_fmtm(v) if k is "fmtm" and v is not None else self.fmtm
            self.set_zz(v) if k is "zz" and v is not None else self.zz
            self.set_lyzzztm(v) if k is "lyzzztm" and v is not None else self.lyzzztm

    def set_isbn(self, value):
        try:
            self.isbn[1] = value
        except IndexError:
            self.isbn.append(value)

    def set_issn(self, value):
        try:
            self.issn[1] = value
        except IndexError:
            self.issn.append(value)

    def set_isrc(self, value):
        try:
            self.isrc[1] = value
        except IndexError:
            self.isrc.append(value)

    def set_ztm(self, value):
        try:
            self.ztm[1] = value
        except IndexError:
            self.ztm.append(value)

    def set_zrz(self, value):
        try:
            self.zrz[1] = value
        except IndexError:
            self.zrz.append(value)

    def set_cbs(self, value):
        try:
            self.cbs[1] = value
        except IndexError:
            self.cbs.append(value)

    def set_cbd(self, value):
        try:
            self.cbd[1] = value
        except IndexError:
            self.cbd.append(value)

    def set_cbrq(self, value):
        try:
            self.cbrq[1] = value
        except IndexError:
            self.cbrq.append(value)

    def set_cbzq(self, value):
        try:
            self.cbzq[1] = value
        except IndexError:
            self.cbzq.append(value)

    def set_fj(self, value):
        try:
            self.fj[1] = value
        except IndexError:
            self.fj.append(value)

    def set_flh(self, value):
        try:
            self.flh[1] = value
        except IndexError:
            self.flh.append(value)

    def set_tyskh(self, value):
        try:
            self.tyskh[1] = value
        except IndexError:
            self.tyskh.append(value)

    def set_gndgh(self, value):
        try:
            self.gndgh[1] = value
        except IndexError:
            self.gndgh.append(value)

    def set_gwdgh(self, value):
        try:
            self.gwdgh[1] = value
        except IndexError:
            self.gwdgh.append(value)

    def set_smkzh(self, value):
        try:
            self.smkzh[1] = value
        except IndexError:
            self.smkzh.append(value)

    def set_yz(self, value):
        try:
            self.yz[1] = value
        except IndexError:
            self.yz.append(value)

    def set_ym(self, value):
        try:
            self.ym[1] = value
        except IndexError:
            self.ym.append(value)

    def set_bc(self, value):
        try:
            self.bc[1] = value
        except IndexError:
            self.bc.append(value)

    def set_jg(self, value):
        try:
            self.jg[1] = value
        except IndexError:
            self.jg.append(value)

    def set_qkjg(self, value):
        try:
            self.qkjg[1] = value
        except IndexError:
            self.qkjg.append(value)

    def set_cc(self, value):
        try:
            self.cc[1] = value
        except IndexError:
            self.cc.append(value)

    def set_ybzlbs(self, value):
        try:
            self.ybzlbs[1] = value
        except IndexError:
            self.ybzlbs.append(value)

    def set_ybxfz(self, value):
        try:
            self.ybxfz[1] = value
        except IndexError:
            self.ybxfz.append(value)

    def set_ztc(self, value):
        try:
            self.ztc[1] = value
        except IndexError:
            self.ztc.append(value)

    def set_zy(self, value):
        try:
            self.zy[1] = value
        except IndexError:
            self.zy.append(value)

    def set_cbtm(self, value):
        try:
            self.cbtm[1] = value
        except IndexError:
            self.cbtm.append(value)

    def set_cbzrz(self, value):
        try:
            self.cbzrz[1] = value
        except IndexError:
            self.cbzrz.append(value)

    def set_ztmpy(self, value):
        try:
            self.ztmpy[1] = value
        except IndexError:
            self.ztmpy.append(value)

    def set_zrzpy(self, value):
        try:
            self.zrzpy[1] = value
        except IndexError:
            self.zrzpy.append(value)

    def set_fjm(self, value):
        try:
            self.fjm[1] = value
        except IndexError:
            self.fjm.append(value)

    def set_ftm(self, value):
        try:
            self.ftm[1] = value
        except IndexError:
            self.ftm.append(value)

    def set_fjh(self, value):
        try:
            self.fjh[1] = value
        except IndexError:
            self.fjh.append(value)

    def set_bltm(self, value):
        try:
            self.bltm[1] = value
        except IndexError:
            self.bltm.append(value)

    def set_qtzrz(self, value):
        try:
            self.qtzrz[1] = value
        except IndexError:
            self.qtzrz.append(value)

    def set_bbysmsfz(self, value):
        try:
            self.bbysmsfz[1] = value
        except IndexError:
            self.bbysmsfz.append(value)

    def set_blztm(self, value):
        try:
            self.blztm[1] = value
        except IndexError:
            self.blztm.append(value)

    def set_fmtm(self, value):
        try:
            self.fmtm[1] = value
        except IndexError:
            self.fmtm.append(value)

    def set_zz(self, value):
        try:
            self.zz[1] = value
        except IndexError:
            self.zz.append(value)

    def set_lyzzztm(self, value):
        try:
            self.lyzzztm[1] = value
        except IndexError:
            self.lyzzztm.append(value)

    def get_isbn(self):
        return self.isbn

    def get_issn(self):
        return self.issn

    def get_isrc(self):
        return self.isrc

    def get_ztm(self):
        return self.ztm

    def get_zrz(self):
        return self.zrz

    def get_cbs(self):
        return self.cbs

    def get_cbd(self):
        return self.cbd

    def get_cbrq(self):
        return self.cbrq

    def get_cbzq(self):
        return self.cbzq

    def get_fj(self):
        return self.fj

    def get_flh(self):
        return self.flh

    def get_tyskh(self):
        return self.tyskh

    def get_gndgh(self):
        return self.gndgh

    def get_gwdgh(self):
        return self.gwdgh

    def get_smkzh(self):
        return self.smkzh

    def get_yz(self):
        return self.yz

    def get_ym(self):
        return self.ym

    def get_bc(self):
        return self.bc

    def get_jg(self):
        return self.jg

    def get_qkjg(self):
        return self.qkjg

    def get_cc(self):
        return self.cc

    def get_ybzlbs(self):
        return self.ybzlbs

    def get_ybxfz(self):
        return self.ybxfz

    def get_ztc(self):
        return self.ztc

    def get_zy(self):
        return self.zy

    def get_cbtm(self):
        return self.cbtm

    def get_cbzrz(self):
        return self.cbzrz

    def get_ztmpy(self):
        return self.ztmpy

    def get_zrzpy(self):
        return self.zrzpy

    def get_fjm(self):
        return self.fjm

    def get_ftm(self):
        return self.ftm

    def get_fjh(self):
        return self.fjh

    def get_bltm(self):
        return self.bltm

    def get_qtzrz(self):
        return self.qtzrz

    def get_bbysmsfz(self):
        return self.bbysmsfz

    def get_blztm(self):
        return self.blztm

    def get_fmtm(self):
        return self.fmtm

    def get_zz(self):
        return self.zz

    def get_lyzzztm(self):
        return self.lyzzztm




if __name__ == "__main__":
    # aa = {"isbn": "111"}
    # a = MARCModel(**aa)
    # a.set_isbn('aaa')
    # # a.set_issn('aaa')
    # c = a.get_isbn()
    # d = a.get_issn()
    # print(c, d)
    a = []
    a[1] = 1

    print(a)