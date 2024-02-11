import matplotlib.pyplot as plt
import numpy as np

# Wavelength range in nanometers
wavelength_range = np.linspace(200, 2500, 1000)

# Solar spectrum intensity values (hypothetical values for demonstration)
solar_spectrum_intensity = np.exp(-0.0005 * (wavelength_range - 700) ** 2) + 0.5 * np.random.rand(1000)

# Plotting the solar spectrum
plt.plot(wavelength_range, solar_spectrum_intensity, label='Solar Spectrum')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.title('Solar Spectrum')
plt.legend()
plt.show()

############################ solar spectrum
#import numpy as np
#from astropy.modeling import models
#import astropy.units as u

#np.random.seed(42)
#g1 = models.Gaussian1D(1, 4.6, 0.2)
#g2 = models.Gaussian1D(2.5, 5.5, 0.1)
#g3 = models.Gaussian1D(-1.7, 8.2, 0.1)
#x = np.linspace(0, 10, 200)
#y = g1(x) + g2(x) + g3(x) + np.random.normal(0., 0.2, x.shape)
#spectrum = Spectrum1D(flux=y*u.Jy, spectral_axis=x*u.um)

#from matplotlib import pyplot as plt
#plt.plot(spectrum.spectral_axis, spectrum.flux)
#plt.xlabel('Spectral Axis ({})'.format(spectrum.spectral_axis.unit))
#plt.ylabel('Flux Axis({})'.format(spectrum.flux.unit))
#plt.grid(True)
################################### black body #################

#import numpy as np
#import matplotlib.pyplot as plt

temps = np.array([2000, 3500, 4500, 5778, 9940, 15000])
temps_cool=np.array([2.725,300])

# Set Constants
c = 2.99e8
h = 6.626e-34
k = 1.38e-23

def BlackBody(nu, T):
    B = (2 * h * nu**3 / c**2) * 1 / (np.exp(h * nu / (k * T)) - 1)
    return B

nuCMB = np.linspace(100, 6e11, num=500)
nuStar = np.linspace(100, 2e15, num=500)

# Plot CMB spectrum
figCMB, axCMB = plt.subplots()
#coolNames = ['CMB','FIRE']
axCMB.plot(nuCMB, BlackBody(nuCMB, temps_cool[0]), temps_cool[1], label='CMB,fire')
axCMB.set_title('Black Body Spectrum of the CMB')
axCMB.set_xlabel('Frequency [Hz]')
axCMB.set_ylabel('Spectral Radiance [W/sr/m$^2$/Hz]')
axCMB.legend()

# Plot star spectra
figStar, axStar = plt.subplots()
starNames = ['lightbulb','Betelgeuse', 'stove','Sun', 'Sirius','lightsaber']
for i in range(1, len(temps)):
    axStar.plot(nuStar, BlackBody(nuStar, temps[i]), label=starNames[i - 1])

axStar.set_title('Black Body Spectrum of Stars')
axStar.legend()
axStar.set_xlabel('Frequency [Hz]')
axStar.set_ylabel('Spectral Radiance [W/sr/m$^2$/Hz]')

plt.show()


