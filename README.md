# Wordle_Remake

Phase I
1. Assign Roles
There are three roles that need to be determined among the team:
  
    A - Head of Algorithm: 
  * Code ownership: 
  o Main algorithm for determining the final color of each letter in the answer provided by the user.
  
    B - Chief Statistician:  
  * Code ownership: 
  o Coloring console output using the right colors, including the Wordle results provided by the Head of Algorithm.
  o Keeping track of game statistics and displaying them using colors. 
  * Depends on Head of Algorithm for providing the letter -> color matching
  
    C - Handshake Rockstar: 
  * Point-of-contact in charge of scheduling the meetings among the team members, and also with the Google TAs. 
  * Code Ownership: 
  o Navigation through the program, including giving the user an option of whether to start a new wordle game, show stats, or exit.
  o Taking input and validating it: capitalize all letters, reject non-dictionary words or words of length distinct from 5
  * Depends on Head of Algorithm and Chief Statistician for running their pieces, depending on user selection
  
  Everybody: 
  * Meet, discuss and help each other by explaining how things work, not by giving away answers without explanation (help your teammates learn and do better). 
  * Document your code with comments as needed, focus on consistent code style.
  * Test the program end-to-end, find bugs and fix them along the way. 
  * Represent the project during the final presentations. You will be expected to know how the code does and does not work. 
  

Phase II
2.  Create Example Guesses and Outputs
We will start by coming up with some example inputs and outputs. We will use example 4 as your motivating example (i.e. when you are explaining your doc or code to a TA, you can use your sample to show if your idea will work for all 3 color cases). Make sure your examples are 5 letters long and don’t have duplicate letters.
  
  
  1. All letters in the guess are correct (have a green background)
    a. Guess: SHAKE
    b. Answer: SHAKE
  2. Some letters in the guess are in the secret word (have a yellow background) 
    a. Guess: PAINT
    b. Answer: SHAKE
  3. All letters in the guess are not in the secret word (have a gray background)
    a. Guess: POWER
    b. Answer: VALID
  4. The guess has letters with green, yellow, and gray backgrounds (don’t use my TOWEL and LOWER example - come up with a new example)
    a. Guess: SHAKE
    b. Answer: SALTY
  5. Start with the First Letter in Guess
  Part of why this project seems complex is that we need to do a lot of checks. Let’s break down the problem by first just focusing on the first letter. 
  Assume we have the following two variables:
  
  guess = ‘WORDS’    # Stores the user’s guess for each round
  answer = ‘VALID’   # Stores the secret word
  
  
  
  
  How can we check if the first letter of guess should be printed with a green background?
  
  if guess[0] == answer[0]:
      # Print (guess[0], ‘Green’)   
  
  How can we check if the first letter of guess should be printed with a gray background?
  
  elif guess[0] in answer and guess[0] != answer[0]:
      # Print (guess[0], ‘Yellow’)
  
  How can we check if the first letter of guess should be printed with a yellow background?
  
  else:
      # Print (guess[0], ‘Gray’)

3.  Apply Previous Step to All Letters in Guess
You might have used a specific index number [0] to get the first letter in guess in the above section. Now how can we generalize that solution to work through every letter in guess? How can you use while loops and an index counter to achieve this?
  
  answer = list('SKEET')
  guess = list(input().upper())
  lis = [' ', ' ' , ' ' , ' ', ' ']
  
  def check(answer, guess, lis):
      for i in range(5):
          if answer[i] == guess[i]:
              lis[i] = 'Green'
              answer[i] = ' '
      
      for i in range(5):
          if guess[i] in answer and lis[i] == ' ':
              lis[i] = 'Yellow'
      for i in range(5):
          if lis[i] == ' ':
              lis[i] = 'Grey'
              
      print(lis)
      
  check(answer, guess, lis)


4.  Passing Colors to Chief Statistician
Now that we can determine the correct colors for each letter, we want to make sure that we share it with the Chief Statistician in a way that lets them print the full output.
How can we update our previous while loop so the color information can be shared with and used by another part of the code?

  def categorize_colors:
    Dict = {}
    index = 0
    while index < len(guess):
       if guess[index] == answer[index]:
           print('Green', guess[index])
           Dict[guess[index]] = ‘Green’
       elif guess[index] in answer:
           print('Yellow', guess[index])
           Dict[guess[index]] = ‘yellow’
       else:
           print('Grey', guess[index])
           Dict[guess[index]] = ‘Grey’
       index += 1
    return <what should we return here?>

5.  Handling Duplicate Letters
Now that you’ve colored each letter in a guess, you’ll want to check that it works for duplicate letters in both the secret word and the guessing word.
  Let’s show a few more examples:
  1. The secret word does not have duplicate letters, but the guess does.
    a. Guess: SKEET
    b. Answer: STARE
    c. Output: Green S, Grey K, Yellow E, Grey E, Yellow T
  2. The secret word has duplicate letters, but the guess does not.
    a. Guess: STARE
    b. Answer: SKEET
    c. Output: Green S, Yellow T, Grey A, Grey R, Yellow E
  3. Both the secret word and the guess have duplicate letters.
    a. Guess: SKEET
    b. Answer: STATS
    c. Output: Green S, Grey K, Grey E, Grey E, Yellow T

Role B: Chief Statistician
6.  Counting game stats
How can we keep track of the number of wins and losses and use this data to calculate the % of games won?

  Win = 0
  Loses = 0
  if index = 0: 
      print(input(“guess a word” ))
  elif <What condition should go here when the player wins?>
        guess == answer:
         print(“cool”)
         Win += 1
  elif guess_count == 6 and guess != answer:
      Loses += 1
  
  return win / (win + loses) 

7.  Win Frequency for Each Number of Guesses
We also need to show the distribution for the number of games won for each number of guesses.

  How can we calculate the win percentage for each number of guesses?
  
  wins_by_guesses = {}           {num_guesses:num_games} 
  
  if num_guesses not in win_by_guesses:
       wins_by_guesses[num_guesses] = 1 
  else (if num_guesses in win_by_guesses)
      wins_by_guesses[num_guesses] = win_by_guesses[num_guesses] + 1 

8.  Printing Color to the Background
Throughout the game, you will need to print each letter in a specific color and background color (e.g., green, yellow, gray). What color to print should come from the Head of Algorithm, and you will need to figure out how to display those colors in the game.
  
  We have provided you with a file coloring.py that gives you helpers to set the color.
  How would you use the utility to set the color of a letter?
  letter = “a”
     coloring.green(letter)
  
  Now, how can we iterate through each letter in a guess and apply the appropriate color?
  
  def colored_word(letter):
  
      for word in letter:
          match word:  
              Case “green”:
                    print(“Its green)
              Case “yellow”:
                    print(“Its yellow)
              Case “Grey”:
                    print(“nah”)
      return none
  
  Role C: Handshake Rockstar

9.  Read in the Word Dictionary
For this assignment, we’ve prepared a dictionary (file) of valid secret words in a file. Only words from this list are valid, meaning only these words can be used as the secret word or as a guess in the game.

  How would you read in a file and store it in a list?
  Import file
  A = open (dict.txt)
  Contents = [a for a in A.read()]
  

10.  Allow The User to Make Multiple Guesses
So far, we have a solid plan for how to deal with one guess. But now we want the user to keep making guesses until they win (the user guesses the answer) or they lose (the user runs out of their 6 guesses).

  How do we check if the user should keep guessing?
  
  def has_won(num_guesses, user_input):  *NOTE : SHOULD INVOLVE A BOOLEAN 
      if user_input == secret_word:
          print(‘Congrats’) Return TRUE
      Elif num_guesses == 6 and user_input != secret_word:
         print(‘Game over’) RETURN TRUE 
      Else:
         print(‘Guess Again’) RETURN FALSE
  
  
  To continue game play, how would you set up a while loop and num_guesses variable below? The loop should be True if the user hasn’t won or lost the game yet (i.e. they should keep making guesses).
  
  num_guesses = 0
  # Continue the game while…
  while user_input != secret_word and num_guesses < 6:
       User_input = input()
     # num_guesses += 1

11.  Wordle Game Output
After each game ends we’ll want to let the user know if they won or lost. 
  * If they won, also mention how many guesses it took.
  * If they lost, also mention what the answer was.
  * Regardless of if they won or not, print the updated game statistics.
  
  What if / else if statement can you set up at the end of your code? Also include your cout statements.
  if has_won():
       print(f’ You WOn! It took {num__guesses} guesses.’)
  else
      print(f’You lost… The word was {secret_word}’)
  print(Stat_result_function)
  
  12.  Starting a Game
  Last, but definitely not least, you’ll need a way for the user to exit the game or continue playing new games.
  
  How do you prompt the user after each game to know if they want to play a new game or exit the program?
  print(input(‘Would you like to play again?’ ))
  <How do you process the user’s input?>
  
  if input == ‘Yes’ or input == ‘yes’:
      Restart the Game
  elif input == ‘no’ or input == ‘No’: 
      End the game. Stop!
  else:
      print(input(‘Please enter yes or no.’ ))

13. Putting it All Together
Write some pseudocode that outlines what your project will look like. Remember, you have the following main components:
  1. The dictionary in Section 13 to check words against.
  2. A while loop from Section 15 that allows the user to keep making guesses.
  3. Another while loop from Section 9 where you process each of the 5 letters in guess.
  4. An if..elif..else statement from Section 10 to calculate game stats.
  
  1. Ask user for input
  2. Check if input meets requirements 
  a. Input is 5 words long
  i. If not ask user to enter another word
  b. Input is in the dictionary 
  i. If not ask user to enter another word 
  c. Input is all uppercase letters
  i. Ask user to enter another input or Make the word uppercase manually
  3. Check if input matches the secret word
  a. If not add 1 to guess tally 
  b. Prompt user to enter another guess
  4. If guess count reaches 6 and input still hasn’t matched secret, User lost
  a. Display that user lost and reveal secret word.
  i. Show the stats
  ii. Num_games += 1
  5.  If input matches secret word, User Won.
  a.  Display the user won and # of guesses it took
  i. Show the stats
  ii. Num_games += 1
  6. Ask user if they’d like to play again
  a. If user types Yes or yes 
  i. Restart the game 
  b. If user types no or No 
  i. Stop the program 
  c. If user types neither 
  i. Ask user to type yes or no(or Yes or No)
  win_by_guesses[num_guesses] = win_by_guesses[num_guesses] + 1
