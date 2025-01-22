d1 = {}
d1["a"] = 1
d1["b"] = 2

assert d1["a"] == 1
assert d1 == {"a": 1, "b": 2}

# Cancello la chiave "b"
del d1["b"]

# Controllo che il dict non contenga ancora la chiave "b"
assert "b" not in d1

# Potrei anche controllarlo in questo modo
# e verificare anche la presenza di "a"
if "b" not in d1 and "a" in d1:
    assert True
else:
    assert False
