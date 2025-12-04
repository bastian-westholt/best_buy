<div align="center">
<pre>
 ____  _____ ____ _____   ____  _   ___   __
| __ )| ____/ ___|_   _| | __ )| | | \ \ / /
|  _ \|  _| \___ \ | |   |  _ \| | | |\ V /
| |_) | |___ ___) || |   | |_) | |_| | | |
|____/|_____|____/ |_|   |____/ \___/  |_|

--- Y O U R   S H O W C A S E   S T O R E ---
</pre>
</div>

---

Ein Shop-Backend, das ich während meiner Masterschool-Ausbildung entwickelt habe. Der Fokus lag auf Error-Handling und OOP-Patterns.

## Was macht das Projekt?

Ein einfaches E-Commerce-System für einen Elektronik-Store. CLI-basiert, keine UI - nur Backend-Logik. Das Projekt startete mit bewusst eingebauten Bugs, die ich dann systematisch identifiziert und behoben habe.

## Setup

```bash
git clone <repo-url>
cd best_buy
python3 main.py
```

Keine Dependencies erforderlich, läuft mit Standard-Python.

## Wie es funktioniert

### Product Class
Verwaltet einzelne Produkte. Name, Preis und Lagermenge werden validiert bevor sie akzeptiert werden. Wenn der Stock auf 0 fällt, wird das Produkt automatisch deaktiviert. Die `buy()` Methode prüft die Lagerverfügbarkeit vor dem Kauf.

### Store Class
Verwaltet die Produktkollektion. Der Constructor stellt sicher, dass nur Product-Objekte hinzugefügt werden. Beim Hinzufügen wird geprüft, ob das Produkt bereits existiert. Die `order()` Methode ermöglicht den Kauf mehrerer Produkte.

### Main Program
CLI mit 4 Optionen: Produkte auflisten, Gesamtbestand anzeigen, Bestellung aufgeben, Programm beenden. Input-Validierung ist durchgehend implementiert - bei ungültigen Eingaben werden aussagekräftige Fehlermeldungen angezeigt statt eines Crashes.

## Was ich dabei gelernt habe

### Der Range-Check Bug
Der subtilste Fehler war `if x < len() or x > len()` - sieht auf den ersten Blick korrekt aus, ist aber logisch falsch. Mit `or` ist die Bedingung fast immer true. Korrekt wäre `if x < 1 or x > len()`. Diese Erfahrung hat mir gezeigt, wie wichtig es ist, Boolean Logic sorgfältig zu prüfen.

### Exception Handling Strategy
Business Logic (products.py, store.py) wirft Exceptions bei Regelverletzungen. Presentation Layer (main.py) fängt diese ab und zeigt dem User verständliche Meldungen. Keine print() Statements in der Business Logic, try-except Blöcke nur dort wo sie hingehören.

### Type Checks vor Value Checks
Erst den Typ prüfen, dann den Wert validieren. Sonst kann `if not price` bei 0 fälschlicherweise einen Fehler werfen, obwohl 0 ein valider Preis sein kann.

```python
# Korrekte Reihenfolge
if not isinstance(price, (int, float)):
    raise TypeError('Price must be numeric')
if price < 0:
    raise ValueError('Price cannot be negative')
```

### 0 ist nicht "empty"
Bei Strings ist `""` empty. Bei Zahlen ist `None` empty. Aber `0` ist ein valider Wert, nicht empty. Ein wichtiger Unterschied, den man beachten muss.

## Projekt Status

Alle CRITICAL (7/7) und HIGH Priority (7/7) Bugs sind behoben. Von 20 identifizierten Issues sind 14 erledigt. Die restlichen 6 sind Edge Cases, die in der Praxis selten auftreten (z.B. Produktnamen die nur aus Leerzeichen bestehen).

Der Code ist production-ready. Es gibt keine bekannten Bugs, die das Programm zum Absturz bringen können.

## Testing

Getestete Szenarien:
- Text-Input bei erwarteten Zahlenwerten
- Negative Zahlen
- Produktnummer 0 oder außerhalb des gültigen Bereichs
- Bestellmenge übersteigt Lagerbestand
- Versuche 0 Stück zu kaufen
- Duplikat-Produkte hinzufügen
- Ctrl+C während der Programmausführung

Alle Fälle werden sauber abgefangen mit aussagekräftigen Error-Messages.

## Technisches

- Python 3.x (getestet mit 3.13)
- Keine externen Dependencies
- SOLID Principles, Design by Contract
- Exception Types: TypeError, ValueError, IndexError, KeyboardInterrupt

## Best "Bye" Easter Egg

Die Exit-Nachricht lautet "Thank you for choosing BEST BYE!" - der Typo ist beabsichtigt. 😉

---

**Masterschool E-Commerce Backend** | Dezember 2025 | Bastian
