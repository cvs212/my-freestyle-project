from Freestyle_App.baby_name_app import *

def test_read_name_boy():
    result = len(read_names_from_file(filename="babynames_boys.csv"))
    assert result == 200

def test_read_name_girl():
    result = len(read_names_from_file_girl(filename="babynames_girls.csv"))
    assert result == 200
