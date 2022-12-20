# PythonStuff
A repository of all I've been learning about Python and Version Control using GitHub

## My First Markdown Boilerplate, Haha😂  
### Credits to [ChristianLempa](https://github.com/ChristianLempa) on GitHub 
![Compile](https://github.com/mobizt/Firebase-ESP8266/actions/workflows/compile_library.yml/badge.svg) ![Examples](https://github.com/mobizt/Firebase-ESP8266/actions/workflows/compile_examples.yml/badge.svg) [![Github Stars](https://img.shields.io/github/stars/mobizt/Firebase-ESP8266?logo=github)](https://github.com/mobizt/Firebase-ESP8266/stargazers) ![Github Issues](https://img.shields.io/github/issues/mobizt/Firebase-ESP8266?logo=github)
---
All rights reserved. No part of this book shall be __reproduced__, __stored in a retrieval system__, or 
__transmitted by any means__, __electronic__, __mechanical__, __photocopying__, __recording__, or otherwise, without 
written permission from the publisher. *No patent liability is assumed with respect to the use of 
the information contained herein.* Although every precaution has been taken in the preparation of 
this book, the publisher and author assume no responsibility for errors or omissions. Nor is any 
liability assumed for damages resulting from the use of the information contained herein.  

---

Image with alt text:  
![KiCAD Image](https://repository-images.githubusercontent.com/256938513/f21ca700-fada-11ea-9bb9-10a6ea72efbe)  


Emphasis, aka italics, with *asterisks* or _underscores_.

Strong emphasis, aka bold, with **asterisks** or __underscores__.

Qiskit code for **Bernstein Vazirani Algorithm**.  

```python
def bernstein_vazirani(string):
    
    # Save the length of string
    string_length = len(string)
    
    # Make a quantum circuit
    qc = QuantumCircuit(string_length+1, string_length)
    
    # Initialize each input qubit to apply a Hadamard gate and output qubit to |->
    
    qc.x(string_length)
    qc.h(string_length)
    qc.h(range(string_length))
    
    qc.barrier()
    
    # Apply an oracle for the given string
    # Note: In Qiskit, numbers are assigned to the bits in a string from right to left
    
    for ii, yesno in enumerate(reversed(string)):
        if yesno == "1":
            qc.cx(ii, string_length)
    qc.barrier()
    
    # Apply Hadamard gates after querying the oracle
    qc.h(range(string_length))
    qc.barrier()
    
    # Measurement
    qc.measure(range(string_length), range(string_length))
    
    
    
    return qc
```

Strikethrough uses two tildes. ~~Scratch this.~~

__BIGGER__ ~~THAN~~ __AND__ __BETTER__  

Image without alt text:  
![](https://upload.wikimedia.org/wikipedia/commons/5/50/KiCad_V6_PCB_Full_View.png)

__*LINK NEVER BEFORE*__  

First line with two spaces after it.  
And the next line.

1. First item
2. Second item
3. Third item
4. Fouth item

🎶 Music  
🍔 Eat  
👨‍💻 Code  
🛌 Sleep  
🔁 Repeat  

Link with text: [My Email](https://www.gmai.com/quameofosuemma@gmail.com)  

Inline `code` has `back-ticks around` it.  
Then type `print("Hello World")` in the next cell  

Check out A KiCAD board he rendered in Blender below:  
![Quantum Circuit](https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/133449391/original/7049eccda8469a83e1d7596a3918c6de6d18616c/do-realistic-renderings-of-your-pcb.png)  


``` python  
def mqc_s(quantity):
    print("MULTIPLE CHOICE------------------------------------")
    for i in range(quantity):
        guess = input(multple_choice[i])
        check_guess(guess, multiple_choice_Ans[i])
        print("-----------------------------------------------")
```  
```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```  

```
No language indicated, so no syntax highlighting. 
But let's throw in a tag.
```  
| Heading 1 | Heading 2 | Heading 3 |
|---|---|---|
| col1 | col2 | col3 |
| col1 | col2 | col3 |  


``` python  
import random

print("-------------Nine Lives Challenge Game-------------")
print("Developed by Manuel Ofosu Copyright@15/12/2022")
print('-----------------------------------------------')
print('-----------------------------------------------')

lives = 9
words = ['pizza', 'fairy', 'teeth', 'shirt',
         'otter', 'plane', 'brush', 'horse', 'light']
secret_word = random.choice(words)
clue = list('?????')
heart_symbol = u'\u2764'
guessed_word_correctly = False

# Function to Update clue


def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1


# Keep asking the user to guess untill they run out of lives

while lives > 0:
    print(clue)
    print('lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect. You lose a life')
        lives = lives - 1

# Determine if player won or lost

if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)
else:
    print('You lost! The secret word was ' + secret_word)

```

![KiCAD Image](https://i.ytimg.com/vi/C7-8nUU6e3E/maxresdefault.jpg)

| Semester 1 | Semester 2 | Semester 3 |  
|---|---|---|  
| 100% | 65%  | 89% |  
| 100% | 65%  | 89% |  
| 100% | 65%  | 89% |  
| 100% | 65%  | 89% |  
| 100% | 65%  | 89% |  

[x] Open the cheatsheet website  
[x] Navigate to the cheatsheet Repo  
[x] Write the post  
[ ] Update the website  
[ ] Contact the user  


### __Appreciations__
: 

Here's a sentence with a footnote. [^1]

[^1]: This is the footnote.
