import spacy
import numpy as np
import json
from torch.utils.data import Dataset

class PrepData:
	puncts = ",./;'[]}{<>?:\"\\|+_)(*&^%$#@!~`-="
	nlp = spacy.load("en_core_web_sm")
	def __init__(self, filename, compile_attr=True):
		if compile_attr:
			with open(filename,"r") as file:
				self.datafile = json.load(file)
			self.bag_of_words = self.make_bag_of_words()
			self.all_labels = sorted([i['tag'] for i in self.datafile])
			self.all_word_vectors = self.sentence_vectors() 

	def lemmatizer(self, sentence):
		return [token.lemma_ for token in self.nlp(sentence) if token.text not in self.puncts]

	def vector(self, tokenized_sentence, bag_of_words, all_labels, label=None):
		res = np.zeros(len(bag_of_words), dtype=np.float32)
		for index, word in enumerate(bag_of_words):
			if word in tokenized_sentence:  
				res[index] = 1.0
		if label:
			tag = [all_labels.index(label)]
			# tag_[tag] = 1
			return res, tag
		else:
			return res

	def make_bag_of_words(self):
		print("[BAG OF WORDS] Starting creation")
		bag = []
		for i in self.datafile:
			for sentence in i["statements"]:
				bag.extend(self.lemmatizer(sentence))
		print("[BAG OF WORDS] Finished creation")
		return sorted(set(bag))

	def sentence_vectors(self):
		print("[ALL WORD VECTORS] Starting creation")
		all_vectors = []
		for i in self.datafile:
			for sentence in i["statements"]:
				all_vectors.append(self.vector(tokenized_sentence=self.lemmatizer(sentence),label=i['tag'],
					bag_of_words=self.bag_of_words,all_labels=self.all_labels))
		print("[ALL WORD VECTORS] Finished creation")
		return all_vectors

class ChatDataset(Dataset):
	def __init__(self, X_train, y_train):
		self.n_samples = len(X_train)
		self.x_data = X_train
		self.y_data = y_train

	def __getitem__(self,index):
		return self.x_data[index], self.y_data[index]

	def __len__(self):
		return self.n_samples	