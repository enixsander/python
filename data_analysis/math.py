import scipy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

N = 64
Fs = 10
Fd = 512
Tm = N/Fd
# t = np.arange(0, Tm, 1/Fd)
t = np.linspace(0.0, 1/Fd, N, endpoint=False)
fi_1 = 0

inph = np.cos(2*np.pi*Fs*t + fi_1)
quadr = np.sin(2*np.pi*Fs*t + fi_1)

# plt.plot(t, inph, t, quadr, marker='o')

mu, sigma = 0, 1  # mean and standard deviation
white_noise = np.random.normal(mu, sigma, size=1000)  # 1000 samples with normal distribution
# seaborn histogram with Kernel Density Estimation
sns.displot(white_noise, bins=40, kde=True)


