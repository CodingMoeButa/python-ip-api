#!/usr/bin/python3

class IPv4Pool:
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    e1 = 0
    e2 = 0
    e3 = 0
    e4 = 0

    def __init__(self, curip, endip):
        self.c1 = int(curip.split('.')[0])
        self.c2 = int(curip.split('.')[1])
        self.c3 = int(curip.split('.')[2])
        self.c4 = int(curip.split('.')[3])
        self.e1 = int(endip.split('.')[0])
        self.e2 = int(endip.split('.')[1])
        self.e3 = int(endip.split('.')[2])
        self.e4 = int(endip.split('.')[3])

    def get(self):
        return str(self.c1)+ '.' + str(self.c2) + '.' + str(self.c3) + '.' + str(self.c4)

    def next(self):
        f1 = False
        f2 = False
        f3 = False
        f4 = False
        if self.c4 >= 255:
            f4 = True
            self.c4 = 0
            if self.c3 >= 255:
                f3 = True
                self.c3 = 0
                if self.c2 >= 255:
                    f2 = True
                    self.c2 = 0
                    if self.c1 >= 255:
                        f1 = True
                        self.c1 = 0
                    else:
                        self.c1 = self.c1 + 1
                else:
                    self.c2 = self.c2 + 1
            else:
                self.c3 = self.c3 + 1
        else:
            self.c4 = self.c4 + 1
        if self.c1 < self.e1:
            return True
        else:
            if self.c2 < self.e2:
                return True
            else:
                if self.c3 < self.e3:
                    return True
                else:
                    if self.c4 < self.e4:
                        return True
                    else:
                        return False

    def next256(self):
        f1 = False
        f2 = False
        f3 = False
        if self.c3 >= 255:
            f3 = True
            self.c3 = 0
            if self.c2 >= 255:
                f2 = True
                self.c2 = 0
                if self.c1 >= 255:
                    f1 = True
                    self.c1 = 0
                else:
                    self.c1 = self.c1 + 1
            else:
                self.c2 = self.c2 + 1
        else:
            self.c3 = self.c3 + 1
        if self.c1 < self.e1:
            return True
        else:
            if self.c2 < self.e2:
                return True
            else:
                if self.c3 < self.e3:
                    return True
                else:
                    return False