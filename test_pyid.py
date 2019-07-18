import pyid


def test_list():
    mylist = [[1, 2, 3] for i in range(5)]
    mylist = [pyid.idfy(item) for item in mylist]
    for item in mylist:
        assert item == [1, 2, 3]
        assert item.id


def test_dict():
    mylist = [{1: 2} for i in range(5)]
    mylist = [pyid.idfy(item) for item in mylist]
    for item in mylist:
        assert item == {1: 2}
        assert item.id


def test_int():
    mylist = [1 for i in range(5)]
    mylist = [pyid.idfy(item) for item in mylist]
    for item in mylist:
        assert item == 1
        assert item.id
