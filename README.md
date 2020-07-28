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
* Tapahtuma - Tapahtuma, johon maksu liittyy
* Osa-alue - Kertoo, mihin tapahtuman osa-alueeseen maksu kuuluu. Joka osa-alueella on määritelty budjetti.
* Maksukategoria - Kirjanpitoa varten, maksun voi merkitä esimerkiksi varausmaksuksi tai käteiskassan maksuksi.
* Liitostaulu Maksu<>Maksukategoria - Jos päädytään siihen, että maksu voi kuulua moneen kategoriaan tarpeen mukaan.

## Toiminnallisuuksia, alustava suunnitelma
* Käyttäjän maksaman kokonaissumman tarkistaminen
* Maksujen määrien ja maksettujen summien jakaantuminen käyttäjittäin
* Osaprojektin maksimibudjetin ja osaprojektiin liitettyjen toteutuneiden maksujen summien vertaaminen, tieto budjetin alituksesta tai ylityksestä
* Koko tapahtuman kuluarvion (osaprojektien maksimisummien summa) vertaaminen kaikkiin toteutuneisiin maksutapahtumiin
* Maksujen haku tietyltä päivältä tai ennen tai jälkeen tietyn päivän (esim. ennen tai jälkeen tapahtuman)
* Tietyn kulukategorian maksujen seuraaminen
* Mahdollisesti toteutettava: syötetyn maksun tietojen muokkaaminen (voisi olla näppärä?)

## Kehityksen tilanne
Ohjelmalle on nyt toteutettu runkoa, hyvin perustason ominaisuuksia ja mm. koko kannan rakenne on jo tiedostossa schema.sql (toki voi tulla viilauksia vielä).
Tähän mennessä on tehty kirjautuminen ja tapahtumat-taulun uusien tapahtumien lisääminen siten, että jokainen tapahtuma liittyy sen luoneeseen käyttäjään.
Ohjelman käyttöliittymässä taas on luotu tapahtumien listaus, josta pääsee tarkastelemaan kullekin tapahtumalle id:n perusteella generoituvaa omaa sivua, sekä uuden tapahtuman lisäyslomake.

Tiivistetysti: kirjautumaton käyttäjä voi ohjelman tämänhetkisessä versiossa
* kirjautua sisään
* rekisteröityä.

Kirjautunut käyttäjä puolestaan voi
* tarkastella tapahtumalistaa
* tarkastella kunkin tapahtuman tietoja omalla sivullaan
* lisätä tapahtuman
* kirjautua ulos.

Tämän jälkeen mahdollistetaan osa-alueiden ja niiden budjettien lisääminen, muokkaaminen, listaaminen ja poistaminen tapahtuman alla.
Sitten kannattaa varmaan tehdä maksukategorioiden lisääminen ja listaus, ja viimeisenä eniten riippuvuuksia sisältävä eli maksutapahtuman lisääminen, muokkaus ja listaus.

Aivan viimeiseksi jää sitten erilaisten yhteenvetokyselyiden tekeminen kunkin tapahtuman sivulla.
