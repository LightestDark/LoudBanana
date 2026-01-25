# LoudBanana
A submission into wacky files that converts the image into a .wav audio file and then back again



Ver 1:
After some research, I found that the simplest way to change the image uis by turning the image’s pixel bytes directly into raw audio sample values, plays them as sound, then reverses the mapping to turn the exact same numbers back into the image

So far I have found a way to make the image a loooong line of numbers of bits.

<img width="388" height="170" alt="image" src="https://github.com/user-attachments/assets/834e75cb-83db-47db-8376-e2768a4140c5" />

So far what I have mustered up granted it's really compact
Ver 2:

Added a auto open of the banana file, reduced code lines through some yt tutorials and placed all files in a auto generated folder!

Ver 3:

Added together the decoding and encoding.py files into one for easier access.

Ver 4 : (FINAL FOR NOW)

I kept gettign errors in my krnl for windows when i realised that the libraries that I was using were exclusive to C, so i swapped out some libraries so it would work for windows too, also merged the installer.py into the main.py just for easier access. Last but not least, I found a way to extract only the red, green and blue aspects of the image via some fancy transformations, and it also saves them into the same file!




