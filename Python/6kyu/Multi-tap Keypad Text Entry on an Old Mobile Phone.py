def presses(phrase):
	keypad = ['1', 'abc2', 'def3', 'ghi4', 'jkl5', 'mno6', 'pqrs7', 'tuv8', 'wxyz9', '*', ' 0', '#']

	totla_presses = 0

	phrase = phrase.lower()

	for char in phrase:
		for button in keypad:
			if char in button:
				totoal_presses += 1 + button.find(char)
	return total_presses
