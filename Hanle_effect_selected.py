import numpy as np
import matplotlib.pyplot as plt


def hanle_effect(wavelength, magnetic_field_strength, sensitivity):
    # Placeholder function for simulating the Hanle effect
    # Here, we'll just return some arbitrary values for demonstration
    # In a real simulation, you would use appropriate equations and models

    # Simulating more realistic behavior
    # Assuming polarization degree decreases with increasing wavelength and magnetic field strength
    polarization_degree = np.exp(-wavelength / 1000) * np.exp(-magnetic_field_strength / sensitivity / 1000)

    return polarization_degree


# Wavelength range for the spectral lines (6302 Å, 6563 Å, 8542 Å)
wavelength_6302 = 6302  # in Å
wavelength_6563 = 6563  # in Å
wavelength_8542 = 8542  # in Å

# Magnetic field strengths
magnetic_field_strengths = np.linspace(0, 2000, 11)  # in Gauss

# Sensitivity factors for each spectral line
sensitivity_6302 = 1  # Fe I 6302 Å is the most sensitive
sensitivity_6563 = 0.7  # Hα 6563 Å is less sensitive than Fe I 6302 Å
sensitivity_8542 = 1.5  # Ca II 8542 Å is more sensitive than Hα 6563 Å

# Calculate Hanle effect for each spectral line and magnetic field strength
hanle_data_6302 = [ hanle_effect(wavelength_6302, B_field, sensitivity_6302) for B_field in magnetic_field_strengths ]
hanle_data_6563 = [ hanle_effect(wavelength_6563, B_field, sensitivity_6563) for B_field in magnetic_field_strengths ]
hanle_data_8542 = [ hanle_effect(wavelength_8542, B_field, sensitivity_8542) for B_field in magnetic_field_strengths ]

# Plot Hanle effect for each spectral line
plt.figure(figsize=(10, 5))

# Plot for 6302 Å
plt.plot(magnetic_field_strengths, hanle_data_6302, label='Fe I 6302 Å')

# Plot for 6563 Å
plt.plot(magnetic_field_strengths, hanle_data_6563, label='Hα 6563 Å')

# Plot for 8542 Å
plt.plot(magnetic_field_strengths, hanle_data_8542, label='Ca II 8542 Å')

plt.xlabel('Magnetic Field Strength (Gauss)')
plt.ylabel('Polarization Degree')
plt.title('Hanle Effect for Spectral Lines')
plt.legend()
plt.grid(True)
plt.show()
