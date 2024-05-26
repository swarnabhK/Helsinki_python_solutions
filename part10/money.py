# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        c = f"0{self._cents}" if 0<=self._cents<=9 else self._cents
        return f"{self._euros}.{c} eur"

    def __eq__(self,another):
        return self._euros == another._euros and self._cents==another._cents

    def __ne__(self,another):
        return not (self._euros == another._euros and self._cents==another._cents)

    def __gt__(self,another):
        if self._euros>another._euros:
            return True
        if self._euros==another._euros:
            if self._cents>another._cents:
                return True
        return False
    
    def __lt__(self,another):
        if self._euros<another._euros:
            return True
        if self._euros==another._euros:
            if self._cents<another._cents:
                return True
        return False

    def __add__(self,another):
        s = self._euros+self._cents/100
        a = another._euros+another._cents/100
        n = s+a
        eu,ce = map(int,f"{n:.2f}".split("."))
        return Money(eu,ce)

    def __sub__(self,another):
        s = self._euros+self._cents/100
        a = another._euros+another._cents/100
        n = s-a
        if n<0:
            raise ValueError("a negative result is not allowed")
        eu,ce = map(int,f"{n:.2f}".split("."))
        return Money(eu,ce)



e1 = Money(4, 5)
e2 = Money(2, 95)

e3 = e1 + e2
e4 = e1 - e2

print(e3)
print(e4)


