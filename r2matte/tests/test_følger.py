from r2matte.følger import finn_eksplisit, finn_rekursiv

def test_finn_eksplisit():
    tallfølge = [1, 2, 3]
    
    funksjon = finn_eksplisit(tallfølge)

    assert True

def test_finn_rekursiv():
    assert finn_rekursiv()=="not implemented"