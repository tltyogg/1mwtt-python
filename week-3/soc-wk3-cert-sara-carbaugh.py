# Day 1
print('')
print('***** DAY ONE *****')
print('')

# Compare the lexical diversity scores for humor and romance fiction in 1.1. Which genre is more lexically diverse?

# import nltk
# from nltk.book import *
#
#
# def lexical_diversity(text):
#     return len(set(text)) / len(text)
#
# def percentage(count, total):
#     return 100 * count / total
#
# print(lexical_diversity(text2))
#
# print(lexical_diversity(text6)) # Monty Python is more lexically diverse (.127 > .048)
#
#
# # Produce a dispersion plot of the four main protagonists in Sense and Sensibility: Elinor, Marianne, Edward, and Willoughby. What can you observe about the different roles played by the males and females in this novel? Can you identify the couples?
#
# dispersion = text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])
# print(dispersion) #austin_character_plot.png


# Day 2
print('')
print('***** DAY TWO *****')
print('')

# type up the whole Chapter 1

# exercises 8 and 10

# ◑ Define a conditional frequency distribution over the Names corpus that allows you to see which initial letters are more frequent for males vs. females (cf. 4.4).

# ◑ Read the BBC News article: UK's Vicky Pollards 'left behind' http://news.bbc.co.uk/1/hi/education/6173441.stm. The article gives the following statistic about teen language: "the top 20 words used, including yeah, no, but and like, account for around a third of all words." How many word types account for a third of all word tokens, for a variety of text sources? What do you conclude about this statistic? Read more about this on LanguageLog, at http://itre.cis.upenn.edu/~myl/languagelog/archives/003993.html.

# The rest of the exercises are optional, of course they provide fabulous practice.

# Day 3
print('')
print('***** DAY THREE *****')
print('')

# Do research to see what Python libraries are already in existence that you could start using in your day-job, or daily life.
#
# Exercises on WordNet

#5 ☼ Investigate the holonym-meronym relations for some nouns. Remember that there are three kinds of holonym-meronym relation, so you need to use: member_meronyms(), part_meronyms(), substance_meronyms(), member_holonyms(), part_holonyms(), and substance_holonyms().
#13 ◑ What percentage of noun synsets have no hyponyms? You can get all noun synsets using wn.all_synsets('n').
#14 ◑ Define a function supergloss(s) that takes a synset s as its argument and returns a string consisting of the concatenation of the definition of s, and the definitions of all the hypernyms and hyponyms of s.
