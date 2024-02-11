import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 2.99e8  # Speed of light (m/s)
h = 6.626e-34  # Planck's constant (J*s)
k = 1.38e-23  # Boltzmann constant (J/K)
T_sun = 5778  # Temperature of the Sun (K)

# Wavelength range for a wider spectrum (in meters)
wavelength_range_full = np.linspace(1e-9, 3e-6, 1000)

# Planck's Law for black body radiation
black_body_radiance = (8 * np.pi * h * c) / (wavelength_range_full**5) * \
                      1 / (np.exp(h * c / (wavelength_range_full * k * T_sun)) - 1)

# Function to simulate absorption lines
def absorption_lines(wavelength, centers, depths, widths):
    absorption_spectrum = np.ones_like(wavelength)
    for center, depth, width in zip(centers, depths, widths):
        absorption_spectrum *= 1 - depth * np.exp(-((wavelength - center) / width)**2)
    return absorption_spectrum

# Function to simulate emission lines
def emission_lines(wavelength, centers, intensities, widths):
    emission_spectrum = np.zeros_like(wavelength)
    for center, intensity, width in zip(centers, intensities, widths):
        emission_spectrum += intensity * np.exp(-((wavelength - center) / width)**2)
    return emission_spectrum

# Function to simulate absorption and emission lines
def lines_spectrum(wavelength, centers_abs, depths_abs, widths_abs, centers_emission, intensities_emission, widths_emission):
    absorption_spectrum = np.ones_like(wavelength)
    emission_spectrum = np.zeros_like(wavelength)

    # Simulate absorption lines
    for center, depth, width in zip(centers_abs, depths_abs, widths_abs):
        absorption_spectrum *= 1 - depth * np.exp(-((wavelength - center) / width)**2)

    # Simulate emission lines
    for center, intensity, width in zip(centers_emission, intensities_emission, widths_emission):
        emission_spectrum += intensity * np.exp(-((wavelength - center) / width)**2)

    return absorption_spectrum, emission_spectrum

# Define absorption lines parameters
absorption_centers = [400e-9, 600e-9, 800e-9]  # Example wavelength centers for absorption
absorption_depths = [0.9, 0.2, 0.3]  # Example depths for absorption
absorption_widths = [50e-10, 100e-10, 150e-10]  # Example widths for absorption

# Define emission lines parameters
emission_centers = np.random.uniform(1e-6, 2e-6, 3)  # Example wavelength centers for emission (random)
emission_intensities = np.random.uniform(5.1, 1.5, 3)  # Example intensities for emission (random)
emission_widths = np.random.uniform(20e-10, 50e-10, 3)  # Example widths for emission (random)

# Add absorption and emission lines to the spectrum
absorption_spectrum, emission_spectrum = lines_spectrum(wavelength_range_full,
                                                       absorption_centers,
                                                       absorption_depths,
                                                       absorption_widths,
                                                       emission_centers,
                                                       emission_intensities,
                                                       emission_widths)

# Combine absorption and emission spectra
spectrum_with_lines = black_body_radiance * absorption_spectrum + emission_spectrum

# Normalize the radiance for better visualization
black_body_radiance /= np.max(black_body_radiance)
spectrum_with_lines /= np.max(spectrum_with_lines)

# Plotting
plt.figure(figsize=(10, 6))

# Plot regular black body spectrum
plt.plot(wavelength_range_full * 1e9, black_body_radiance, label='Regular Black Body Spectrum', linestyle='dashed')
plt.plot(wavelength_range_full * 1e9, spectrum_with_lines, label='With Absorption and Emission Lines', linestyle='solid')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Normalized Intensity')
plt.legend()

plt.tight_layout()

plt.show()

# Plot regular black body spectrum
plt.subplot(3, 1, 1)
plt.plot(wavelength_range_full * 1e9, black_body_radiance, label='Regular Black Body Spectrum', linestyle='dashed')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Normalized Intensity')
plt.title('Simulated Black Body Spectrum of the Sun')

# Plot spectrum with absorption lines
plt.subplot(3, 1, 2)
plt.plot(wavelength_range_full * 1e9, absorption_spectrum, label='With Absorption Lines', linestyle='solid')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Normalized Intensity')

# Plot spectrum with emission lines
plt.subplot(3, 1, 3)
plt.plot(wavelength_range_full * 1e9, emission_spectrum, label='With Emission Lines', linestyle='solid')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Normalized Intensity')

plt.tight_layout()

plt.show()
