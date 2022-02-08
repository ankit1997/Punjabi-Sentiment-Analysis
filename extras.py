feelings = {
	1:'anger',
	2:'sad',
	3:'disgust',
	4:'fear',
	5:'happy',
	6:'surprise',
	7:'no_emotion',
}

result = [
	'Anger',
	'Angry~',
	'Sad',
	'Sad~',
	'Disgust',
	'Disgust~',
	'Fear',
	'Fear~',
	'Happy',
	'Happy~',
	'Surprise',
	'Surprise~',
	'No emotion'
]

def stemmer(word):
	if word.endswith("ਿਆਂ"):
		stem=word[:-len("ਆਂ")]
				
	elif word.endswith("ੀਆਂ"):
		stem=word[:-len("ਆਂ")]

	elif word.endswith("ੂਆਂ"):
		stem=word[:-len("ਆਂ")]
				 
	elif word.endswith("ੀਏ"):
		stem=word[:-len("ਏ")]
				 
	elif word.endswith("ਈ"):
		stem=word[:-len("ਈ")]
			 
	elif word.endswith("ੇ"):
		stem=word[:-len("ੇ")]
			 
	elif word.endswith("ੀਓ"):
		stem=word[:-len("ਓ")]
			 
	elif word.endswith("ਿਓ"):
		stem=word[:-len("ਿਓ")].join('।')

	elif word.endswith("ਵਾਂ"):
		stem=word[:-len("ਵਾਂ")]

	elif word.endswith("ਾਂ"):
		stem=word[:-len("ਾਂ")]

	elif word.endswith("ੋਂ") :
		stem=word[:-len("ੋਂ")]

	elif word.endswith("ੀਂ") :
		stem=word[:-len("ੀਂ")]
	 
	elif word.endswith("ੋ") :
		stem=word[:-len("ੋ")]
		
	elif word.endswith("ਿੳਂ") :
		stem=word[:-len("ਿੳਂ")]
		
	else :
		stem=word
	return stem