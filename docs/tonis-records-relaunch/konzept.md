# Website-Relaunch — Toni's Records

**Leitmotiv:** *„Bewahre die Seele von Toni's Records. Modernisiere das Erscheinungsbild."*

> **Hinweis zur Grundlage dieses Konzepts:** Die bestehende Seite `www.tonis-records.de` war aus dieser Arbeitsumgebung heraus nicht erreichbar (Netzwerkzugriff blockiert) und ließ sich auch über eine Websuche nicht auffinden. Dieses Konzept wurde daher auf Basis der im Auftrag beschriebenen Charakteristik erstellt — traditionsreicher, liebevoll geführter Schallplattenladen, Sammlerkultur, gewachsene Markenidentität. Alle markenspezifischen Fakten (Gründungsjahr, Standort, Slogan, Logo-Details, Fotos, Sortiment) stehen als **`[Platzhalter]`** und sind vor Umsetzung mit den echten Inhalten und einer Analyse der bestehenden Seite abzugleichen. Das Konzept ist so aufgebaut, dass die Platzhalter 1:1 gegen die realen Marken-Assets getauscht werden können, ohne Struktur oder Gestaltung zu ändern.

Visuelle Ausarbeitung (Moodboard, Desktop- und Mobile-Wireframe der Startseite):
**[Design-Canvas „Toni's Records Relaunch"](https://claude.ai/code/artifact/24f93222-762e-4c92-bf75-e86bca2fd7db)**

---

## 1. Designkonzept

### Leitidee
Ein traditionsreicher Plattenladen wird für die Gegenwart neu gestaltet — Besucher:innen sollen auf den ersten Blick erkennen: *das ist immer noch Toni's Records*, nur aufgeräumter, hochwertiger, professioneller. Die Gestaltung übersetzt drei bestehende Werte in zeitgemäße Mittel:

| Bestehender Wert | Modernes Gestaltungsmittel |
|---|---|
| Analoge Wärme, Retro-Charme | Warme, papierartige Grundfarbe statt reinweiß; Vinyl-Schwarz statt reinschwarz |
| Handwerk & Sammlerkultur | Großformatige, ehrliche Fotografie (Rillen, Kisten, Ladenalltag) statt Stock-Bildsprache |
| Gewachsene, persönliche Marke | Emblem/Logo bleibt inhaltlich (Tonarm- und Vinyl-Motiv), wird nur sauberer gezeichnet |

### Farbpalette
Warme, analoge Grundtöne statt neutralem Grau/Weiß — bewusst **nicht** die generische SaaS-Palette (kein reines Weiß, kein Techno-Blau):

| Farbe | Hex | Verwendung |
|---|---|---|
| Vinyl-Schwarz | `#1B1613` | Textfarbe, dunkle Flächen (Header/Footer, Story-Sektion) |
| Analog-Creme | `#F7F2E6` | Seitenhintergrund — warmer Papierton statt Reinweiß |
| Creme-2 (Kartenflächen) | `#EFE6D2` | Kartenhintergründe, Trennflächen |
| Label-Gold | `#C9762F` | Primärakzent — CTAs, Hervorhebungen, Links |
| Sleeve-Rot | `#9B3826` | Sekundärakzent — Sale, Ankauf-Banner, Betonung |
| Retro-Teal | `#2E6B66` | Tertiärakzent, **sparsam** — Electronic-Kachel, Auflockerung |

Die drei Akzentfarben sind bewusst in ähnlicher Helligkeit/Sättigung gehalten und unterscheiden sich primär im Farbton — das wirkt wie eine kuratierte Plattencover-Palette, nicht wie zufällig gewählte Bunttöne.

### Typografie
Zwei Schriften, klare Hierarchie:

- **Headlines:** *Bricolage Grotesque*, Bold/Extrabold — ein charaktervoller, leicht eigenwilliger Grotesk mit Ecken, der an Schallplatten-Label-Typografie erinnert, ohne in Retro-Kitsch (Schreibschrift, Western-Serifen) zu verfallen.
- **Fließtext/UI:** *Archivo*, Regular/Medium/Bold — sehr gut lesbar, neutral genug, um im Alltag nicht zu ermüden.

Beide sind über Google Fonts frei verfügbar, performant einbindbar und decken alle nötigen Schnitte ab.

### Bildsprache
Vier wiederkehrende Motivarten, alle mit warmem, natürlichem Licht (kein cleanes Studiolicht, keine Stockfotografie):

1. **Rillen-Makro** — Nahaufnahme der Vinyl-Rille im Streiflicht
2. **Krate-Wühlen** — Hände beim Durchblättern von Plattenkisten, Bewegung und Haptik
3. **Ladenporträt** — Toni bzw. das Team im Laden, ehrlich statt gestellt
4. **Vinyl-Label-Detail** — Nahaufnahme bedruckter Labels, Typografie und Farbigkeit

Diese vier Motive ziehen sich durch Hero, Story-Teaser und Marketing-Flächen und ersetzen Produktfotos-auf-weißem-Grund als alleinige Bildsprache.

### Logo/Emblem
Das bestehende Motiv (Tonarm, Rille, Label) bleibt als Kernidee erhalten, wird aber:
- **reduziert und linienbasiert** neu gezeichnet (statt mit Farbverläufen/Schatten),
- **einfarbig druckbar**, damit es auf Tüten, Aufklebern, Schaufenster funktioniert,
- **skalierbar** vom 16×16-Favicon bis zum Ladenschild, ohne Details zu verlieren.

Ein kompaktes Monogramm (Rille + Tonarm) dient als App-Icon/Favicon, die volle Wortmarke „Toni's Records" für Header und Signaturen.

---

## 2. Moderne Sitemap

```
Startseite
├── Shop
│   ├── Alle Platten (Filter: Genre, Format LP/12"/7", Zustand neu/gebraucht, Preis, Label)
│   ├── Genres (Rock, Jazz, Soul, Electronic, Hip-Hop, Klassik, …)
│   ├── Neuheiten
│   ├── Second Hand
│   └── Sale
├── Second Hand & Ankauf
│   ├── So funktioniert der Ankauf
│   └── Ankauf-Anfrage (Formular)
├── Events
│   ├── Kommende Termine (In-Store-DJ-Sets, Record Store Day, Workshops)
│   └── Rückblick / Archiv
├── Über uns
│   ├── Unsere Geschichte
│   ├── Team
│   └── Presse (optional)
├── Magazin/Blog (optional, falls redaktionell gepflegt)
│   └── Genre-Guides, Pflegetipps, Neuvorstellungen
├── Kontakt & Anfahrt
├── Konto
│   ├── Bestellungen
│   ├── Wunschliste
│   └── Verkaufte Sammlungen (Ankauf-Historie)
└── Footer (auf jeder Seite)
    ├── Versand & Rückgabe
    ├── FAQ
    ├── Newsletter
    ├── Social Media
    └── Rechtliches (Impressum, Datenschutz, AGB)
```

**Warum diese Struktur:** Die drei zentralen Besuchsgründe — *kaufen*, *verkaufen*, *dabei sein* (Events) — stehen gleichrangig in der Hauptnavigation, statt in Untermenüs zu verschwinden. „Second Hand & Ankauf" ist bewusst ein eigener Hauptpunkt, weil Ankauf bei Sammler:innen ein eigenständiges, vertrauensrelevantes Thema ist (siehe Abschnitt 4).

---

## 3. Startseiten-Vorschlag

Reihenfolge und Inhalt der Startseite (siehe Wireframe im Design-Canvas):

1. **Sticky Header** — Logo, Hauptnavigation, Suche, Konto, Warenkorb. Bleibt beim Scrollen sichtbar, dezenter Schlagschatten sobald gescrollt wird.
2. **Hero** — großformatige, stimmungsvolle Fotofläche (Ladenlicht/Krate), Wortmarke, ein kurzer emotionaler Claim (*„Musik zum Anfassen."*, Platzhalter), zwei klar gewichtete CTAs: primär „Jetzt stöbern", sekundär „Unsere Geschichte".
3. **Genre-Kacheln** — visuelle Einstiegsnavigation in die wichtigsten Genres, große Klickflächen statt Dropdown-Menü.
4. **„Frisch reingekommen"** — horizontal scrollbare, aktuelle Ware; schafft Aktualität und Wiederkehr-Anreiz.
5. **Story-Teaser** — ganzflächiges Foto + kurzer, persönlicher Text aus Tonis Geschichte, Link zu „Über uns". Transportiert die Identität, ohne die Startseite mit Fließtext zu überladen.
6. **„Toni's Pick der Woche"** — eine einzelne, redaktionell kuratierte Empfehlung mit kurzer Begründung. Menschliche Kuration als Differenzierung gegenüber Streaming-Algorithmen.
7. **Second-Hand/Ankauf-Banner** — eigenständige, farblich abgesetzte Fläche, die Ankauf aktiv bewirbt (wichtige Einnahmequelle & Vertrauenssignal für Sammler:innen).
8. **Events-Teaser** — die nächsten 2–3 Termine.
9. **Newsletter-Signup** — niedrigschwellig, ein Feld.
10. **Footer** — Shop/Service/Über uns/Social/Rechtliches, sauber in Spalten.

---

## 4. Modernisierungsvorschläge pro Bestandselement

Da die Live-Seite nicht einsehbar war, sind die „Ist"-Spalten typische Symptome gewachsener, seit Jahren nicht überarbeiteter Plattenladen-Websites — **bitte gegen die tatsächliche Seite abgleichen**, bevor priorisiert wird.

| Element | Typischer Ist-Zustand | Modernisierungsvorschlag | Begründung |
|---|---|---|---|
| Hauptnavigation | Viele Menüpunkte, tiefe Untermenüs, uneinheitliche Benennung | Sechs klare Hauptpunkte (Shop, Neuheiten, Second Hand/Ankauf, Events, Über uns, Kontakt), Filter statt Untermenüs im Shop | Reduziert kognitive Last, macht Kernangebote sofort sichtbar |
| Startseite | Viele kleine Banner/Module untereinander, unterschiedliche Bildformate | Klare Abschnittsfolge mit einheitlichem Raster, ein dominantes Hero-Bild statt Banner-Karussell | Karussells werden kaum vollständig gesehen; ein starkes Bild wirkt hochwertiger |
| Produktlisten | Kleine Cover-Thumbnails, viel Text/Metadaten auf einmal | Große, quadratische Cover, reduzierte Metadaten (Titel, Künstler:in, Preis), Details erst auf der Produktseite | Vinyl ist ein visuelles Produkt — das Cover verkauft mit |
| Schrift & Farben | Oft reines Schwarz/Weiß plus eine grelle Akzentfarbe, viele Schriftschnitte gemischt | Warme Grundpalette (Creme/Vinyl-Schwarz) mit zwei kuratierten Schriften | Wirkt hochwertiger, weniger „gebastelt", ohne die Retro-Anmutung zu verlieren |
| Logo/Emblem | Als Rastergrafik mit Verlauf/Schatten eingebunden, in klein unscharf | Als Vektor (SVG) neu gezeichnet, linienbasiert, einfarbig druckbar | Skaliert verlustfrei vom Favicon bis zum Schaufenster |
| Second-Hand/Ankauf | Meist als Unterseite versteckt oder nur als Kontaktformular ohne Kontext | Eigener Hauptnavigationspunkt, klarer Ablauf erklärt, prominenter Banner auf der Startseite | Ankauf ist für Sammler:innen ein Vertrauensthema und oft eine wichtige Einnahmequelle — verdient Sichtbarkeit |
| Mobile Darstellung | Desktop-Layout „zusammengequetscht", kleine Klickflächen, horizontales Scrollen nötig | Eigenständiges, thumb-freundliches Mobile-Layout (siehe Wireframe), horizontal scrollbare Produktreihen statt Tabellen | Der Großteil des Traffics ist heute mobil; kleine Tippflächen kosten Umsatz |
| Ladezeiten | Unkomprimierte Originalfotos, viele externe Skripte/Plugins | Optimierte, responsive Bildformate (WebP/AVIF), schlanke technische Basis | Schnelle Ladezeit ist direkter Ranking- und Conversion-Faktor |
| Geschichte/„Über uns" | Oft ein einzelner Textblock ohne Bild, oder ganz fehlend | Eigene, bebilderte Seite plus Teaser auf der Startseite | Die Geschichte ist das stärkste Differenzierungsmerkmal gegenüber Online-Marktplätzen |
| Barrierefreiheit | Geringer Textkontrast auf Bildern, fehlende Alt-Texte, kleine Schrift | Kontrastgeprüfte Farbpaare, konsequente Alt-Texte, Mindestschriftgröße 16px | Gesetzlich zunehmend relevant (BFSG) und erschließt mehr Kundschaft |

---

## 5. Was bleibt erhalten — und warum

Bewusst **nicht** verändert werden sollen:

- **Das Logo-/Emblem-Motiv** (Tonarm, Rille, Label) — es ist der visuelle Anker, an dem Stammkundschaft die Marke wiedererkennt. Nur die Ausführung (Vektor statt Raster, reduzierte Linienführung) wird modernisiert, nicht die Idee.
- **Der Name und Namenszug „Toni's Records"** samt der persönlichen, inhaberbezogenen Note — das unterscheidet den Laden von anonymen Online-Plattformen und ist Kern der Markenidentität.
- **Die warme, analoge Farbanmutung** — statt auf ein neutrales, generisches Weiß/Grau umzustellen (wie es viele „moderne" Relaunches tun), bleibt der Grundton warm und papierartig. Das erhält den Retro-Charakter, während Layout und Typografie modernisiert werden.
- **Die persönliche Kuration** („Toni's Pick der Woche", Story-Teaser) — Empfehlungen aus persönlicher Expertise sind ein Alleinstellungsmerkmal gegenüber Streaming-Algorithmen und sollten nicht wegrationalisiert werden.
- **Second-Hand/Ankauf als Kernangebot** — falls dies bereits heute ein tragendes Element des Ladens ist, wird es in der neuen Struktur nicht nur beibehalten, sondern durch einen eigenen Navigationspunkt aufgewertet.

Verändert werden dagegen konsequent: Layout-Dichte, Bildqualität/-führung, Schriftmischung, Navigationstiefe, mobile Nutzbarkeit und technische Performance — also alles, was die *Wahrnehmung* der Marke unnötig alt wirken lässt, ohne zur *Identität* zu gehören.

---

## 6. Technische Anforderungen (Umsetzungsleitplanken)

- **SEO-Struktur:** sprechende URLs (`/shop/jazz`, `/second-hand/ankauf`), eine `<h1>` pro Seite, strukturierte Daten (`Product`, `LocalBusiness`) für Google Shopping/Local-Sichtbarkeit.
- **Performance:** responsive Bildformate (WebP/AVIF mit Fallback), Lazy Loading unterhalb des Folds, schlanke JS-Basis ohne unnötige Drittanbieter-Skripte.
- **Barrierearmut:** Kontrastverhältnisse nach WCAG AA prüfen (insbesondere Text auf den Akzentfarben Label-Gold/Sleeve-Rot), konsequente Alt-Texte für Produktfotos, Tastaturbedienbarkeit der Navigation.
- **Zukunftsfähige Architektur:** Trennung von Content (Shop-Katalog, Events, Blog) und Layout, damit Toni's Team Neuheiten/Events selbst pflegen kann, ohne Entwicklerunterstützung für jede Änderung zu brauchen.

---

## 7. Nächste Schritte

1. Zugriff auf die bestehende Seite und vorhandene Marken-Assets (Logo-Originaldatei, Fotos, Farbwerte, Texte) beschaffen und dieses Konzept damit abgleichen — die `[Platzhalter]` ersetzen.
2. Mit dem Design-Canvas (Moodboard + Wireframes) in eine Feedbackrunde gehen; Richtungsentscheidung zu Farben/Typografie treffen.
3. Sitemap und Startseiten-Gliederung gegen das tatsächliche Sortiment/Angebot prüfen (z. B. ob Second Hand, Events oder ein Magazin überhaupt Bestandteil des heutigen Angebots sind).
4. Auf Basis des freigegebenen Konzepts technische Umsetzung planen (Shopsystem-Wahl, Content-Pflege durch das Team, Migration bestehender Inhalte).
