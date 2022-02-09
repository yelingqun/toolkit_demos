import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda, Compose


def load_data():
    '''Load data from FashionMNIST'''
    data = datasets.FashionMNIST(
        root="data",
        train=True,
        download=True,
        transform=ToTensor(),
    )
    return data

def first_item(data):
    '''Get first item from data and reshape it to 28X28'''
    X = data.__getitem__(0)[0]
    Y = X.reshape([28,28])
    return Y


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    data = load_data()
    pic1 = first_item(data)

    plt.gray()
    plt.imshow(pic1)
    plt.show()