# Behave - BDD (Behavior Driven Development)

## Co to jest Behave?
- **BDD framework** - testowanie przez opisywanie zachowania w języku naturalnym
- **Gherkin syntax** - Given/When/Then do pisania scenariuszy
- **Dla testów akceptacyjnych** - nie unit testów!

## Struktura projektu
```
_behave/
├── src/                # Kod źródłowy aplikacji  
│   ├── calculator.py
│   └── login_system.py
├── features/           # Scenariusze w języku naturalnym (.feature)
│   ├── calculator.feature
│   ├── login.feature
│   └── steps/          # Implementacje kroków (tylko glue code)
│       ├── calculator_steps.py
│       └── login_steps.py
├── environment.py      # Setup/teardown (opcjonalne)
└── README.md
```

## Instalacja i uruchomienie
```bash
pip install behave
cd _behave
behave                  # Uruchamia wszystkie .feature
behave features/calculator.feature  # Konkretny plik
```

## Składnia Gherkin
- **Feature:** - opis funkcjonalności
- **Scenario:** - konkretny test case
- **Given** - warunki początkowe
- **When** - akcja użytkownika  
- **Then** - oczekiwany wynik
- **And** - dodatkowe kroki tego samego typu

## Dlaczego BDD?
- **Komunikacja** - biznes i dev mówią tym samym językiem
- **Dokumentacja żywa** - scenariusze to dokumentacja
- **Testy akceptacyjne** - testowanie całych workflow'ów

## Przykłady w tym folderze

### 1. simple_example.feature
**Najprostszy przykład** - jeden scenariusz, jeden krok
```gherkin
Scenario: Say hello
  Given I have a name "World"
  When I say hello  
  Then I should get "Hello, World!"
```

### 2. features/calculator.feature
**Podstawowe operacje** - matematyka z parametryzacją
- Dodawanie, odejmowanie, mnożenie
- `Scenario Outline` - parametryzowane testy
- Obsługa błędów (dzielenie przez zero)

### 3. features/login.feature  
**Realistyczny przykład** - system logowania
- `Background` - setup wspólny dla scenariuszy
- `@tags` - grupowanie testów
- Wielokrotne kroki z `And`
- Symulacja lockout'u konta

## Kluczowe koncepty

### Context object
```python
# Przekazywany między krokami (jak fixture)
context.calculator = Calculator()
context.result = 42
```

### Capture parameters - konwertery typów (z modułu `parse`)

Behave używa biblioteki `parse` która dostarcza konwertery:

| Konwerter | Opis | Przykład | Typ w Pythonie |
|-----------|------|----------|----------------|
| `{x:d}` | Decimal integer | `{age:d}` → 25 | `int` |
| `{x:f}` | Float | `{price:f}` → 19.99 | `float` |  
| `{x:w}` | Word chars (letters, numbers, _) | `{name:w}` → "John_123" | `str` |
| `{x}` | String (domyślny) | `{text}` → "hello" | `str` |

**Uwaga:** Nie wszystkie konwertery mogą być dostępne w każdej wersji behave.

**Przykłady użycia:**
```python
@when('I add {num1:d} and {num2:d}')      # num1, num2 = int, int
@given('I have a balance of {amount:f}')  # amount = float  
@when('I search for {query:w}')           # query = str (jedno słowo)
@then('I see message "{text}"')           # text = str z cudzysłowami
```

**W Gherkin:**
```gherkin
When I add 5 and 3          # {num1:d}=5, {num2:d}=3
Given I have a balance of 19.99    # {amount:f}=19.99
When I search for python           # {query:w}="python"  
Then I see message "Success!"      # {text}="Success!"
```

### Step matching
```python
# Gherkin:     Given I have a calculator
# Python:      @given('I have a calculator')
```

### Background - wspólny setup
```gherkin
Feature: Login system

Background:              # Wykonuje się przed każdym scenariuszem
  Given I open browser
  And I go to login page

Scenario: Valid login    # Background + ten scenariusz  
  When I enter credentials
  Then I see dashboard
```

**Ważne:**
- **Pozycja**: po `Feature:`, przed pierwszym `Scenario:`
- **Jeden per plik** .feature
- **Automatycznie** uruchamia się przed każdym scenariuszem

### Tags i uruchamianie
```bash
behave                                # Wszystkie testy
behave --tags=@smoke                  # Tylko @smoke
behave --tags=@smoke,@critical        # @smoke LUB @critical  
behave --tags=@smoke --tags=@critical # @smoke I @critical
behave features/calculator.feature    # Konkretny plik
```

## Formatowanie Gherkin
- **Wcięcia** - dowolne, ale konsekwentne (2 spacje zalecane)
- **Języki** - obsługa polskiego: `# language: pl`
- **Komentarze** - linie zaczynające się od `#`
- **Wieloliniowe stringi** - użyj `"""`

## Najczęstsze błędy
1. **Brak step definition** - musisz zaimplementować każdy krok
2. **Niewłaściwe matching** - tekst musi dokładnie pasować
3. **Context nie przekazany** - użyj `context.` do przechowywania danych
4. **Zbyt szczegółowe scenariusze** - BDD to high-level testy