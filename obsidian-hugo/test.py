import markdown2
from format import format_internal_links, format_internal_aliased_links, format_tags

obs = """![](https://toriavey.com/images/2011/01/Falafel-10-640x480-1.jpg)

## Ingredienser

Oppskrift for **6** porsjoner (5 falafler per porsjon):

- 500 g [[Kikerter|tørkede kikerter]]
- 0.5 ts [[Bakepulver|bakepulver]]
- 1 [[Løk|liten løk]]
- 0.5 dL [[Persille|bladpersille]]
- 3-5 fedd [[Hvitløk|hvitløk]]
- 1.5 ss [[Mel|mel]]
- 1.75 ts [[NaCl|salt]]
- 2 ts [[Spisskummen|spisskummen]]
- 1 ts [[Korianderfrø|malt korianderfrø]]
- 0.25 ts [[Pepper|sort pepper]]
- 0.25 ts [[Kajennepepper|kajennepepper]]
- Litt [[Kardemomme|malt kardemomme]]
- Olje til frityrsteking (typisk [[Solsikkeolje|solsikke]])

## Fremgangsmåte

- Hermetiske kikerter smuldrer opp og gir falaflene en veldig tørr konsistens. Bruk derfor tørkede kikerter. Disse må bløtlegges 12-24 timer i forveien, med rikelig med vann. Tilsett gjerne 0.5 ts [[Bakepulver|bakepulver]] i vannet for å få kikertene enda mykere. De eser ut og blir omtrent dobbelt så store.
- Hell av vannet og skyll kikertene godt etter bløtlegging. Ha i en foodprocessor sammen med [[Løk|hakket løk]], [[Hvitløk|hvitløk]], [[Persille|persille]], [[Mel|mel]], [[NaCl|salt]], [[Spisskummen|spisskummen]], [[Korianderfrø|koriander]], [[Pepper|pepper]], [[Kajennepepper|kajennepepper]] og [[Kardemomme|kardemomme]].
- Kjør alt sammen til blandingen har konsistens et sted mellom couscous og en paste. Du vil at falaflene skal holde sammen, men du ønsker ikke hummus. Bilde for referanse:
	
	![](https://toriavey.com/images/2011/01/Falafel-4-900x675.jpg)

- Vil du være ekstra nøye kan du nå ha blandingen over i en bolle og blande sammen med en gaffel. Dette vil gjøre den jevnere og du får sett om det er noen kikertklumper igjen.
- Legg blandingen i kjøleskapet i 1 time.
- Varm opp 3-4 cm med olje i en stor panne/kjele. Bruk gjerne en olje med høyt røykpunkt. [[Solsikkeolje]] har et røykpunkt mellom 180°C og 200°C, som er ideell temperatur for fritering av falafler.
- Form falafelblandingen til små "pucker" og legg dem i oljen. En tommelfingerregel er 2 ss med blanding per "puck", men her må du føle deg frem. La dem brunes i 2-3 minutter per side.

	> **Tips**: Falaflene er ganske løse når du former dem, men burde bli faste så fort de legges i oljen. Er de for løse til å legge ned i pannen, kan du gjerne kjøre blandingen litt ekstra i foodprocessoren, eller tilsette 1-2 [[Egg|egg]] for å få den litt fastere. 

	> **Tips**: Test gjerne med én falafel først for å peile steketiden. Ideelt sett skal de trenge 2-3 minutter per side for å få en gyllen brunfarge, men går det fortere er oljen for varm og de vil ikke bli gjennomstekt. 

- Når falaflene er ferdige, la dem kjøle seg litt ned på kjøkkenpapir og server toppet med litt [[Tahini|tahini]], ved siden av litt [[Pita|pitabrød]] og [[Hummus|hummus]].

[Kilde](https://toriavey.com/toris-kitchen/falafel/)

#Oppskrift
"""

md = format_internal_links(
        format_internal_aliased_links(
            format_tags(obs)))

md = markdown2.markdown(md)

print(md)
