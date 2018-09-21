from pymatgen import Structure
from pymatgen.transformations.site_transformations import PartialRemoveSitesTransformation



estrutura = Structure.from_file("POSCAR")


remove = PartialRemoveSitesTransformation([range(0,63)], [1/63], algo=1)
print(type(remove))


result = remove.apply_transformation(estrutura, return_ranked_list=63)
print(type(remove))


for i, item in enumerate(result):
    item["structure"].to(filename="POSCAR{:02d}".format(i) ,tmp="POSCAR")

    






