import numpy as np
import matplotlib.pyplot as plt


def zeeman_effect(wavelength, g_factor, B_field):
    # Constants
    mu_B = 9.274009994e-24  # Bohr magneton in J/T
    delta_lambda = (g_factor * mu_B * B_field) / wavelength

    return delta_lambda


# Define spectral lines for Fe 6302, Ca 8542, and Halpha
Fe_6302 = {'wavelength': 630.25, 'g_factor': 1.5}  # nm
Ca_8542 = {'wavelength': 854.2, 'g_factor': 2.0}  # nm
H_alpha = {'wavelength': 656.3, 'g_factor': 1.0}  # nm

# Wavelength range
wavelength_range = np.linspace(600, 900, 1000)  # in nm

# Magnetic field strengths
B_fields = np.linspace(0, 2000, 11)  # in Gauss

# Calculate Zeeman effect for each magnetic field strength for Fe 6302
delta_lambdas_Fe = [ zeeman_effect(Fe_6302[ 'wavelength' ], Fe_6302[ 'g_factor' ], B_field) for B_field in B_fields ]

# Calculate Zeeman effect for each magnetic field strength for Ca 8542
delta_lambdas_Ca = [ zeeman_effect(Ca_8542[ 'wavelength' ], Ca_8542[ 'g_factor' ], B_field) for B_field in B_fields ]

# Calculate Zeeman effect for each magnetic field strength for Halpha
delta_lambdas_Halpha = [ zeeman_effect(H_alpha[ 'wavelength' ], H_alpha[ 'g_factor' ], B_field) for B_field in
                         B_fields ]

# Plot Zeeman splitting for each magnetic field strength for Fe 6302
plt.figure(figsize=(10, 5))
sc1 = plt.scatter(Fe_6302[ 'wavelength' ] * np.ones_like(B_fields), delta_lambdas_Fe, c=B_fields, cmap='Blues',
                  label='Fe 6302', s=30)
sc2 = plt.scatter(Ca_8542[ 'wavelength' ] * np.ones_like(B_fields), delta_lambdas_Ca, c=B_fields, cmap='Reds',
                  label='Ca 8542', s=30)
sc3 = plt.scatter(H_alpha[ 'wavelength' ] * np.ones_like(B_fields), delta_lambdas_Halpha, c=B_fields, cmap='Greens',
                  label='Halpha', s=30)

plt.xlabel('Wavelength (nm)')
plt.ylabel('Change in Wavelength (nm)')
plt.title('Zeeman Effect for Fe 6302, Ca 8542, and Halpha Lines')
plt.colorbar(label='Magnetic Field (Gauss)')
plt.legend()
plt.grid(True)
plt.show()
