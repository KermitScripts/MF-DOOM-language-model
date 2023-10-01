I asked chatGPT to generate an MF DOOM inspired song and this is what it came up with.<br /> 
I'm MF DOOM, the villainous one<br />
Hiding behind a metal mask, my face is never shown<br />
I spit rhymes like bullets, sharp and deadly<br />
Leaving my competition in the dust, already<br />
<br />
I'm the king of the underground, no one can bring me down<br />
I reign supreme, I wear the crown<br />
I'm the doom bringer, the one and only<br />
I'm MF DOOM, the legendary MC<br />

Just to compare how bad this is, here is an example of the sort of word play MF DOOM is known for:<br />
...what up?<br />
To all rappers, shut up.<br />
While you shutting up, keep a shirt on,<br />
At least a button up. Yuck... Is they rhymers or stripping males?<br />
Outta work jerks, since they shut down chippendales.<br />
Chipping nails,<br />
DOOM - tipping scales,<br />
Let alone the preorders, that's counted off shipping sales,<br />
This one goes out to all my people skipping bail,<br />
Dipping jail, whipping tail, and sipping ale.<br />
<br />
I went out to train my own GPT on lyrics from MF DOOM to see if I can do any better. I followed Andrej Karpathy's tutorial https://www.youtube.com/watch?v=kCc8FmEb1nY&t=6027s&ab_channel=AndrejKarpathy. Sadly I do not have a graphics card so had to scale down the model a fair bit, it has 0.009825 parameters. As expected a model this small will only spit out garbage and this is exactly what happaned. The traning and validation plot can be found in figure_1.png.
<br />
This is the best my model can do:<br />

P.zered kiti geens yon you srio' I larvin't't hent C<br />
"Eis rucke too take cool al there fom gow core oule I bis the camf mer<br />
Lith Plil t aste ames and jud coflc cay<br />
Gom pam nof cloms swinnedy<br />
As whed y wig F Pou dor mfarat anke whith tar demininsts whon<br />
<br />
Wan swhonown fellor, thent, thel the chlick<br />
Whe clit heatngulaks<br />
Amatobuh t mil wint vait asch<br />
I's a ttryo shom doot Reo he buall<br />
I a pinge<br />
To stot wit git icotssedes anin'sth avom, seast<br />
Wis pikeress sther o deseade fick Re tictosh<br />
om sa fop le<br />
<br />
<br />
If you want to try for yourself, the scrapeLyrics.py file scrapes the website https://www.songlyrics.com/mf-doom-lyrics/ for all the lyrics and puts them into the lyrics.txt file. Then it's just a case of running the gpt.py file. However, I sincerly recomend running this on a computer with a GPU. 

