import pytest

from baia import Molecule


@pytest.mark.parametrize(
    "test_case, expected",
    [
        ("3-Methylheptane", "CCCCC(C)CC"),
        ("aspirin", "CC(=O)Oc1ccccc1C(O)=O"),
        ("Diethylsulfate", "CCO[S](=O)(=O)OCC"),
        ("Diethyl sulfate", "CCO[S](=O)(=O)OCC"),
        ("50-78-2", "CC(=O)Oc1ccccc1C(O)=O"),
    ]
)
def test_molecule_from_name_works_with_valid_names(test_case, expected):
    assert Molecule.from_name(test_case).smiles == expected


def test_molecule_from_name_does_not_work_with_invalid_names():
    with pytest.raises(AssertionError):
        Molecule.from_name("vibranium")
