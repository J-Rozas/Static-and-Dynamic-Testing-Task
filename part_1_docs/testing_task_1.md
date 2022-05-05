### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  # This would fail after card.value there is an assignment operator (=) rather than an equal comparison operator (==)
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
  # This would fail because the keyword to start a function is misspelled. It should be "def" rather than "dif"
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

  # This would fail because the return is inside of the loop, so the function would exit at the end of the first iteration regardless of the number of cards
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
