from flask import Flask, jsonify, request, render_template
import json
from preprocessing_funcs import PrepData
from model import FeedForwardNet
import torch
import random

#setting up AI model that has been trained
filename = "C:\\Users\\Luc10s\\Desktop\\Chatbot_Tensorflow\\chatbot\\training_data.json"
data_formatter = PrepData(filename, compile_attr=False)

model = torch.load("optimal_model_data\\model_data.pth")
# print(dir(model))
with open("training_intents_dataset.json","r") as datafile:
	intent_responses = json.load(datafile)
	responses = {}
	for i in intent_responses:
		responses[i["tag"]] = i["responses"]
input_size = model["input_size"]
hidden_size = model["hidden_size"]
n_classes = model["n_classes"]
bag_of_words = model["bag_of_words"]
labels = model["all_labels"]
model_state = model["model_state"]

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
neural_net = FeedForwardNet(input_size, hidden_size, n_classes).to(device)
neural_net.load_state_dict(model_state)
neural_net.eval()

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello():
    # POST request
	if request.method == 'POST':
		print('Incoming..')
		sentence = request.get_json(force=True)["text"]
		print("RECEIVED")  # parse as JSON
		words = data_formatter.lemmatizer(sentence)
		word_vector = data_formatter.vector(words,bag_of_words=bag_of_words, all_labels=labels)
		word_vector = torch.tensor(word_vector)
		output = neural_net(word_vector)
		_, predicted = torch.max(output.view(1,output.size()[0]),dim=1)
		tag = labels[predicted.item()]
		probs = torch.softmax(output.view(1,output.size()[0]),dim=1)
		prob = probs[0] 
		if prob[predicted.item()] >= 0.5:
			# print(tag,'\n',prob,'\n',prob[predicted.item()])
			if tag == "make_account":
				return jsonify({"ai":responses[tag][random.randint(0,len(responses[tag])-1)],"action":"make account"})
			else:
				return jsonify({"ai":responses[tag][random.randint(0,len(responses[tag])-1)],"action":""})
		else:
			# print("Sorry, I cant make sense of that")
			return jsonify({"ai":"Sorry, I cant make sense of that"})
    # GET request
	else:
		message = {'ai':"Only POST requests"}
		return jsonify(message)  # serialize and use JSON headers

@app.route('/test')
def test_page():
    # look inside `templates` and serve `index.html`
    return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)