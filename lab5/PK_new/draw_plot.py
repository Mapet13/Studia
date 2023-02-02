import matplotlib.pyplot as plt
import numpy as np


labels = ['Standard', 'Equal', 'Simple']
locks_means = [3521264.0, 3077314.6, 1676226.4]
cond4_means = [1324589.4, 1115061.8, 1660504.6]

x = np.arange(len(labels))  
width = 0.35 

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, locks_means, width, label='Locks')
rects2 = ax.bar(x + width/2, cond4_means, width, label='4 Conditions')

ax.set_title('Locks vs 4 Conditions')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3, fmt = '%.1f')
ax.bar_label(rects2, padding=3, fmt = '%.1f')

fig.tight_layout()

plt.ticklabel_format(style='plain', axis='y')
plt.show()