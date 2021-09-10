import numpy as np
import matplotlib.pyplot as plt

org = np.load('input/phase.npy')
unw = np.load('output/unwrapped_phase.npy')


plt.figure(), plt.imshow(org, cmap='jet'), plt.colorbar(), plt.title('Wrapped-Phase')
plt.savefig('wrapped_phase_from_demo.png', dpi=600)

plt.figure(), plt.imshow(unw, cmap='jet'), plt.colorbar(), plt.title('Unwrapped-Phase')
plt.savefig('unwrapped_phase_from_demo.png', dpi=600)

