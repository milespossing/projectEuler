class PanDigitalOperator:
    def __init__(self, length=10):
        self.values = range(0, length)

    def iterate(self, function):
        num = []
        self._iterate(function, num, self.values)

    def _iterate(self, function, num, vals):
        if len(vals) == 0:
            function(num)
        else:
            for v in vals:
                nVals = vals[:]
                nNum = num[:]
                nNum.append(v)
                nVals.remove(v)
                self._iterate(function,nNum,nVals)