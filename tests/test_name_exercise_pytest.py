from exercises.name_exercise import vowel

def test_vowel():
    assert vowel("james") == "ames"
    assert vowel("emma") == "emma"
    assert vowel("chetna") == "etna"
    assert vowel("yolanda") == "olanda"
    assert vowel("byron") == "yron"
    assert vowel("yvette") == "yvette"
    assert vowel("") == "noname"