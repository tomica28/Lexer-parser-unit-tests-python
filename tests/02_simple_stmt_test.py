class SimpleStmt:
    def aug_assignment(self, arg):
        arg += 1
        arg -= 2
        arg *= 3
        arg /= 4
        arg %= 5

    def simple_stmts(self):
        pass
        print "test text"
        return 1
        return
        while True:
            break
        while False:
            continue
