class filme:
    def __init__(self, nome, genero, ano):
        self.nome = nome
        self.genero = genero
        self.ano = ano

    def __str__(self):
        return f"{self.nome} ({self.ano}) - {self.genero}"
    def __repr__(self):
        return f"{self.nome} ({self.ano}) - {self.genero}"
    def __eq__(self, other):
        if isinstance(other, filme):
            return self.nome == other.nome and self.genero == other.genero and self.ano == other.ano
        return False
    def __lt__(self, other):
        if isinstance(other, filme):
            return self.nome < other.nome
        return False
    def __le__(self, other):
        if isinstance(other, filme):
            return self.nome <= other.nome
        return False
    def __gt__(self, other):
        if isinstance(other, filme):
            return self.nome > other.nome
        return False
    def __ge__(self, other):
        if isinstance(other, filme):
            return self.nome >= other.nome
        return False
    def __ne__(self, other):
        if isinstance(other, filme):
            return self.nome != other.nome or self.genero != other.genero or self.ano != other.ano
        return False
    def __hash__(self):
        return hash((self.nome, self.genero, self.ano))
    def __len__(self):
        return len(self.nome)
    def __contains__(self, item):
        if isinstance(item, str):
            return item in self.nome
        return False

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.nome[item]
        elif isinstance(item, slice):
            return self.nome[item]
        else:
            raise TypeError("Invalid argument type")
    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.nome[key] = value
        elif isinstance(key, slice):
            self.nome[key] = value
        else:
            raise TypeError("Invalid argument type")

    def __delitem__(self, key):
        if isinstance(key, int):
            del self.nome[key]
        elif isinstance(key, slice):
            del self.nome[key]
        else:
            raise TypeError("Invalid argument type")
    def __iter__(self):
        return iter(self.nome)
    def __next__(self):
        return next(self.nome)
    def __reversed__(self):
        return reversed(self.nome)
    def __add__(self, other):


        if isinstance(other, filme):
            return filme(self.nome + other.nome, self.genero + other.genero, self.ano + other.ano)
        return NotImplemented
    def __sub__(self, other):
        if isinstance(other, filme):
            return filme(self.nome - other.nome, self.genero - other.genero, self.ano - other.ano)
        return NotImplemented
    def __mul__(self, other):
        if isinstance(other, filme):
            return filme(self.nome * other.nome, self.genero * other.genero, self.ano * other.ano)
        return NotImplemented
    def __truediv__(self, other):
        if isinstance(other, filme):
            return filme(self.nome / other.nome, self.genero / other.genero, self.ano / other.ano)
        return NotImplemented
    def __floordiv__(self, other):
        if isinstance(other, filme):
            return filme(self.nome // other.nome, self.genero // other.genero, self.ano // other.ano)
        return NotImplemented
    def __mod__(self, other):
        if isinstance(other, filme):
            return filme(self.nome % other.nome, self.genero % other.genero, self.ano % other.ano)
        return NotImplemented
    def __pow__(self, other):
        if isinstance(other, filme):
            return filme(self.nome ** other.nome, self.genero ** other.genero, self.ano ** other.ano)
        return NotImplemented
    def __and__(self, other):
        if isinstance(other, filme):
            return filme(self.nome & other.nome, self.genero & other.genero, self.ano & other.ano)
        return NotImplemented
    def __or__(self, other):
        if isinstance(other, filme):
            return filme(self.nome | other.nome, self.genero | other.genero, self.ano | other.ano)
        return NotImplemented
    def __xor__(self, other):
        if isinstance(other, filme):
            return filme(self.nome ^ other.nome, self.genero ^ other.genero, self.ano ^ other.ano)
        return NotImplemented
    def __invert__(self):
        return filme(~self.nome, ~self.genero, ~self.ano)
    def __call__(self, *args, **kwargs):
        return filme(self.nome(*args, **kwargs), self.genero(*args, **kwargs), self.ano(*args, **kwargs))
    def __str__(self):
        return f"{self.nome} ({self.ano}) - {self.genero}"       
    def __repr__(self):
        return f"{self.nome} ({self.ano}) - {self.genero}"
    def __format__(self, format_spec):
        return f"{self.nome:{format_spec}} ({self.ano}) - {self.genero}"
    def __sizeof__(self):
        return len(self.nome) + len(self.genero) + len(str(self.ano))
    def __del__(self):
        del self.nome
        del self.genero
        del self.ano
    def __copy__(self):
        return filme(self.nome, self.genero, self.ano)
    def __deepcopy__(self, memo):
        return filme(self.nome, self.genero, self.ano)
    def __reduce__(self):
        return (filme, (self.nome, self.genero, self.ano))
    def __reduce_ex__(self, protocol):
        return (filme, (self.nome, self.genero, self.ano))
    def __getstate__(self):
        