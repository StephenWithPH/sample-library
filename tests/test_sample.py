from sample_library import sample

def test_read():
    result = sample.read()
    assert result.foo == 42
    assert round(result.bar, 2) == 3.14
    assert result.baz is True
