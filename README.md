I decided to make a mini Spotify player because I love listening to music, and I thought it would be cool to be able to see what's playing even if I'm doing other things on my PC. It shows me the current song, artist, and a progress bar with the current timestamp and the length of the whole song.

On the hardware side, I made a PCB that connects a Raspberry Pi Pico W to a LCD display.
<img width="403" height="566" alt="pcb" src="https://github.com/user-attachments/assets/788c5ca3-eee8-417c-b394-6d29c6281afc" />

THe wiring looks like this in the schematic. It's quite simple, as I'm only connecting the raspberry pi to the disaply 8 pin socket.
<img width="909" height="826" alt="cleanwire" src="https://github.com/user-attachments/assets/d1efb6e0-bc0f-43b2-abee-85b87e505634" />

Once it's made for real and I build it, it will look like the 3d render here, just with a display attached to the 8 pin socket seen on the PCB>
<img width="1057" height="598" alt="3dmodel" src="https://github.com/user-attachments/assets/c792ab5e-fb6a-4b69-b3ec-790773207bca" />

The software is the more complex of the two, and here is a brief explanation of how it works.

Basically, this connects the raspberry pi to the PC over WiFi, and sets up the screen to recieve data from the PC. It also initializes the screen to be all black until it has to disaply something.
<img width="689" height="488" alt="week5code1" src="https://github.com/user-attachments/assets/2a9beef1-2ea6-43b7-bb7c-bc97fa2c1c6d" />

In this part of the code, it defines varibales such as the title, artist, and etc. It also takes the title and artist and prints it on the display.
<img width="765" height="360" alt="week5code2" src="https://github.com/user-attachments/assets/7b535eda-519a-4457-b27a-2ecee65af3c1" />

Lastly, this part takes the ratio of current time over the total length of the song, and fills in the progress bar accordingly. It then prints that, along with the current time and total time, updating every second.
<img width="896" height="305" alt="week5code3" src="https://github.com/user-attachments/assets/5d546cb5-6630-44ee-9bfb-59c1c588cc70" />


