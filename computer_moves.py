import random


class Computer_moves():

    def __init__(self, combined_symbol_status, comp_x, comp_y, move_count):
        self.combined_symbol_status = combined_symbol_status
        self.comp_x = comp_x
        self.comp_y = comp_y
        self.move_count = move_count

    def row_threat_checker(self):
        threat = False
        i = 0
        while(i < 7):
            p1 = self.combined_symbol_status[i] == "user" and self.combined_symbol_status[i +1] == "user" and self.combined_symbol_status[i + 2] == False
            p2 = self.combined_symbol_status[i] == "user" and self.combined_symbol_status[i +2] == "user" and self.combined_symbol_status[i + 1] == False
            p3 = self.combined_symbol_status[i + 1] == "user" and self.combined_symbol_status[i +2] == "user" and self.combined_symbol_status[i] == False
            if p1 is True or p2 == True or p3 == True:
                row_of_threat = i
                threat = True
                if p1 == True:
                    self.combined_symbol_status[i+2] = "comp"
                    self.comp_y[self.move_count] = 2
                    self.comp_x[self.move_count] = i/3
                elif p2 == True:
                    self.combined_symbol_status[i + 1] = "comp"
                    self.comp_y[self.move_count] = 1
                    self.comp_x[self.move_count] = i/3
                elif p3 == True:
                    self.combined_symbol_status[i] = "comp"
                    self.comp_y[self.move_count] = 0
                    self.comp_x[self.move_count] = i/3
            i = i + 3
        return threat

    def column_threat_checker(self):
        threat = False
        column_of_threat = 10
        i = 0
        while(i < 3):
            p1 = self.combined_symbol_status[i] == "user" and self.combined_symbol_status[i +
                                                                                          3] == "user" and self.combined_symbol_status[i + 6] == False
            p2 = self.combined_symbol_status[i] == "user" and self.combined_symbol_status[i +
                                                                                          6] == "user" and self.combined_symbol_status[i + 3] == False
            p3 = self.combined_symbol_status[i + 3] == "user" and self.combined_symbol_status[i +
                                                                                              6] == "user" and self.combined_symbol_status[i] == False
            if p1 == True or p2 == True or p3 == True:
                column_of_threat = i
                threat = True
                if p1 == True:
                    self.combined_symbol_status[i+6] = "comp"
                    self.comp_y[self.move_count] = i
                    self.comp_x[self.move_count] = 2
                elif p2 == True:
                    self.combined_symbol_status[i + 3] = "comp"
                    self.comp_y[self.move_count] = i
                    self.comp_x[self.move_count] = 1
                elif p3 == True:
                    self.combined_symbol_status[i] = "comp"
                    self.comp_y[self.move_count] = i
                    self.comp_x[self.move_count] = 0
            i = i + 1
        return threat

    def diagonal_threat_checker(self):
        diagonal_threat = False
        p1 = self.combined_symbol_status[0] == "user" and self.combined_symbol_status[4] == "user" and \
            self.combined_symbol_status[8] == False
        p2 = self.combined_symbol_status[0] == "user" and self.combined_symbol_status[8] == "user" and \
            self.combined_symbol_status[4] == False
        p3 = self.combined_symbol_status[4] == "user" and self.combined_symbol_status[8] == "user" and \
            self.combined_symbol_status[0] == False
        if p1 == True or p2 == True or p3 == True:
            diagonal_threat = True
            if p1 == True:
                self.combined_symbol_status[8] = "comp"
                self.comp_y[self.move_count] = 2
                self.comp_x[self.move_count] = 2
                return diagonal_threat

            elif p2 == True:
                self.combined_symbol_status[4] = "comp"
                self.comp_y[self.move_count] = 1
                self.comp_x[self.move_count] = 1
                return diagonal_threat

            elif p3 == True:
                self.combined_symbol_status[0] = "comp"
                self.comp_y[self.move_count] = 0
                self.comp_x[self.move_count] = 0
                return diagonal_threat

        p4 = self.combined_symbol_status[2] == "user" and self.combined_symbol_status[4] == "user" and self.combined_symbol_status[6] == False
        p5 = self.combined_symbol_status[2] == "user" and self.combined_symbol_status[6] == "user" and self.combined_symbol_status[4] == False
        p6 = self.combined_symbol_status[4] == "user" and self.combined_symbol_status[6] == "user" and self.combined_symbol_status[2] == False
        if p4 == True or p5 == True or p6 == True:
            diagonal_threat = True
            if p4 == True and p1 is False:
                self.combined_symbol_status[6] = "comp"
                self.comp_y[self.move_count] = 0
                self.comp_x[self.move_count] = 2
                return diagonal_threat

            elif p5 == True:
                self.combined_symbol_status[4] = "comp"
                self.comp_y[self.move_count] = 1
                self.comp_x[self.move_count] = 1
                return diagonal_threat

            elif p6 == True and p3 is False:
                self.combined_symbol_status[2] = "comp"
                self.comp_y[self.move_count] = 2
                self.comp_x[self.move_count] = 0
                return diagonal_threat

    def row_oppurtunity(self):
        oppurtunity = False
        i = 0
        while (i < 7):
            p1 = self.combined_symbol_status[i] == "comp" and self.combined_symbol_status[i + 1] == "comp" and \
                self.combined_symbol_status[i + 2] == False
            p2 = self.combined_symbol_status[i] == "comp" and self.combined_symbol_status[i + 2] == "comp" and \
                self.combined_symbol_status[i + 1] == False
            p3 = self.combined_symbol_status[i + 1] == "comp" and self.combined_symbol_status[i + 2] == "comp" and \
                self.combined_symbol_status[i] == False
            if p1 is True or p2 == True or p3 == True:
                oppurtunity = True
                if p1 == True:
                    self.combined_symbol_status[i + 2] = "comp"
                    self.comp_y[self.move_count] = 2
                    self.comp_x[self.move_count] = i/3

                elif p2 == True:
                    self.combined_symbol_status[i + 1] = "comp"
                    self.comp_y[self.move_count] = 1
                    self.comp_x[self.move_count] = i/3
                elif p3 == True:
                    self.combined_symbol_status[i] = "comp"
                    self.comp_y[self.move_count] = 0
                    self.comp_x[self.move_count] = i/3

            i = i + 3
        return oppurtunity

    def column_oppurtunity(self):
        oppurtunity = False
        i = 0
        while (i < 3):
            p1 = self.combined_symbol_status[i] == "comp" and self.combined_symbol_status[i + 3] == "comp" and \
                self.combined_symbol_status[i + 6] == False
            p2 = self.combined_symbol_status[i] == "comp" and self.combined_symbol_status[i + 6] == "comp" and \
                self.combined_symbol_status[i + 3] == False
            p3 = self.combined_symbol_status[i + 3] == "comp" and self.combined_symbol_status[i + 6] == "comp" and \
                self.combined_symbol_status[i] == False
            if p1 is True or p2 == True or p3 == True:
                oppurtunity = True
                if p1 == True:
                    self.combined_symbol_status[i + 6] = "comp"
                    self.comp_y[self.move_count] = i
                    self.comp_x[self.move_count] = 2
                elif p2 == True:
                    self.combined_symbol_status[i + 3] = "comp"
                    self.comp_y[self.move_count] = i
                    self.comp_x[self.move_count] = 1
                elif p3 == True:
                    self.combined_symbol_status[i] = "comp"
                    self.comp_y[self.move_count] = i
                    self.comp_x[self.move_count] = 0
            i = i + 1
        return oppurtunity

    def diagonal_oppurtunity(self):
        oppurtunity = False
        p1 = self.combined_symbol_status[0] == "comp" and self.combined_symbol_status[4] == "comp" and self.combined_symbol_status[8] == False
        p2 = self.combined_symbol_status[8] == "comp" and self.combined_symbol_status[4] == "comp" and self.combined_symbol_status[0] == False
        p3 = self.combined_symbol_status[0] == "comp" and self.combined_symbol_status[8] == "comp" and self.combined_symbol_status[4] == False

        if p1 is True or p2 == True or p3 == True:
            oppurtunity = True
            if p1 == True:
                self.combined_symbol_status[8] = "comp"
                self.comp_y[self.move_count] = 2
                self.comp_x[self.move_count] = 2
            elif p2 == True:
                self.combined_symbol_status[0] = "comp"
                self.comp_y[self.move_count] = 0
                self.comp_x[self.move_count] = 0
            elif p3 == True:
                self.combined_symbol_status[4] = "comp"
                self.comp_y[self.move_count] = 1
                self.comp_x[self.move_count] = 1

        p4 = self.combined_symbol_status[2] == "comp" and self.combined_symbol_status[4] == "comp" and \
            self.combined_symbol_status[6] == False
        p5 = self.combined_symbol_status[6] == "comp" and self.combined_symbol_status[4] == "comp" and \
            self.combined_symbol_status[2] == False
        p6 = self.combined_symbol_status[2] == "comp" and self.combined_symbol_status[6] == "comp" and \
            self.combined_symbol_status[4] == False

        if p4 is True or p5 == True or p6 == True:
            oppurtunity = True
            if p4 == True:
                self.combined_symbol_status[6] = "comp"
                self.comp_y[self.move_count] = 0
                self.comp_x[self.move_count] = 2
            elif p5 == True:
                self.combined_symbol_status[2] = "comp"
                self.comp_y[self.move_count] = 2
                self.comp_x[self.move_count] = 0
            elif p6 == True:
                self.combined_symbol_status[4] = "comp"
                self.comp_y[self.move_count] = 2
                self.comp_x[self.move_count] = 2

        return oppurtunity
