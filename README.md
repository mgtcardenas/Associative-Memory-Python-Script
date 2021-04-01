# Associative-Memory-Python-Script

This repository contains the first version of the Associative Memory Mixer, a program capable of combining two motifs in order to generate a new one.
This is done by using an Associative Memory, a type of Recurrent Neural Network which is mostly used for binary image reconstruction.
This version of the Associative Memory Mixer requires the user to interpret a composition as a binary image by himself.
The composition must be written as a series of 1s and -1s in the file "training-patterns.txt" (one pattern per line).

The script only anticipates two patterns and a matrix of 9 by 16.
Currently, the script will also generate a random input to be modified by the weight matrix.
This first version of the Associative Memory Mixer is inteded for rhythm only.
In order to design your own rhythm and listen to the results of this Associative Memory Mixer, please use the Neural Drum Machine.
Neural Drum Machine is a Pen (from CodePen) created by Tero Parviainen and can be found using the following link:
https://codepen.io/teropa/details/RMGxOQ