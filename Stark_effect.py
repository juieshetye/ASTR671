import numpy as np
import matplotlib.pyplot as plt


def stark_effect(wavelength, electric_field_strength):
    # Placeholder function for simulating the Stark effect
    # Assuming a quadratic dependence on the electric field strength
    # Shift = a * E^2 + b * E
    # Coefficients a and b control the non-linear behavior

    a = 1e-15  # Coefficient for quadratic term
    b = 1e-5  # Coefficient for linear term

    stark_shift = a * electric_field_strength ** 2 + b * electric_field_strength

    # Apply the Stark shift to the wavelength
    shifted_wavelength = wavelength + stark_shift

    return shifted_wavelength


# Wavelength range including UV, visible, and IR
wavelength_range_uv = np.linspace(200, 400, 1000)  # UV range in nm
wavelength_range_vis = np.linspace(400, 700, 1000)  # Visible range in nm
wavelength_range_ir = np.linspace(700, 1000, 1000)  # IR range in nm

# Electric field strength
electric_field_strength = 1000  # in V/m

# Calculate Stark effect for each wavelength range
shifted_wavelengths_uv = stark_effect(wavelength_range_uv, electric_field_strength)
shifted_wavelengths_vis = stark_effect(wavelength_range_vis, electric_field_strength)
shifted_wavelengths_ir = stark_effect(wavelength_range_ir, electric_field_strength)

# Plot
plt.figure(figsize=(10, 5))

# UV range
plt.plot(wavelength_range_uv, shifted_wavelengths_uv, label='UV', color='blue')

# Visible range
plt.plot(wavelength_range_vis, shifted_wavelengths_vis, label='Visible', color='green')

# IR range
plt.plot(wavelength_range_ir, shifted_wavelengths_ir, label='IR', color='red')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Shifted Wavelength (nm)')
plt.title('Stark Effect with Non-linear Behavior')
plt.legend()
plt.grid(True)
plt.show()
