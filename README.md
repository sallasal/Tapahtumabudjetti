# Tapahtumabudjetti
Tsoha 2020 -harjoitustyö

##Sovelluksen tarkoitus
Sovellus on tarkoitettu tilanteeseen, jossa joukko ihmisiä järjestää tapahtumaa. Sovellus sopii esimerkiksi suurten juhlien tai järjestötapahtumien järjestäjäjoukoille.
Sovelluksen avulla voi budjetoida koko tapahtuman ja sen osa-alueet (esim. ruoka, koristelu, ohjelma) sekä seurata toteutuneita maksuja käyttäjittäin ja osa-alueittain.
Sovelluksella voi siis seurata, pysyvätkö suuren tapahtuman osaprojektit tai koko tapahtuma suunnitelluissa budjeteissaan, sekä tarkkailla maksun tarkkuudella, kuinka paljon kukin käyttäjä on maksanut tapahtuman kuluja, mihin osaprojekteihin maksut liittyvät jne. 
Lisäksi maksut kategorisoidaan tarvittaessa erikseen seurattaviin kulukategorioihin (esim. varausmaksu, käteiskassan maksu, kuititon kulu), ja maksuja voi tarkastella näistä kategorioista käsin.

##Taulut, alustava suunnitelma
* Käyttäjä - Sovelluksen käyttäjän tiedot
* Maksu - Maksutapahtumat
* Osa-alue - Kertoo, mihin juhlan osa-alueeseen maksu kuuluu. Joka osa-alueella on määritelty budjetti.
* Maksukategoria - Kirjanpitoa varten, maksun voi merkitä esimerkiksi varausmaksuksi tai käteiskassan maksuksi.
* Liitostaulu Maksu<>Osa-alue - Joka osa-alueesta vastaa yksi tai useampi käyttäjä, ja tätä kautta voi selvittää keneen voi olla yhteydessä siitä
* Liitostaulu Maksu<>Maksukategoria - Maksu voi kuulua moneen kategoriaan tarpeen mukaan.

##Toiminnallisuuksia, alustava suunnitelma
