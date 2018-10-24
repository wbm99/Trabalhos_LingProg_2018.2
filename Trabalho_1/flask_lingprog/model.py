class Pessoa():
    def __init__(self, name, rg, age, phone1):
        self._name = name
        self._rg = rg
        self._age = age
        self._phone1 = phone1

    def getName(self):
        return self._name
    def getAge(self):
        return self._age
    def getRG(self):
        return self._rg
    def getPhone(self):
        return self._phone1

class Aluno(Pessoa):
    def __init__(self, name, rg, age, phone2, code, p1, p2, dre):
        super().__init__(name,rg,age,phone2)
        self._code = code
        self._p1 = p1
        self._p2 = p2
        self._dre = dre
        self._mf = (self._p1 + self._p2)*0.5
        self._mf = "{:.2f}".format(self._mf)

    def getCode(self):
        return self._code
    def getP1(self):
        return self._p1
    def getP2(self):
        return self._p2
    def getDRE(self):
        return self._dre
    def getFinalGrade(self):
        return self._mf
    def getSituation(self):
        if(float(self._mf) >= 5):
            return 'Aprovado'
        else:
            return 'Reprovado'
