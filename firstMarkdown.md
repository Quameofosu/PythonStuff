## My First Markdown Boilerplate, Haha😂  
### Credits to [ChristianLempa](https://github.com/ChristianLempa) on GitHub  
---
All rights reserved. No part of this book shall be __reproduced__, __stored in a retrieval system__, or 
__transmitted by any means__, __electronic__, __mechanical__, __photocopying__, __recording__, or otherwise, without 
written permission from the publisher. *No patent liability is assumed with respect to the use of 
the information contained herein.* Although every precaution has been taken in the preparation of 
this book, the publisher and author assume no responsibility for errors or omissions. Nor is any 
liability assumed for damages resulting from the use of the information contained herein.  

---

Image with alt text: ![QuantumComputer](https://qiskit.org/documentation/_images/depth.gif)  


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

Image without alt text: ![](https://camo.githubusercontent.com/4d89cd791580bfb19080f8b0844ba7e1235aa4becc3f43dfd708a769e257d8de/68747470733a2f2f636e642d70726f642d312e73332e75732d776573742d3030342e6261636b626c617a6562322e636f6d2f6e65772d62616e6e6572342d7363616c65642d666f722d6769746875622e6a7067)

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

Check out A KiCAD board he rendered in Blender below:  ![Quantum Circuit](https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/133449391/original/7049eccda8469a83e1d7596a3918c6de6d18616c/do-realistic-renderings-of-your-pcb.png)  


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


