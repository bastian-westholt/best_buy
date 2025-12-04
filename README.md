  
 `____  _____ ____ _____   ____  _   ___   __ | __ )| ____/ ___|_   _| | __ )| | |   / / |  _ |  _| ___  | |   |  _ | | | | V / | |_) | |___ ___) || |   | |_) | |_| | | | |____/|_____|____/ |_|   |____/ ___/  |_|  -- Y O U R   S H O W C A S E   S T O R E --`  
  
  

---

Ein Python-basiertes Shop-System mit vollständigem Error-Handling. Entstanden während meiner Masterschool-Ausbildung als Lernprojekt für OOP und Exception-Handling.

## Was ist das hier?

Ein simples aber robustes E-Commerce-Backend für einen Elektronik-Store. Keine fancy UI, nur solide Python-Logik mit Fokus auf Error-Handling und Validierung.

## Features

-   **Produktverwaltung**: Produkte hinzufügen, entfernen, anzeigen
-   **Lagerverwaltung**: Automatische Deaktivierung bei ausverkauften Produkten
-   **Bestellsystem**: Stock-Validierung, verhindert Überbestellungen
-   **Robuste Input-Validierung**: Fängt ungültige Eingaben ab (Text statt Zahlen, negative Werte, etc.)
-   **Error-Handling**: Business Logic raised Exceptions, Presentation Layer catched sie - so wie es sein soll

## Quick Start

```bash
# Clone the repo
git clone <repo-url>
cd best_buy

# Run it
python3 main.py
```

Keine Dependencies nötig, läuft mit Standard-Python.

## Wie es funktioniert

### Product Class (`products.py`)

Verwaltet einzelne Produkte mit vollständiger Validierung:

-   Name, Price, Quantity → alle validiert (kein Müll erlaubt)
-   Automatische Deaktivierung bei quantity=0
-   `buy()` Methode prüft Stock-Verfügbarkeit

### Store Class (`store.py`)

Verwaltet die Produkt-Collection:

-   Type-Checks im Constructor (nur Product-Objekte erlaubt)
-   Duplikat-Prüfung beim Hinzufügen
-   `get_all_products()` gibt nur aktive Produkte zurück
-   `order()` für Bestellungen mit mehreren Produkten

### Main Program (`main.py`)

CLI mit 4 Optionen:

1.  Liste alle Produkte
2.  Zeige Gesamt-Stock
3.  Bestelle Produkte
4.  Quit (oder Ctrl+C 😉)

Input-Validierung everywhere - Text statt Zahl? ValueError. Produktnummer außerhalb Range? IndexError. Alles wird sauber gefangen.

## Was ich dabei gelernt hab

### Exception Handling Strategy

**Business Logic** (products.py, store.py):

-   Raised Exceptions bei Regel-Verletzungen
-   Keine print() Statements für Errors
-   Klare Exception-Messages

**Presentation Layer** (main.py):

-   Catched Exceptions mit try-except
-   Zeigt benutzerfreundliche Fehlermeldungen
-   Loop läuft weiter, kein Crash

### OOP Best Practices

-   **Single Responsibility**: Jede Klasse macht genau eine Sache
-   **Composition over Inheritance**: Store *hat* Products, ist kein Product
-   **Fail Fast**: Validierung im Constructor, nicht später
-   **Type-Checks**: `isinstance()` vor Operations

### Range-Check Bug (wichtigste Lektion!)

❌ **FALSCH**: `if x < len() or x > len()` → logischer Fehler! ✅ **RICHTIG**: `if x < 1 or x > len()` → korrekte Grenzen

Dieser Bug hat mich gelehrt: Boolean Logic GENAU prüfen, nicht einfach `or` verwenden weil's intuitiv klingt.

### Validierung: Type DANN Value

```python
# ✅ RICHTIG
if not isinstance(price, (int, float)):
    raise TypeError('Price must be numeric')
if price < 0:
    raise ValueError('Price cannot be negative')

# ❌ FALSCH
if not price:  # Bug: 0 wird als invalid behandelt
    raise ValueError(...)
```

Bei Zahlen ist `0` ein valider Wert, nicht "empty"!

## Projekt Status

-   ✅ **Phase 1 & 2 Complete** (CRITICAL + HIGH Priority Bugs)
-   ✅ **14/14 Issues gefixt** (100% der wichtigen Bugs)
-   ✅ **Production Ready** (robustes Error-Handling)
-   ⏳ **Phase 3 Optional** (MEDIUM Priority Edge Cases)

## Testing

Getestete Edge Cases:

-   Text-Input statt Zahlen → ValueError mit Message
-   Negative Zahlen → ValueError mit Message
-   Produktnummer 0 oder außerhalb Range → IndexError
-   Mehr bestellen als auf Lager → Exception mit Stock-Info
-   quantity=0 kaufen → Exception
-   Duplikat-Produkt hinzufügen → ValueError
-   Ctrl+C drücken → "Best Bye!" Message 👋

## Code-Qualität

Priority

Fixed

Status

🔴 CRITICAL

7/7

100% ✅

🟡 HIGH

7/7

100% ✅

🟢 MEDIUM

2/6

33% (optional)

Alle CRITICAL und HIGH Priority Issues sind gefixt. MEDIUM sind Edge Cases die in der Praxis selten auftreten (z.B. Whitespace-only product names).

## Technisches

-   **Python Version**: 3.x (getestet mit 3.13)
-   **Dependencies**: Keine (Standard Library only)
-   **OOP Patterns**: SOLID Principles, Design by Contract
-   **Exception Types**: TypeError, ValueError, IndexError, KeyboardInterrupt

## Warum Best "Bye"?

Weil der Exit-Message ein Typo-Witz ist:

```python
print('Thank you for choosing BEST BYE! 😉')
```

Ja, das war Absicht. 😄

---

**Projekt**: Masterschool E-Commerce Backend **Status**: Production Ready **Entwickelt**: Dezember 2025 **Developer**: Bastian