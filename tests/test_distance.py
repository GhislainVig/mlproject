from mlproject.distance import haversine

def test_type_of_haversine():
    assert type(haversine(48.865, 2.380, 48.235, 2.393)) == float

def test_result_of_haversine():
    assert haversine(48.865, 2.380, 48.235, 2.393) == 70.00696965697475
