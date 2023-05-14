import bpy
import torch
import torchvision
from torchvision import transforms
from PIL import Image
from os import listdir
import random
import torch.optim as optim
from torch.autograd import Variable
import torch.nn.functional as F
import torch.nn as nn

# here normalizing data in order to average out differences
normalize = transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225]
)
# here we crop them in order to get a collective Image_format
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(256),
    transforms.ToTensor(),
    normalize
])

train_data_list = []
train_data = []
target_list = []
files = listdir(r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\BuildingsDataset/")

# TARGET: [ishighrise, isdutch_house, isglassfront]
# creating the train_data and target list
for i in range(len(listdir(r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\BuildingsDataset/"))):
    # l = len(files)
    # r = random.randint(0, l)
    f = random.choice(files)
    files.remove(f)
    img = Image.open(r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\BuildingsDataset/"+f)
    img_tensor = transform(img)
    img_tensor.unsqueeze_(0)
    train_data_list.append(img_tensor)
    ishighrise = 1 if "highrise" in f else 0
    isdutch_house = 1 if "dutch_house" in f else 0
    isglassfront  = 1 if "glassfront" in f else 0

    target = [ishighrise, isdutch_house, isglassfront]
    target_list.append(target)
    if len(train_data_list) >= 64:
        train_data.append((torch.stack(train_data_list), target_list))
        train_data_list = []
        print('Loaded batch ', len(train_data), 'of ', int(len(listdir(r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\BuildingsDataset/")) / 64))
        print('Percentage Done: ', 100 * len(train_data) / int(len(listdir(r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\BuildingsDataset/")) / 64), '%')
        if len(train_data) > 150:
            break

 # defining the net and forward pass, a conv. neural network has been choosen in order to properly work with image data
class Netz(nn.Module):
    def __init__(self):
        super(Netz, self).__init__()
        self.conv1 = nn.Conv2d(3, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(6, 12, kernel_size=5)
        self.conv3 = nn.Conv2d(12, 18, kernel_size=5)
        self.fcs1 = nn.Linear(14112, 1000)
        self.fcs2 = nn.Linear(1000, 2)

    def forward(self, x):
        x = self.conv1(x)
        x = F.max_pool2d(x, 2)
        x = F.relu(x)
        x = self.conv1(x)
        x = F.max_pool2d(x, 2)
        x = F.relu(x)
        x = x.view(-1, 14112)
        x = F.relu(self.fcs1(x))
        x = self.fcs1(x)

        return F.log_softmax(x)
        print(x.size())
        exit()

model = Netz()


optimizer = optim.Adam(model.parameters(), lr = 0.01)
def train(epoch):
    model.train()
    counter = 0
    for data, target in train_data:
        target = torch.Tensor(target)
        data = Variable(data)
        target = Variable(target)
        optimizer.zero_grad()
        out = model(data)
        loss = F.nll_loss(out, target)
        loss.backward()
        optimizer.step()
        counter = counter + 1
        

def test():
    model.eval()
    files = listdir(r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\test_set/")
    f = random.choice(files)
    img = Image.open(r"C:\Users\Have Fun\PycharmProjects\python\pythonImage_datasets\test_set/" + f)
    img_eval_tensor = transforms(img)
    img_eval_tensor.unsqueeze_(0)
    out = model(data)
    print(out.data.max(1, keepdim=True)[1])
    img.show()
    x = input('')
    
