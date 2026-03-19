import psi4

# Molecule
h2o = psi4.geometry("""
O
H 1 0.96
H 1 0.96 2 104.5
""")

# Options
psi4.set_options({'basis': 'sto-3g'})

# Energy calculation
energy = psi4.energy('scf')
print("Hartree-Fock energy:", energy)

