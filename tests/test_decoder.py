#
# These tests are taken from decoder_test.go
#

from __future__ import print_function

from os.path import join, dirname
import hcl
import json

import pytest

# hcl, json, dict
FIXTURE_DIR = join(dirname(__file__), 'fixtures')
FIXTURES = [
    ('issue12.hcl', 'issue12.json', None),
]


@pytest.mark.parametrize("hcl_fname,json_fname,struct", FIXTURES)
def test_decoder(hcl_fname, json_fname, struct):
    with open(join(FIXTURE_DIR, hcl_fname), 'r') as fp:
        hcl_json = hcl.load(fp)

    assert json_fname is not None or struct is not None

    if json_fname is not None:
        with open(join(FIXTURE_DIR, json_fname), 'r') as fp:
            good_json = json.load(fp)

        with open(FIXTURE_DIR + "/"+hcl_fname+"_test.json", 'w') as fp:
            json.dump(hcl_json, fp, indent=4)

        assert hcl_json == good_json

    if struct is not None:
        assert hcl_json == struct
