import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0 , 2*np.pi , 100)
y = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x)*np.cos(x)
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.plot(x,y ,color = 'blue')
plt.title('sine wave')
plt.xlabel('X-axis')
plt.ylabel('y-axis')
