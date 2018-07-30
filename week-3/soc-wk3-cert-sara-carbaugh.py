# Compare the lexical diversity scores for humor and romance fiction in 1.1. Which genre is more lexically diverse?

import nltk
from nltk.book import *


def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

print(lexical_diversity(text2))

print(lexical_diversity(text6)) # Monty Python is more lexically diverse (.127 > .048)


# Produce a dispersion plot of the four main protagonists in Sense and Sensibility: Elinor, Marianne, Edward, and Willoughby. What can you observe about the different roles played by the males and females in this novel? Can you identify the couples?

dispersion = text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])
print(dispersion) #austin_character_plot.png
