# Tapahtumabudjetti
Tsoha 2020 -harjoitustyö

## Sovelluksen tarkoitus
Sovellus on tarkoitettu tilanteeseen, jossa joukko ihmisiä järjestää tapahtumaa. Sovellus sopii esimerkiksi suurten juhlien tai järjestötapahtumien järjestäjäjoukoille.
Sovelluksen avulla voi budjetoida koko tapahtuman ja sen osa-alueet (esim. ruoka, koristelu, ohjelma) sekä seurata toteutuneita maksuja käyttäjittäin ja osa-alueittain.
Sovelluksella voi siis seurata, pysyvätkö suuren tapahtuman osaprojektit tai koko tapahtuma suunnitelluissa budjeteissaan, sekä tarkkailla maksun tarkkuudella, kuinka paljon kukin käyttäjä on maksanut tapahtuman kuluja, mihin osaprojekteihin maksut liittyvät jne. 
Lisäksi maksut kategorisoidaan tarvittaessa erikseen seurattaviin kulukategorioihin (esim. varausmaksu, käteiskassan maksu, kuititon kulu), ja maksuja voi tarkastella näistä kategorioista käsin.

## Taulut, alustava suunnitelma
* Käyttäjä - Sovelluksen käyttäjän tiedot
* Maksu - Maksutapahtumat
* Osa-alue - Kertoo, mihin juhlan osa-alueeseen maksu kuuluu. Joka osa-alueella on määritelty budjetti.
* Maksukategoria - Kirjanpitoa varten, maksun voi merkitä esimerkiksi varausmaksuksi tai käteiskassan maksuksi.
* Liitostaulu Maksu<>Osa-alue - Joka osa-alueesta vastaa yksi tai useampi käyttäjä, ja tätä kautta voi selvittää keneen voi olla yhteydessä siitä
* Liitostaulu Maksu<>Maksukategoria - Maksu voi kuulua moneen kategoriaan tarpeen mukaan.

## Toiminnallisuuksia, alustava suunnitelma
* Käyttäjän maksaman kokonaissumman tarkistaminen
* Maksujen määrien ja maksettujen summien jakaantuminen käyttäjittäin
* Osaprojektin maksimibudjetin ja osaprojektiin liitettyjen toteutuneiden maksujen summien vertaaminen, tieto budjetin alituksesta tai ylityksestä
* Koko tapahtuman kuluarvion (osaprojektien maksimisummien summa) vertaaminen kaikkiin toteutuneisiin maksutapahtumiin
* Maksujen haku tietyltä päivältä tai ennen tai jälkeen tietyn päivän (esim. ennen tai jälkeen tapahtuman)
* Tietyn kulukategorian maksujen seuraaminen
* Mahdollisesti toteutettava: syötetyn maksun tietojen muokkaaminen (voisi olla näppärä?)

## Suunniteltu kehitysjärjestys
Aluksi toteutetaan maksu-taulu ja maksujen syöttäminen. Tämän jälkeen toteutetaan käyttäjä-taulu ja kirjautuminen, mahdollistetaan maksun syöttäminen vain kirjautuneelle ja yhdistetään kukin syötetty maksu käyttäjään.
Tämän jälkeen kehitetään maksujen listaus- ja hakunäkymät, joissa aluksi rajatut toiminnallisuudet. 
Näkymän valmistuttua toteutetaan osa-alue- ja maksukategoria-taulut ja yhdistetään niiden toiminnallisuudet sovellukseen.
Viimeiseksi viimeistellään toiminnallisuudet, kuten kaikkia tauluja hyödyntävät haut, ja sovelluksen ulkoasu. 
