class Date:
    def __init__(self, day, month):
        self.day = day
        self.month = month
        
    def __le__(self, other):
        if self.month < other.month:
            return True
        elif self.month == other.month:
            if self.day <= other.day:
                return True
            else:
                return False
        else:
            return False
    
    def __ge__(self, other):
        if self.month > other.month:
            return True
        elif self.month == other.month:
            if self.day >= other.day:
                return True
            else:
                return False
        else:
            return False


def oneTime():
    dm = input().split()
    date = Date(int(dm[0]), int(dm[1]))

    if date >= Date(20, 1) and date <= Date(18, 2):
        print('Bao Binh')
    elif date >= Date(19, 2) and date <= Date(20, 3):
        print('Song Ngu')
    elif date >= Date(21, 3) and date <= Date(19, 4):
        print('Bach Duong')
    elif date >= Date(20, 4) and date <= Date(20, 5):
        print('Kim Nguu')
    elif date >= Date(21, 5) and date <= Date(20, 6):
        print('Song Tu')
    elif date >= Date(21, 6) and date <= Date(22, 7):
        print('Cu Giai')
    elif date >= Date(23, 7) and date <= Date(22, 8):
        print('Su Tu')
    elif date >= Date(23, 8) and date <= Date(22, 9):
        print('Xu Nu')
    elif date >= Date(23, 9) and date <= Date(22, 10):
        print('Thien Binh')
    elif date >= Date(23, 10) and date <= Date(22, 11):
        print('Thien Yet')
    elif date >= Date(23, 11) and date <= Date(21, 12):
        print('Nhan Ma')
    else:
        print('Ma Ket')


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        oneTime()
