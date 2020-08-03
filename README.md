# Tapahtumabudjetti
Tsoha 2020 -harjoitustyö

## Heroku
Sovellusta voi testata Herokussa: https://tapahtumabudjetti.herokuapp.com/.

Testatessa kannattaa rekisteröidä itselle oma testikäyttäjä ja luoda tällä testikäyttäjällä uusi tapahtuma.
Näin pääsee testaamaan sekä tapahtuman järjestäjän ominaisuuksia (omassa tapahtumassa) että muiden käyttäjien tapahtumien käyttäytymistä.
Herokussa on ainakin käyttäjän Salla tapahtumia jo pari testimielessä.

## Sovelluksen tarkoitus
Sovellus on tarkoitettu tilanteeseen, jossa joukko ihmisiä järjestää tapahtumaa. Sovellus sopii esimerkiksi suurten juhlien tai järjestötapahtumien järjestäjäjoukoille.
Sovelluksen avulla voi budjetoida koko tapahtuman ja sen osa-alueet (esim. ruoka, koristelu, ohjelma) sekä seurata toteutuneita maksuja käyttäjittäin ja osa-alueittain.
Sovelluksella voi siis seurata, pysyvätkö suuren tapahtuman osaprojektit tai koko tapahtuma suunnitelluissa budjeteissaan, sekä tarkkailla maksun tarkkuudella, kuinka paljon kukin käyttäjä on maksanut tapahtuman kuluja, mihin osaprojekteihin maksut liittyvät jne. 
Lisäksi maksut kategorisoidaan tarvittaessa erikseen seurattaviin kulukategorioihin (esim. varausmaksu, käteiskassan maksu, kuititon kulu), ja maksuja voi tarkastella näistä kategorioista käsin.

## Taulut, suunnitelma
* Käyttäjä - Sovelluksen käyttäjän tiedot
* Maksu - Maksutapahtumat
* Tapahtuma - Tapahtuma, johon maksu liittyy
* Osa-alue - Kertoo, mihin tapahtuman osa-alueeseen maksu kuuluu. Joka osa-alueella on määritelty budjetti.
* Maksukategoria - Kirjanpitoa varten, maksun voi merkitä esimerkiksi varausmaksuksi tai käteiskassan maksuksi.
* Liitostaulu Maksu<>Maksukategoria - Tarpeellinen, koska maksu voi kuulua moneen kategoriaan tarpeen mukaan.

## Toiminnallisuuksia, alustava suunnitelma
* Osaprojektin maksimibudjetin ja osaprojektiin liitettyjen toteutuneiden maksujen summien vertaaminen, tieto budjetin alituksesta tai ylityksestä
* Koko tapahtuman kuluarvion (osaprojektien maksimisummien summa) vertaaminen kaikkiin toteutuneisiin maksutapahtumiin
* Maksujen haku tietyltä päivältä tai ennen tai jälkeen tietyn päivän (esim. ennen tai jälkeen tapahtuman)
* Tietyn kulukategorian maksujen seuraaminen
* Mahdollisesti toteutettava: syötetyn maksun tietojen muokkaaminen (voisi olla näppärä?)
* Käyttäjän maksaman kokonaissumman tarkistaminen
* Maksujen määrien ja maksettujen summien jakaantuminen käyttäjittäin

## Kehityksen tilanne
Ohjelmalle on nyt toteutettu runkoa, hyvin perustason ominaisuuksia ja mm. koko kannan rakenne on jo tiedostossa schema.sql (toki voi tulla viilauksia vielä).
Viikkopalautteen perusteella on nyt käännetty koodi ja tietokanta englanniksi.
Tähän mennessä on tehty kirjautuminen ja tapahtumat-taulun uusien tapahtumien lisääminen siten, että jokainen tapahtuma liittyy sen luoneeseen käyttäjään.
Ohjelman käyttöliittymässä taas on luotu tapahtumien listaus, josta pääsee tarkastelemaan kullekin tapahtumalle id:n perusteella generoituvaa omaa sivua, sekä uuden tapahtuman lisäyslomake.

Tiivistetysti: kirjautumaton käyttäjä voi ohjelman tämänhetkisessä versiossa
* kirjautua sisään
* rekisteröityä.

Kirjautunut käyttäjä puolestaan voi
* tarkastella tapahtumalistaa
* tarkastella kaikkien tapahtumien tietoja, osaprojekteja ja maksukategorioita niiden omilla tapahtumasivuilla
* lisätä tapahtuman (jolloin rooliksi tulee tapahtuman järjestäjä)
* lisätä tapahtumaan, jonka järjestäjä on, osaprojekteja ja muokata niihin budjetoituja summia
* lisätä tapahtumaan, jonka järjestäjä on, maksukategorioita
* lisätä maksun kenen tahansa järjestämään tapahtumaan
* kirjautua ulos.

Maksun lisäyksessä havaitut ongelmat, jotka korjataan seuraavaksi: maksun voi syöttää ainoastaan kokonaislukuna, vaikka pitäisi olla desimaalit. Maksuun ei voi lisätä kommenttia.
Näiden korjauksen jälkeen toteutetaan maksujen listaus.

Lähiaikoina voisi listata etusivun projektilistauksessa erikseen käyttäjän mukaan omat tapahtumat ja muut tapahtumat.
Myöhemmin lisätään ominaisuus, että jo lisätyn maksun tietoja voi muokata tai maksun voi poistaa joko tapahtuman järjestäjä tai maksun lisääjä.
Myöhemmin lisätään myös erilaisten yhteenvetokyselyiden tekeminen kunkin tapahtuman sivulla.
