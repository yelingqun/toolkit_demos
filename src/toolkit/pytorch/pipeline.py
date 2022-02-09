import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class linear_module(nn.Module):
    '''Module of linear model'''
    def __init__(self):
        super(linear_module, self).__init__()
        self.a = nn.Parameter(torch.tensor(10.0))
        self.b = nn.Parameter(torch.tensor(20.0))
    
    def forward(self, x, y):
        return torch.abs(self.a * x  + self.b - y)

def get_data():
    '''Data'''
    return np.array([[1,2], [2,3], [4,5], [1.5, 2.3], [8,8]])

def create_module():
    '''Create cpu linear module'''
    device = "cpu"
    module = linear_module().to(device)
    return module

def create_optimizer(module):
    '''Create an optimizer'''
    return optim.SGD(module.parameters(), lr=1e-2)

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    points = get_data()
    module = create_module()
    optimizer = create_optimizer(module)

    #run the module
    for i in range (1000):
        for x, y in points:
            dis = module(x, y)
            cost = dis
            module.zero_grad()
            cost.backward()
            optimizer.step()
        if i%100 == 0:
            print("cost:", dis.data, ",a:", module.a.data, " ,b:", module.b.data)
            #display the result
            fig, ax = plt.subplots()
            ax.scatter(points[:,0], points[:, 1])
            x = np.array([0,10])
            y = module.a.data * x + module.b.data
            ax.plot(x, y)
            plt.show()
