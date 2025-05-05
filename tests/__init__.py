import importlib.metadata
import sys, os

import ics


def test_version_matches():
    dist = importlib.metadata.distribution("ics")
    print(dist.version, dist.__dict__, sys.path, ics.__path__)
    assert len(ics.__path__) == 1
    ics_path = ics.__path__[0]

    site_packages_folder = os.path.sep + "site-packages" + os.path.sep
    assert (
        site_packages_folder in ics_path and not "/src" in ics_path
    ), f"ics should be imported from package not from sources '{ics_path}' for testing"
    for path in sys.path:
        assert not path.endswith("/src"), (
            "Project sources should not be in PYTHONPATH when testing, conflicting entry: %s"
            % path
        )
    assert ics.__version__ == dist.version
