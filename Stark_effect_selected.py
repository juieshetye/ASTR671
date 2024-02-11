import numpy as np
import matplotlib.pyplot as plt


def stark_effect(wavelength, electric_field_strength, sensitivity):
    # Placeholder function for simulating the Stark effect
    # Here, we'll just return some arbitrary values for demonstration
    # In a real simulation, you would use appropriate equations and models

    # Simulating more realistic behavior
    # Assuming the Stark shift is proportional to the electric field strength
    stark_shift = electric_field_strength * sensitivity  # Arbitrary scaling factor

    # Apply the Stark shift to the wavelength
    shifted_wavelength = wavelength + stark_shift

    return shifted_wavelength


# Wavelengths for Fe, Hα, and Ca spectral lines
wavelength_Fe = 6302  # in Å
wavelength_Halpha = 6563  # in Å
wavelength_Ca = 8542  # in Å

# Electric field strength
electric_field_strength = 1000  # in V/m

# Sensitivity factors for each spectral line
sensitivity_Fe = 1e-9  # Fe spectral line sensitivity
sensitivity_Halpha = 5e-10  # Hα spectral line sensitivity
sensitivity_Ca = 2e-9  # Ca spectral line sensitivity

# Calculate Stark effect for each spectral line
shifted_wavelengths_Fe = stark_effect(wavelength_Fe, electric_field_strength, sensitivity_Fe)
shifted_wavelengths_Halpha = stark_effect(wavelength_Halpha, electric_field_strength, sensitivity_Halpha)
shifted_wavelengths_Ca = stark_effect(wavelength_Ca, electric_field_strength, sensitivity_Ca)

# Plot
plt.figure(figsize=(10, 5))

# Plot for Fe
plt.plot(wavelength_Fe, shifted_wavelengths_Fe, 'o', label='Fe 6302 Å', color='blue')

# Plot for Hα
plt.plot(wavelength_Halpha, shifted_wavelengths_Halpha, 'o', label='Hα 6563 Å', color='green')

# Plot for Ca
plt.plot(wavelength_Ca, shifted_wavelengths_Ca, 'o', label='Ca 8542 Å', color='red')

plt.xlabel('Wavelength (Å)')
plt.ylabel('Shifted Wavelength (Å)')
plt.title('Stark Effect for Fe, Hα, and Ca Spectral Lines')
plt.legend()
plt.grid(True)
plt.show()
