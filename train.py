import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from preprocessing_funcs import PrepData, ChatDataset
import numpy as np
from model import FeedForwardNet

filename = "training_intents_dataset.json"
data = PrepData(filename)
train_data = data.all_word_vectors
# print(train_data[0])
y_data = [i[1] for i in train_data]
X_train, y_train = np.array([i[0] for i in train_data]), np.array(y_data,dtype=np.float32)
# print(y_train)

#Hyperparameters
batch_size = 8
input_size = len(data.bag_of_words)
hidden_size = 8
n_classes = 13
learning_rate = 0.0011
num_epochs = 500
expected_final_loss = 0.0001

dataset = ChatDataset(X_train, y_train)
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True)
# print(train_loader.dataset.__dict__) 

def train(train_loader, input_size, hidden_size, n_classes, learning_rate):
	device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
	neural_net = FeedForwardNet(input_size, hidden_size, n_classes).to(device)

	optimizer = torch.optim.Adam(neural_net.parameters(), lr=learning_rate)
	criterion = nn.CrossEntropyLoss()

	for epoch in range(num_epochs):
		for (words, labels) in train_loader:
			# print(words, labels)
			words = words.to(device)
			labels = torch.tensor(labels,dtype=torch.long)
			labels = labels.to(device)
			# print(words)
			for idx, i in enumerate(words):
				outputs = neural_net(i)
			# print(labels)
				loss = criterion(outputs.view(1,outputs.size()[0]), labels[idx])

				optimizer.zero_grad()
				loss.backward()
				optimizer.step()
		if (epoch + 1)%50 == 0:
			print(f"epoch {epoch+1}/{num_epochs}, loss={loss.item():.10f}")
	# print(f"final loss={loss.item():.4f}")

	if loss.item() <= expected_final_loss:
		model_data = {
			"model_state": neural_net.state_dict(),
			"input_size": input_size,
			"hidden_size": hidden_size,
			"n_classes": n_classes,
			"bag_of_words": data.bag_of_words,
			"all_labels": data.all_labels
		} 
		FILE = "optimal_model_data\\model_data.pth"
		torch.save(model_data,FILE)
		print(f"TRAINING FINISHED: Optimal Data saved to {FILE}")
	print(f"TRAINING FINISHED: Loss was {loss.item()}")


if __name__ == "__main__":
	print("TRAINING")
	train(train_loader, input_size, hidden_size, n_classes, learning_rate)