import cantera as ct
import numpy as np
import matplotlib.pyplot as plt


gas = ct.Solution('gri30.yaml')


def calculate_burned_mixture(equivalence_ratio, gas):
   
    fuel = 'H2'
    oxidizer = 'O2:1.0, N2:3.76'  

  
    gas.set_equivalence_ratio(equivalence_ratio, fuel, oxidizer)
    
  
    gas.TP = 300, ct.one_atm  
    

    gas.equilibrate('HP')  
    
    
    burned_temperature = gas.T
    burned_composition = gas.X
    
    return burned_temperature, burned_composition


equivalence_ratios = np.linspace(0.5, 2.0, 50)


temperatures = []
h2o_mole_fractions = []
h2_mole_fractions = []
oh_mole_fractions = []
o2_mole_fractions = []
no_mole_fractions = []


for phi in equivalence_ratios:
    temperature, composition = calculate_burned_mixture(phi, gas)
    temperatures.append(temperature)
    h2o_mole_fractions.append(composition[gas.species_index('H2O')])
    h2_mole_fractions.append(composition[gas.species_index('H2')])
    oh_mole_fractions.append(composition[gas.species_index('OH')])
    o2_mole_fractions.append(composition[gas.species_index('O2')])
    no_mole_fractions.append(composition[gas.species_index('NO')])
    
    print(f'Equivalence Ratio: {phi:.2f}')
    print(f'Burned Gas Temperature: {temperature:.2f} K')
    print('Burned Gas Composition:')
    for species, mole_fraction in zip(gas.species_names, composition):
        if mole_fraction > 1e-6:  
            print(f'  {species}: {mole_fraction:.3e}')
    print()


plt.figure(figsize=(8, 6))
plt.plot(equivalence_ratios, temperatures, marker='')
plt.xlabel('Equivalence Ratio')
plt.ylabel('Burned Gas Temperature (K)')
plt.title('Burned Gas Temperature vs. Equivalence Ratio')
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 6))
plt.plot(equivalence_ratios, h2o_mole_fractions, marker='', label='H2O')
plt.plot(equivalence_ratios, h2_mole_fractions, marker='', label='H2')
plt.plot(equivalence_ratios, o2_mole_fractions, marker='', label='O2')
plt.xlabel('Equivalence Ratio')
plt.ylabel('Mole Fraction')
plt.title('Mole Fractions vs. Equivalence Ratio')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(equivalence_ratios, oh_mole_fractions, marker='', label='OH')
plt.plot(equivalence_ratios, no_mole_fractions, marker='', label='NO')
plt.xlabel('Equivalence Ratio')
plt.ylabel('Mole Fraction')
plt.title('Mole Fractions vs. Equivalence Ratio')
plt.legend()
plt.grid(True)
plt.show()