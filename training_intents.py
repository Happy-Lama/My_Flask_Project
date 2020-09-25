import json

data = []

greetings_phrases = ["Hello","Hi","How are you","Good morning","Good afternoon","Good evening","Hi there",
					"How are you","what's up","Hey", "Hey there","How's everything going","Howdy","good day","greetings"]
greetings_responses = ["Good day to you. How may I help you?","Hello. Can I assist you in any way?","Hi I'm a bot and I can help you with some simple tasks",
						"Hey there, what's up?"]
data.append({"tag":"greetings","statements":greetings_phrases,"responses":greetings_responses})

thanks_phrases = ["Thank you","Thanks alot","I'm very grateful for your help","Thanks for the help"]
thanks_responses = ["You're welcome","Glad I could be of assistance","Glad I could help","I'm here to assist you. I was born for this"]

data.append({"tag":"thank_you","statements":thanks_phrases,"responses":thanks_responses})

goodbye_phrases = ["Goodbye","bye","See you","Later","See you later","Have a nice day","Bye bye"]
goodbye_responses = ["Okay. See you...","Until next time","Glad I could be of assistance"]

data.append({"tag":"goodbye","statements":goodbye_phrases,"responses":goodbye_responses})

who_made_you_phrases = [
						"who made you",
						"what are you",
						"who designed you",
						"are you human or a bot",
						"are you a robot",
						"Tell me about yourself",
            			"who is the one that made you",
            			"who is your maker",
            			"which company made you",
            			"name the person or group that programmed you"
				]
who_made_you_responses = ["I'm a bot made by a person for this website you're visiting to help with some menial tasks.",
							"I think... no I can't think. I'm a bot made to help you with menial tasks thats all."]

data.append({"tag":"who_made_you","statements":who_made_you_phrases,"responses":who_made_you_responses})

what_can_you_do_phrases = [
            "can you tell me what you can help with",
            "what things are you able to help me with",
            "i would like to know what you can help with",
            "i want to know what type of things you can help me with",
            "can i know what type of things you can help me with",
            "what type of questions can i ask you",
            "tell me what you can do for me",
            "what are you programmed to do for me",
            "what things do you know how to do",
            "how can you help me"
        ]
what_can_you_do_responses = ["I can help you search for items for sale, make an account and other tasks as of now.",
								"The following tasks:"]
data.append({"tag":"what_can_you_do","statements":what_can_you_do_phrases,"responses":what_can_you_do_responses})


make_account_phrases = ["Create an account for me","Make me a new account","Help me set up an account","register an account here",
				"help me sign up","I want to sign up"]
make_account_responses = ["Okay. Just a moment","Please fill out you're information below","Just a moment please.",
							"Give me a second to set up the form"]
data.append({"tag":"make_account","statements":make_account_phrases,"responses":make_account_responses})

tandoa_info_phrases = ["what's this site for","who owns this site","what is tandoa","can you tell me about tandoa",
						"what does tandoa do"]
tandoa_info_responses = ["Tandoa is an e-commerce website which provides an online market for the respective members",
						"This is an e-commerce platform under the name Tandoa working as an online market place for respective members to buy and sell their goods.",
						"This is an upstart business under the name Tandoa providing an e-commerce platform for sale and purchase of goods."]

data.append({"tag":"tandoa_info","statements":tandoa_info_phrases,"responses":tandoa_info_responses})

other_phrases = []
other_responses = ["Sorry, I can't make sense of that.","I'm just a bot so pardon me not being able to answer your request.",
					"Blame my maker for slacking off and leaving me dumb.","I'm unable to complete the above task"]
data.append({"tag":"other","statements":other_phrases,"responses":other_responses})

with open("training_intents_dataset.json","w") as outfile:
	data_out = json.dumps(data,indent=4)
	outfile.write(data_out)						
