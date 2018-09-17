# import numpy as np
import pandas as pd

data_list = [[-0.4209509421981435, 0.8071645740343169, 0.8024297226075767, 1.075427029340095],
             [-1.1558437026900632, 0.22398337153660722, 0.7744098509275676, 1.1909264260675636],
             [-0.6141475317571331, -1.554080855238347, -0.3112621386026188, -0.5262859503312299],
             [0.3911896392001301, -1.9429374656920229, 0.7015908672138063, 0.915084969114771],
             [-0.14291622550466518, -0.8508378018024315, 0.8919302757239321, 0.6335576291982921],
             [3.402552092447471, -0.7280813840146305, -0.7804882386460715, 0.038980875798346595]]

# df = pd.DataFrame(np.random.randn(6, 4), index=list('abcdef'), columns=list('ABCD'))
df = pd.DataFrame(data_list, index=list('abcdef'), columns=list('ABCD'))
print(df)

print(df[df.A == 0.365102])
# print(df.values.tolist())
