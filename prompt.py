import re

def sepPrompt(prompt):
	prompt = re.split("([+|×|÷|/|<|>|%|*|-|' '|~])", prompt)
	
	for x in range(0,10000):
		for a in prompt:
			if (str.isspace(a)) or (a == ''):
				prompt.remove(a)
	
	return prompt