import requests
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem, Draw


class Molecule:

    def __init__(self, smiles: str, name: str = None):
        self.smiles = smiles
        self.name = name
        self.rdkit_molecule = Chem.MolFromSmiles(self.smiles)

    @classmethod
    def from_name(cls, name: str):
        url = f"http://cactus.nci.nih.gov/chemical/structure/{name}/smiles"
        try:
            response = requests.get(url, timeout=2)
            assert response.status_code == 200
            return Molecule(smiles=response.content.decode(), name=name)
        except requests.exceptions.Timeout:
            raise
        except AssertionError:
            #TODO: use different alternatives if not found
            #https://stackoverflow.com/questions/54930121/converting-molecule-name-to-smiles
            raise

    @classmethod
    def from_smiles(cls, smiles: str):
        return Molecule(smiles=smiles)

    @classmethod
    def from_image(cls, path: str):
        raise NotImplementedError

    def draw2d(self, as_numpy: bool = False):
        #template = Chem.MolFromSmiles(self.smiles)
        AllChem.Compute2DCoords(self.rdkit_molecule)
        img = Draw.MolToImage(self.rdkit_molecule)
        if as_numpy:
            return np.array(img)
        return img

    def draw3d(self):
        pass