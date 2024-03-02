# ftb-odds-py: A F\*ck The Bus/Ride The Bus odds calculator

F\*ck the Bus (FTB) is a [simple drinking game](https://drinkinggamesbible.com/ride-the-bus-or-fuck-the-bus-drinking-game/) that uses a pack of standard playing cards. This odds calculator ensures that you will play your best game (statistically speaking) and offloads the thinking from your potentially inebriated brain.

Simply input the cards that are drawn and the calculator will generate the odds for each stage of the game, keeping track of what cards have already been played.

# Input
As soon as you executed the script, it will be listening for either commands or card inputs only. No other input is expected.

## Card Inputs
Card inputs are structured like this: \[Rank Number\]\[Suit Abbreviation\], where \[Rank Number\] is:

**Rank Number to Rank**
1 = Ace
2..10 = 2..10 
11 = Jack
12 = Queen
13 = King

and \[Suit Abbreviation\] is:

**Suit Abbreviation to Suit**
D = Diamonds
H = Hearts
C = Clubs
S = Spades

So for example, a 2 of Clubs would be `7C` and a King of Hearts would be `13H`.

## Commands
These are the following commands that can be executed:

`q`: Quits the odds calculator.
`r`: Resets the list of played cards, resetting all odds.
