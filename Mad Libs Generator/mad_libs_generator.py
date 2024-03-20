'''
A mad lib generator where users can input various parts of a story 

'''

import random
import re

story_templates = [
    "Once upon a time, there was a {noun[0]} who loved to {verb[0]} in the {place[0]}. One day, they {adverb[0]} {verb[1]} and {verb[2]} {adjective[0]}. It was a {adjective[1]} {noun[1]}!",
    "In a {adjective[0]} {place[0]}, there lived a {noun[0]} who had a passion for {verb[0]}. Every day, they would {adverb[0]} {verb[1]} and feel {adjective[1]}.",
    "Once upon a time, in a {adjective[0]} kingdom, there was a brave {noun[0]} who embarked on a quest to {verb[0]} the {noun[1]} and save the {noun[2]} from {adjective[1]} peril.",
    "In a futuristic {place[0]}, a brilliant {noun[0]} created a {adjective[0]} {noun[1]} that could {verb[0]} {adverb[0]}. Little did they know, their invention would {verb[1]} the world forever.",
    "Long ago, in a mystical {place[0]}, a young {noun[0]} discovered a {adjective[0]} {noun[1]} hidden deep within a {noun[2]}. As they {verb[0]} it, they gained incredible {adjective[1]} powers.",
    "In a bustling city, a {noun[0]} dreamed of becoming a renowned {noun[1]}. Through hard work and {adjective[0]} determination, they {verb[0]} their way to the top, inspiring others along the way.",
    "On a remote island, a group of {adjective[0]} {noun[0]} embarked on an exciting {adjective[1]} {noun[1]}. Together, they faced {adjective[2]} challenges and discovered the true meaning of {noun[2]}."
]

input_categories = {
    "noun": "Enter a noun: ",
    "verb": "Enter a verb: ",
    "place": "Enter a place: ",
    "adverb": "Enter an adverb: ",
    "adjective": "Enter an adjective: ",
}

story_template = random.choice(story_templates)

user_inputs = {category: [] for category in input_categories}

# Determine the number of occurrences for each input category in the story template
for category, _ in input_categories.items():
    count = len(re.findall(r"\{" + category + r"\[\d+\]\}", story_template))
    user_inputs[category] = [input(f"Enter {category.capitalize()} {i + 1}: ") for i in range(count)]

# Replace the placeholders in the story template with user inputs
for category, inputs in user_inputs.items():
    for i, value in enumerate(inputs):
        story_template = story_template.replace("{" + category + f"[{i}]" + "}", value)

print(story_template)
