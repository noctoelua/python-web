class test():
    def __init__(self):
        self.test1 = 1
        self.test0 = 0

TEST=test()

if hasattr(TEST, "test2"):
    print("TEST")
else:
    print("nyan")
