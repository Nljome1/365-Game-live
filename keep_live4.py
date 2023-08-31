import torch
import torch.nn as nn

# 定义一个简单的卷积神经网络
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()
        self.maxpool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc = nn.Linear(16 * 14 * 14, 10)  # 输入图像大小为28x28，经过卷积和池化后变为14x14

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.maxpool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

# 创建一个随机输入图像（3x28x28）
input_image = torch.randn(1, 3, 28, 28)

# 初始化神经网络
model = SimpleCNN()

# 对输入图像进行分类预测
output = model(input_image)
print(output.size())  # 输出大小为(1, 10)，表示10个类别的得分
