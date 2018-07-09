class Train:

    def __init__(self, index, tag, load, status, comment=None):
        self.index = index
        self.tag = tag
        self.load = load
        self.status = status
        self.comment = comment

    def toDict(self):
        return {
            "index": self.index,
            "tag": self.tag,
            "load": self.load,
            "status": self.status,
            "comment": self.comment
        }

