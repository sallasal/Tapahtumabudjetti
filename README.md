# Tapahtumabudjetti
Tsoha 2020 -harjoitustyö

## Heroku
Sovellusta voi testata Herokussa: https://tapahtumabudjetti.herokuapp.com/.

TESTIVERSION TIETOKANTA ON TYHJENNETTY 23.8., eli kaikki tätä ennen luodut käyttäjät, tapahtumat ym. on poistettu.

Testatessa kannattaa rekisteröidä itselle oma testikäyttäjä ja luoda tällä testikäyttäjällä uusi tapahtuma.
Näin pääsee testaamaan rekisteröitymistä, tapahtuman järjestäjän ominaisuuksia (omassa tapahtumassa) ja muiden käyttäjien tapahtumien käyttäytymistä.

Sovelluksessa on jo käyttäjien Salla ja Eemeli luomia tapahtumia ja maksuja. Eemelin tiliä voi mennä katselemaan tunnuksilla Eemeli - testieemeli. 
(Eemelin tapahtumassa on jo aika paljon maksuja ym., niin saa ehkä paremman kuvan.)

# Vaatimukset ja laitteet

Sovelluksen käyttämät kirjastot on listattu tiedostossa requirements.txt.

Sovellus toimii myös mobiilissa.

## Sovelluksen tarkoitus
Sovellus on tarkoitettu tilanteeseen, jossa joukko ihmisiä järjestää tapahtumaa. Sovellus sopii esimerkiksi suurten juhlien tai järjestötapahtumien järjestäjäjoukoille.
Sovelluksen avulla voi budjetoida koko tapahtuman ja sen osa-alueet (esim. ruoka, koristelu, ohjelma) sekä seurata toteutuneita maksuja käyttäjittäin ja osa-alueittain.
Sovelluksella voi siis seurata, pysyvätkö suuren tapahtuman osaprojektit tai koko tapahtuma suunnitelluissa budjeteissaan, sekä tarkkailla maksun tarkkuudella, kuinka paljon kukin käyttäjä on maksanut tapahtuman kuluja, mihin osaprojekteihin maksut liittyvät jne. 
Lisäksi maksut kategorisoidaan tarvittaessa erikseen seurattaviin kulukategorioihin (esim. varausmaksu, käteiskassan maksu, kuititon kulu), ja maksuja voi tarkastella näistä kategorioista käsin.

## Kehityksen tilanne
Sovelluksen taulut ja lisäystoiminnallisuudet on toteutettu. Kirjautuminen on toteutettu ja sovellus näyttää erilaiselta kullekin kirjautuneelle käyttäjälle. Tiedonhakua monipuolistetaan vielä paljon.

Tiivistetysti: kirjautumaton käyttäjä voi ohjelman tämänhetkisessä versiossa
* kirjautua sisään
* rekisteröityä.

Kirjautunut käyttäjä puolestaan voi
* tarkastella tapahtumalistaa ryhmiteltynä käyttäjän omiin ja muiden järjestämiin tapahtumiin
* tarkastella kaikkien tapahtumien tietoja, osaprojekteja ja tapahtumia niiden omilla tapahtumasivuilla
* tarkastella kaikkien tapahtumien maksuja tapahtumasivulla ryhmiteltynä käyttäjän omiin ja muiden käyttäjien maksuihin
* lisätä tapahtuman (jolloin rooliksi tulee tapahtuman järjestäjä)
* lisätä tapahtumaan, jonka järjestäjä on, osaprojekteja ja muokata niihin budjetoituja summia
* lisätä tapahtumaan, jonka järjestäjä on, maksukategorioita
* lisätä maksun kenen tahansa järjestämään tapahtumaan
* poistaa omia maksujaan mistä tahansa tapahtumasta
* nähdä tapahtumasivulla tapahtumaan budjetoidun kokonaissumman sekä tähän mennessä tapahtuman maksuista kertyneen summan
* verrata osaprojektin maksimibudjettia ja tähän mennessä syötettyjen maksujen summaa sekä nähdä tiedon budjetin alituksesta tai ylityksestä.
* listata tapahtuman, jonka järjestäjä on, maksut osa-alueittain ja tarkastella niitä.
* listata tapahtuman, jonka järjestäjä on, maksut maksukategorioittain ja tarkastella niitä.
* listata kaikki oman tapahtuman maksut päivämäärän mukaan nousevasti ja laskevasti
* listata kaikki oman tapahtuman maksut ennen ja jälkeen määrittelemänsä päivämäärän
* poistaa omasta tapahtumasta kaikkien maksujen yhteenvedoissa minkä tahansa maksun
* kirjautua ulos.

Lisäillään vielä kokonaissummia sekä erilaisia yhteenvetomahdollisuuksia tapahtuman järjestäjälle.

# Myöhempiä laajennusmahdollisuuksia
Sovellus toimii suurin piirtein tällaisenaan esimerkiksi ainejärjestön tai muun yhden tapahtumia järjestävän joukon sisällä. 
Jos käyttäjäkunta olisi useampi erillinen järjestäjäjoukko, sovelluksen käyttäjänhallintaa voisi kehittää vielä niin, että kullekin tapahtumalle määritetään järjestäjäjoukko, jota hallinnoi järjestäjä.
Tällöin vain järjestäjäjoukko näkisi tapahtuman tiedot.
