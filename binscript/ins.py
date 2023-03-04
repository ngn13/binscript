class Ins:
    def __init__(self):
        self.inss = {
            "hts": [self.hts_ins, 1],
            "sth": [self.sth_ins, 1],
            "stx": [self.stx_ins, 2],
            "ext": [self.ext_ins, 0],
            "add": [self.add_ins, 2],
            "sub": [self.sub_ins, 2],
            "set": [self.set_ins, 2],
            "out": [self.out_ins, 1],
            "cmb": [self.cmb_ins, 2],
            "len": [self.len_ins, 1]
        }

        self.sets = {"pre": "null"}
        self.out = True

    def preprs(self, prs):
        newprs = []
        for pr in prs:
            for se in self.sets.keys():
                pr = pr.replace("$"+se, self.sets[se])
            newprs.append(pr)
        return newprs

    ##########################
    # hex-to-string
    ##########################
    def hts_ins(self, prs):
        try:
            prs[0] = prs[0].replace("0x", "")
            return bytes.fromhex(prs[0]).decode("utf-8")
        except:
            return True

    ##########################
    # string-to-hex
    ##########################
    def sth_ins(self, prs):
        try:
            return "0x"+prs[0].encode("utf-8").hex()
        except:
            return True

    ##########################
    # string-times-X
    ##########################
    def stx_ins(self, prs):
        try:
            prs[1] = int(prs[1])
        except:
            return True

        return prs[0]*int(prs[1])

    ##########################
    # exit
    ##########################
    def ext_ins(self, prs):
        exit()

    ##########################
    # add
    ##########################
    def add_ins(self, prs):
        try:
            return hex(int(prs[0], 16)+int(prs[1], 16))
        except:
            return True

    ##########################
    # subtract
    ##########################
    def sub_ins(self, prs):
        try:
            return hex(int(prs[0], 16)-int(prs[1], 16))
        except:
            return True

    ##########################
    # set
    ##########################
    def set_ins(self, prs):
        self.sets[prs[0]] = prs[1]
        return ""

    ##########################
    # output
    ##########################
    def out_ins(self, prs):
        if prs[0] == "!":
            self.out = not self.out
            return ""
        return prs[0]

    ##########################
    # combine
    ##########################
    def cmb_ins(self, prs):
        return prs[0]+prs[1]

    ##########################
    # length
    ##########################
    def len_ins(self, prs):
        return len(prs[0])

