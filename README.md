# StringManipulation
UTM Hack Lab Code Challenge 2

Code String Manipulation 

1. Return all duplicate letters in a string, in alphabetical order. 
```
>>> duplicates("Bookkeeper") 
eko 
>>> duplicates("Java") 
a 
```

2. You are given three strings: first, second and third. Your function should return true if and only if the third string, is a shuffle of the first string and the second string. ie, uses all the letters of the first and second strings in any order. 
```
>>> shuffle ('abc','def','aafedc') 
false 
>>> shuffle('ab','cd','dacb') 
true 
```

3. Remove all of the vowels from the input list of strings (Function Name: remove_vowels() 

4. You are given two strings: a and b. If the strings share 3 consecutive letters, return a new string which is the combination of the first part of the first string, the 3 same letters, and then the second part of the second string. Otherwise return the empty string. 
```
>>> new_word('windspeaker','special') 
windspecial 
>>> new_word('cat','rebound') 
"" 
>>> new_word("beansprouts","unanswered") 
'beanswered' 
```

5. Every letter has a score based on it's place in the alphabet. a = 1, b= 2... z = 26. If there are no repeat letters, then the word score gains 10 bonus points. Given a list of words, re-order the words by their score (from highest to lowest) and return the re-ordered list. If words have the same score, order them alphabetically. (Function Name: word_score())


NOTE: Use the correct function names as in the examples. As well as call the file: challenge2.py
