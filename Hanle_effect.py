import numpy as np
import matplotlib.pyplot as plt


def hanle_effect(wavelength, magnetic_field_strength):
    # Placeholder function for simulating the Hanle effect
    # Here, we'll just return some arbitrary values for demonstration
    # In a real simulation, you would use appropriate equations and models

    # Simulating more realistic behavior with negative polarization
    # Assuming polarization degree varies sinusoidally with wavelength and magnetic field strength
    polarization_degree = np.sin(wavelength / 1000 * np.pi) * np.cos(magnetic_field_strength / 1000 * np.pi)

    return polarization_degree


# Wavelength range (including UV, visible, and IR)
wavelength_range = np.linspace(200, 1000, 1000)  # in nm

# Magnetic field strengths
magnetic_field_strengths = np.linspace(0, 2000, 11)  # in Gauss

# Calculate Hanle effect for each magnetic field strength and wavelength
hanle_data = np.zeros((len(magnetic_field_strengths), len(wavelength_range)))
for i, B_field in enumerate(magnetic_field_strengths):
    for j, wavelength in enumerate(wavelength_range):
        hanle_data[ i, j ] = hanle_effect(wavelength, B_field)

# Plot Hanle effect for each magnetic field strength
plt.figure(figsize=(10, 5))
for i, B_field in enumerate(magnetic_field_strengths):
    plt.plot(wavelength_range, hanle_data[ i ], label=f'B = {B_field} G')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Polarization Degree')
plt.title('Hanle Effect for Different Magnetic Field Strengths')
plt.legend()
plt.grid(True)
plt.show()
