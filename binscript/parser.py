from binscript.ins import Ins

class Parser:
    def __init__(self):
        self.ins = Ins()

    def parse(self, lexd):
        preout = ""
        for line in lexd:   
            cins = ""
            prev = ""
            prs = []

            for ins in line:
                if cins == "":
                    cins = ins
                else:
                    prs.append(ins)
            
            try:
                rins = self.ins.inss[cins][0]
                prsz = self.ins.inss[cins][1]
            except:
                return True

            if len(prs) != prsz:
                return True
            prs = self.ins.preprs(prs)
            out = rins(prs)
            if out == True:
                return True
           
            if out != "":
                preout = out
                self.ins.sets["pre"] = preout
                if self.ins.out:
                    print(out)
                

