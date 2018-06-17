from MathPackage.PanDigitalOperator import PanDigitalOperator

o = PanDigitalOperator(4)

def printer(v):
    print(v)

o.iterate(printer)
