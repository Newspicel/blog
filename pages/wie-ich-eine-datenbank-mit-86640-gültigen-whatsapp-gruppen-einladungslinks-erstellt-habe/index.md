# Wie ich eine Datenbank mit 86640 gültigen WhatsApp Gruppen Einladungslinks erstellt habe.
<!-- date: 2021-05-30 14:00:00 -->
<!-- category: data-science -->
<!-- description: Mein erster Beitrag und gleichzeit eine kleine Beschreibung von Whatsapp Gruppen Einladungslinks -->
Willkommen zu meinem ersten Beitrag, in diesem Beitrag gehe ich darauf ein wie einfach es ist selbiges zu tun. Und wie man so an Hundert Tausende gültige Nummern kommen könnte. Und wie man das theoretisch auch mit anderen Diensten wie Discord anfangen könnte.

## Wie ich auf diese Idee kam:

Auf die Idee kam ich schon vor längerem. Lass es fast zwei Jahre her sein, nur ich habe mir nie die Zeit genommen das schnell auf zusetzten. Auf jeden fall bin ich vor kurzem wieder auf das Projekt gestoßen und habe mir überlegt das ich es jetzt einfach Anfange. Man muss dazu sagen: Es war nicht besonders aufwendig, ich war nach ein paar Stunden fertig. 

Also, wie kam ich auf die Idee: Recht Simple, ich habe einen Tweet übers Web Archive gesehen und bin auf die Idee gekommen einfach nach _chat.whatsapp.com/* _im Web Archive zu suchen. Und so kriegt man eine Liste mit ungefähr 0.8 Millionen Links. Wie habe ich nun die ~86000 gültige Links daraus bekommen.

## Das erste Programm: Der Downloader

Das erste Programm was ich dazu geschrieben habe ist der Downloader. Dieser lädt sich die Links vom Webarchive runter und überprüft sie schonmal Lokal auf Dopplungen. Filtert Parameter der URL und nimmt sich den Key raus und speichert diesen in der Datenbank. Das ist im groben und ganzen schon alles für dieses Programm.

## Das zweite Programm: Der Überprüfer

Beim zweiten Programm habe ich mir vorher etwas Kopfschmerzen gemacht, am Ende war es aber deutlich einfach als ich gedacht hätte. Wie funktioniert mein Programm nun: Ich stelle eine Anfrage an chat.whatsapp.com/<KEY> und frage ganz simple ab ob der Name vorhanden ist und wen ja, speichere ich den Key mit dem Namen in einer neuen Tabelle in meiner Datenbank. Das macht WhatsApp mir hier echt einfach, da ich nicht mal über Proxys oder sonstiges gehen musste, da diese Webseite von WhatsApp meines Wissenstandes kein Limit hat, da ich am Ende bei ungefähr 150-200 Anfragen pro Sekunde war. 

Ungültiger WhatsApp Invite Link: 

<p><img src="https://i.newspicel.dev/data/B8taGHXNK419xcYRZ9TsBCoc3MiHz7Qz.png" width="680" height="324" alt=""></p>

Gültiger WhatsApp Invite Link:

<p><img src="https://i.newspicel.dev/data/TB8kR7Ip2DN8l73AvbPc2Yg3cuDX7cRq.png" width="698" height="350" alt=""></p>

## Noch ein paar andere Infos:

Ich habe das ganze Programm in Java geschrieben, einfach weil ich mich damit am besten auskenne. Und für die Datenbank habe ich RethinkDB benutzt aus dem selbigen Grund. 

## Analyse: 

Was ich mit den ganzen Links und Namen anstellen will: Ich will in der Zukunft noch ein kleines Programm schreiben was die Links durchschaut und in Kategorien einteilt, den nachdem ich mir die ersten Links angeschaut habe ist mir aufgefallen das sicherlich 1/5 allein Pornografische Inhalte sind. Und ein anderer fünftel allein Gruppen im Bereich von schnell Reich werden, BTC, Trading und so weiter sind. Diese Analyse werde ich aber in einem kommenden Blogartikel genauer machen. 

## Problematik:

Wir selber sind in den Unterschiedlichsten Gruppen gelandet: Von Klassen Gruppen, über Gruppen von Firmen Mitarbeitern, über einfache Gruppe die nur Notizen hießen, zu Gruppen wo nur scheiße gemacht wurde. Trotzdem könnten wir für alle diese Gruppen Requests an WhatsApp schicken und somit Hundert Tausende an gültigen Nummern speichern und diese für die Unterschiedlichsten Dinge ausnutzen. 

Aber wen man mit einem Account Requests an WhatsApp schickt verstoßt man dann gegen die AGBs und das kann dann zu einer Sperrung des Accounts führen.

## Schlusswort: 

Jeder der diese Links für etwas sinnvolles benutzen will kann mich gerne anschreiben und dann gebe ich die natürlich weiter. Und sonnst kann man noch dazu sagen das dies nicht nur mit WhatsApp möglich ist. Das genau gleiche System kann man auch bei z.b. Discord benutzen. 

Zusätzlich ist noch zu sagen das Web Archive sammelt nicht jeden Link weswegen ich auch nicht an jede Einladung die es gibt kommen kann. Das könnte man wohl nur durch Bruteforce erreichen.