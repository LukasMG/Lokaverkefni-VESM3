# IOT Sjálfsali

## Verlefnalýsing

Verkefnið var í raun tveir partar. Það var auðvitað sjálfsalinn og virkninn hans, síðan var það vefsíðan sem hélt utan um allar upplýsingar fyrir eigandann að skoða.
Við vorum í raun bara að ná í einfaldar "sölu" upplýsingar um sjálfsalann. Það var upplýsinga söfnun um stöðu hólfa (hvort þau voru tóm eða ekki), upplýsingar um hversu mikið kúnar eru búnir að eyða í sjálfsalann og hvað er vinsælasta varann.

## Efnislisti

3x Servo

1x esp32

1x 4x4 Numpad

1x OLED skjár

## Virkni

Sjálfsalinn sjálfur átti í raun að nota tvær "tölvur". Hann var með esp32, sem notaði [þessa](https://github.com/LukasMG/Lokaverkefni-VESM3/tree/main/Lokaverkefni%20VESM-3/Wending_machience/Wending_machience) skrá. Esp32 var ekki með neinn rök í sér, eina sem hann gerði var að senda gögnin sem voru sent til hans á adafruit Io, semsagt numpad, og tók á móti skipunum, t.d. til að opna hólf. Talvan sem var með rökinn hefði geta verið hver sem er, það hefði líklegast verið raspberri pi í lokaútgáfu en við notuðum bara skólatölvurnar okkar til að keyra skjalið, [þetta](https://github.com/LukasMG/Lokaverkefni-VESM3/tree/main/Lokaverkefni%20VESM-3/processor) er það skjal. 

Rök talvan tók á móti gögnunum frá esp32 og vann í gegnum þau, ef þau voru leyfð eða lögleg þá hélt rök talvan áfram og myndi biðja um næstu gögn, semsagt rfid kortinu. Ef öll gögn voru lögleg þá myndi rök talvan segja esp32 að opna hólfið sem notandi vildi opna og varan er gefinn.

Ps. Kóðaskjölin virka ekki fullkomlega eins lokavirkninn átti að vera. Það vantaði OLED skjáinn, það vantar sambands miðilinn á mílli esp32 og rök tölvurnar og það vantar error-kóða úrvinnslu á esp32. Því miður komu upp vandamál sem ég munn útskýra á eftir.

Vefsíðan notaði gögninn út frá Adafruit Io til að finna tölfræði um sjálfsalann. Við notuðum flask til að búa til vefsíðuna og við ætluðum að geyma hana á Heroku. Hún hélt skjölum sem voru með tölu sem sagði til hversu mikið af gagna eintökum voru sent, ef sú tala hækkaði þá fór sala í gegn og vefsíðan myndi byrja fara í gegnum tölfræðina með því að kveikja á föllum, kóða mappann fyrir vefsíðuna er [hér](https://github.com/LukasMG/Lokaverkefni-VESM3/tree/main/Lokaverkefni%20VESM-3/Vefsíðan).

[Hér](https://youtu.be/VfE6Zoql3Tg) er myndband af virkni vefsíðu og gögnin sem hún heldur um. Ég er bara persónulega að bæta við gagna stökum í gagnasöfnuna okkar en það breytir engu upp á virkni

## Hönnurnar ákvarðarnir

Við þurftum að parta niður mikið af upprunlegu skránni af kassanum vegna þess að hún var hreinlega allt of stór þegar það kom að því að skera kassann út.

Við höfðum ekki það mikinn tíma og við höfðum enga hugmynd um hvernig við áttum að samþykkja og vinna út úr gögnunum sem við fengum frá notanda, semsagt numpad og rfid, þannig til að laga það léttum við auka tölvu vinna út úr því sem notaði python, tungumál sem við höfðum mikla reynslu í.

## Myndir af öllu

Hér höfum við mynd af rafrásinni í því ástandi sem hún átti að vera í

![Rafrás](https://github.com/LukasMG/Lokaverkefni-VESM3/blob/main/Lokaverkefni%20VESM-3/mynd/rafras.png)

Hér eru nokkrar myndir af sjálfsalanum sjálfum

![kassi 1](https://github.com/LukasMG/Lokaverkefni-VESM3/blob/main/Lokaverkefni%20VESM-3/mynd/kassi1.png)

![kassi 2](https://github.com/LukasMG/Lokaverkefni-VESM3/blob/main/Lokaverkefni%20VESM-3/mynd/kassi2.png)

![kassi 3](https://github.com/LukasMG/Lokaverkefni-VESM3/blob/main/Lokaverkefni%20VESM-3/mynd/kassi3.png)

## Hönnurnar skjöl

[Hér](https://github.com/LukasMG/Lokaverkefni-VESM3/tree/main/Lokaverkefni%20VESM-3/stl%20files) er slóð á möppuna með hönnurnar skjölunum, semsagt sjálfsalinn

## Heimildir

https://dronebotworkshop.com/esp32-servo/

https://esp32io.com/tutorials/esp32-keypad

https://www.aranacorp.com/en/using-an-rfid-module-with-an-esp32/

https://www.instructables.com/ESP32-With-RFID-Access-Control/
