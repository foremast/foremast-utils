import pytest
from gogoutils.formats import Formats

FORMATS = {
    'domain': 'example.com',
}


def test_formats_defaults():
    """Test defaults."""
    config = Formats().get_formats()
    assert config.get('app') == '{repo}{project}'
    assert config.get('iam_base') == '{project}_{repo}'
    assert config.get('git_repo') == '{raw_project}/{raw_repo}'


def test_formats_params():
    """Test params sent."""

    config = Formats(FORMATS).get_formats()
    assert config.get('domain') == 'example.com'
