# DeepQLearningForWoW
(This is my first project on neural networks of this scale.)
Teaching model: Deep Q Learning
Attention! AI is not completed to the end, as you need access to the game API to get data into the Q table.
                                                             Principle of operation.
The table contains data about the position of your character, two enemies and an ally, about their class and race, about health and the amount of resources, about the abilities of the covenant and saves.
                                                      Getting data about X and Y coordinates.
The repository contains files “X.png” and “Y.png” (I apologize right away for the quality, I just couldn't find the best photo in Google)
The main idea is to divide the arena area into 4 equal rectangles (including the spawn to avoid mistakes) and change the value in the Q table depending on the position.
                                                        Definition of race and class.
Using the game API, we get information about the races and classes of all participants in the battle. You ask: "how do we pass values ​​to the table?"
I answer.
You can divide 1 by the number of races (classes) and, depending on the race (class), transfer the desired value (start the countdown from the person (warrior for the class) and then add 1 / the number of races (classes)).
We do the same with the covenant and save abilities.
                                                     Definition of health and resources.
It's really quite simple, we divide the percentage of% of current health and resources by 100 and pass this value.
                                                              Learning process.
I created an environment in OpenAI Gym (for objective reasons it needs to be improved). To make the neural network easier to learn, we run the game and the “main.py” file at the same time and train it for a long time until we reach the desired result (to speed up the training, you can run several class setups at once).
