import pytest
from subprefix.subpref import brutforce, fast

def test_brutforce():
    assert brutforce(["vegetable", "red", "redflag", "book", "notebook"]) == (4, ["book", "notebook"])

def test_brutforce_not_pref():
    assert brutforce(["vegetable", "red", "cat", "book", "log"]) == (0, [])

def test_brutforce_1word():
    assert brutforce(["vegetable"]) == (0, [])

def test_brutforce_null():
    assert brutforce([]) == (0, [])

@pytest.mark.parametrize("input, expected", [
    ([], (0, [])),
    (["red", "white", "violet", "violett"], (6, ["violett", "violet"])),
    (["tea"], (0, [])),
])
def test_fast(input, expected):
    assert fast(input) == expected

@pytest.fixture()
def fixture():
    print("fixture")

def test_fast_fixture(fixture):
    assert fast(["graf","pets", "grafica", "giraf"]) == (4, ["grafica", "graf"])

def test_fast_fixture_2same_word(fixture):
    assert fast(["graf", "graf", "pets", "ui"]) == (0, [])