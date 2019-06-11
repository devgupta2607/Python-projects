import numpy as np

import matplotlib.pyplot as plot

 

# Get x values of the sine wave

x_values       = np.arange(-10, 10, 0.1);

 

# Amplitude of the sine wave is sine of a variable like time

y_values  = 2*(np.sin(x_values*(np.pi/4)))

 

# Plot a sine wave using time and amplitude obtained for the sine wave

plot.plot(x_values, y_values)

 

# Give a title for the sine wave plot

plot.title('Sine wave')

 

# Give x axis label for the sine wave plot

plot.xlabel('x')

 

# Give y axis label for the sine wave plot

plot.ylabel('y = 2sin(x*pi/4)')

 

plot.grid(True, which='both')

 

plot.axhline(y=0, color='k')

 

plot.show()

 

# Display the sine wave

plot.show()
