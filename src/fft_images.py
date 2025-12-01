import matplotlib.pyplot as plt
import numpy as np

import two_dim_fft

image_to_freq = two_dim_fft.image_to_freq
freq_to_image = two_dim_fft.freq_to_image

test_uniform_image = np.ones((257, 257), dtype=np.float64)
spectrum = image_to_freq(test_uniform_image)
plt.imshow(test_uniform_image, cmap="gray")
plt.title("Uniform Image")
plt.show()

plt.imshow(np.log(np.abs(spectrum) + 1), cmap="gray")
plt.title("Frequency Spectrum of Uniform Image")
plt.show()
