class Permuter:
    def __init__(self, options, length):
        self.length = length
        self.options = options
        self.optionsStack = []
        self.arrayStack = []

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self, array, options):
        if len(options) > 1:
            for i in range(0,len(options)):
                arrayCopy = array[:]
                optionsCopy = options[:]
                arrayCopy.append(options[i])
                optionsCopy.remove(options[i])
                self.next(arrayCopy, optionsCopy)
        else:
            array.append(options[0])
            return array
