import torch
import torch.nn as nn
#model architecture simple feeddforward network
class FeedForwardNet(nn.Module):
	def __init__(self, input_size, hidden_size, n_classes):

		super(FeedForwardNet, self).__init__()

		self.input = nn.Linear(input_size, hidden_size)
		self.h1 = nn.Linear(hidden_size, hidden_size)
		self.h2 = nn.Linear(hidden_size, hidden_size)
		self.output = nn.Linear(hidden_size, n_classes)
		self.relu = nn.ReLU()

	def forward(self, x):

		out = self.relu(self.input(x))
		out = self.relu(self.h1(out))
		out = self.relu(self.h2(out))
		out = self.output(out)

		return out