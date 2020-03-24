class Node():

    def __init__(self, value=None):
        self.val = value
        self.next = None

    def dodaj_z_przodu(self,arg):
        new_el = Node(arg)
        new_el.next = self.next
        self.next = new_el

    def dadaj_z_tylu(self,arg):
        new_el = Node(arg)
        tmp = self
        while tmp.next is not None :
            tmp = tmp.next
        tmp.next = new_el

    def wypisz(self):
        tmp = self
        while tmp is not None :
            print(tmp.val)
            tmp=tmp.next

    def babelkowe(self):
        head = self   
        flaga = None  
        while flaga is not head.next :
            head = self 
            prev = self
            ob = self
            nast = head.next
            while nast.next is not flaga :
                prev = ob
                ob = nast
                nast = nast.next
                if ob.val > nast.val :
                    prev.next = nast
                    ob.next = nast.next
                    nast.next = ob
                    ob = nast
                    nast = nast.next
            flaga = nast

if __name__ == '__main__':
    kamil = Node()
    kamil.dodaj_z_przodu(4)   #w ten sposób dodajemy elementy do łańcucha można dopracować ale nie o to chodzi
    kamil.dodaj_z_przodu(2)
    kamil.dodaj_z_przodu(4)
    kamil.dodaj_z_przodu(7)
    kamil.dodaj_z_przodu(1)
    kamil.dodaj_z_przodu(33)
    kamil.dadaj_z_tylu(6)
    kamil.wypisz()             #przed sortowaniem
    kamil.babelkowe()
    kamil.wypisz()             # po sortowaniu