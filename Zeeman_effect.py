import numpy as np
import matplotlib.pyplot as plt


def zeeman_effect(wavelength, g_factor, B_field):
    # Constants
    mu_B = 9.274009994e-24  # Bohr magneton in J/T
    delta_lambda = (g_factor * mu_B * B_field) / wavelength

    return delta_lambda


# Wavelength range (including infrared and ultraviolet)
wavelength_range = np.linspace(200, 1000, 1000)  # in nm

# Define arbitrary Landé g values corresponding to each wavelength
# These are just placeholders; replace them with realistic values
g_values = {
    400: 1.5,  # Example g-value for 400 nm wavelength
    500: 2.0,  # Example g-value for 500 nm wavelength
    600: 1.8,  # Example g-value for 600 nm wavelength
    700: 2.2,  # Example g-value for 700 nm wavelength
    800: 1.6,  # Example g-value for 800 nm wavelength
    900: 2.5,  # Example g-value for 900 nm wavelength
    1000: 1.9  # Example g-value for 1000 nm wavelength
}

# Magnetic field strengths
B_fields = np.linspace(0, 2000, 11)  # in Gauss

# Calculate Zeeman effect for each magnetic field strength and wavelength
delta_lambdas = np.zeros((len(B_fields), len(wavelength_range)))
for i, B_field in enumerate(B_fields):
    for j, wavelength in enumerate(wavelength_range):
        g_factor = g_values.get(round(wavelength), 2.0)  # Use g-value from dictionary, default to 2.0 if not found
        delta_lambdas[ i, j ] = zeeman_effect(wavelength, g_factor, B_field)

# Plot Zeeman splitting for each magnetic field strength
plt.figure(figsize=(10, 5))
for i, B_field in enumerate(B_fields):
    plt.scatter(wavelength_range, delta_lambdas[ i ], label=f'B = {B_field} G', s=1)

# Add extra labels for UV, visible, and IR regions
plt.axvline(x=400, color='k', linestyle='--', linewidth=0.5)
plt.axvline(x=700, color='k', linestyle='--', linewidth=0.5)
plt.axvline(x=1000, color='k', linestyle='--', linewidth=0.5)

plt.xlabel('Wavelength (nm)')
plt.ylabel('Change in Wavelength (nm)')
plt.title('Zeeman Effect for Different Magnetic Field Strengths')
plt.legend()
plt.grid(True)

# Add extra x-axis labels
plt.xticks(ticks=[ 200, 400, 600, 700, 800, 1000 ], labels=[ 'UV', '400', '600', 'Visible', '800', 'IR' ])

plt.show()
