# IWH-STARK: ostdeutsche Energieversorgung

Aus dem Projekt zur [Evaluation des "Kohlekompromisses"](https://www.iwh-halle.de/forschung/projekte/evaluierung-des-invkg-und-des-bundesprogrammes-stark) (InvKG & KVBG) des IWH Halle



**Fragen**:

- Welche Stein-/Braunkohlekraftwerke werden in den Revieren abgeschaltet?
  - Wie viele Beschäftigte haben dort gearbeitet?
  - Welche wurden im Rahmen des KVBG kompensiert?
- Was entsteht an neuen Kraftwerken in den Revieren (Gas / Wind / PV)?
  - welche davon auf dem Gebiet ehemaliger Tagebaue / Kraftwerke?





**Datenquellen**

- Marktstammdatenregister (MASTR): [Bundesnetzagentur](https://www.marktstammdatenregister.de/MaStR)
- Kraftwerksliste (KWL): [Bundesnetzagentur](https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/Versorgungssicherheit/Erzeugungskapazitaeten/Kraftwerksliste/start.html), basiert auf MASTR
- Liste deutscher Braunkohletagebaue (LBKT): [Wikipedia](https://de.wikipedia.org/wiki/Liste_deutscher_Braunkohletagebaue#Weblinks)
- PLZ-Zuordnung zu Ort / BL (PLZ): [Postleitzahl.net](https://www.postleitzahl.net/plz-downloads)
- Kompensation für Kraftwerke (KVBG): [Anlage 2 KVBG](https://www.buzer.de/Anlage_2_KVBG.htm)
- Fördergebiete / Reviere (INVKG): [§2 / §11 / §12 InvKG](https://www.vdivde-it.de/sites/default/files/document/Hinweisblatt-F%c3%b6rdergebiete_0.pdf)



**Datensatz 1**: AbbauKW

| Variable            | Beschreibung / Kommentar                                | Quelle |
| ------------------- | ------------------------------------------------------- | ------ |
| nr_MASTR            | Nr im MASTR                                             | KWL    |
| betreiber           | Betreiber des Kraftwerks (unvollständig!)               | KWL    |
| name                | Name des Kraftwerks (unvollständig!)                    | KWL    |
| energietraeger      | Erdgas, Kohle etc                                       | KWL    |
| leistung_brutto     | Bruttoleistung in Megawatt                              | KWL    |
| leistung_netto      | Nettoleistung in Megawatt                               | KWL    |
| plz                 | Postleitzahl                                            | KWL    |
| kreis               | Landkreis                                               | PLZ    |
| bundesland          | Bundesland                                              | PLZ    |
| region              | `Rheinisches Revier`, `Mitteldeutsches Revier`, ...     | INVKG  |
|                     |                                                         |        |
| jahr_inbetriebnahme | Jahr der Inbetriebname des KW                           | KWL    |
| stillgelegt         | `true / false`                                          |        |
| stillegung_type     | siehe Erklärung                                         | KWL    |
| jahr_stillegung     | wenn `stillgelegt=true`, auch mit Jahren in der Zukunft | KWL    |

 `stillegung_type` = Grund für die Stillegung

- KVBG = beinhaltet auch KW, die in die Reserve nach KVBG geschickt werden (Da sie effektiv nicht mehr produzieren)
- EnWG = Stillegung nach §13 EnWG
- "reserve" = nach ENWG (Netz bzw Kapaittätsreservere), oder [besonderes netztechniches Betriebsmittel](https://de.wikipedia.org/wiki/Besondere_netztechnische_Betriebsmittel)
- 



**Datensatz 2**: AufbauKW

| Variable | Beschreibung                                                 | Quelle |
| -------- | ------------------------------------------------------------ | ------ |
| nr_MASTR | Nr im MASTR | MASTR |
| anlagenbetreiber    | Betreiber des Kraftwerks (unvollständig!)               | MASTR |
| anzeigename         | Name des Kraftwerks (unvollständig!)                    | MASTR |
| energietraeger      | Erdgas, Kohle etc                                       | MASTR |
| bruttoleistung      | Bruttoleistung in Megawatt                              | MASTR |
| nettoleistung       | Nettoleistung in Megawatt                               | MASTR |
| region   | `Rheinisches Revier`, `Mitteldeutsches Revier`, ...          | INVKG  |
| tagebau  | `true/false`: ob die Analge auf ehemaligen Tagebaugebiet ist | LBKT |
| plz                 | Postleitzahl                                            | MASTR  |
| kreis               | Landkreis                                               | PLZ    |
| bundesland          | Bundesland                                              | PLZ    |
