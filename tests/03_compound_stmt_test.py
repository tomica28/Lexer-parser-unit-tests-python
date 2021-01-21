import lib_test

class CompoundStmts(Object):
    def if_stmt(self, arg):
        if arg == 0:
            return 1
        elif arg == 2:
            return 2
        else:
            return 3
    def while_stmt(self, arg):
        i = 5
        while arg is True:
            i += 2
            if i > 20:
                arg = False
            else:
                print i
