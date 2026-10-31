import cim_python_sdk


def test_version():
    assert isinstance(cim_python_sdk.__version__, str)
