class Case:
    def __init__(self, attribut ):

        self.attribut = attribut

    def __repr__(self):
        return "<attribut: {}>".format(self.attribut)