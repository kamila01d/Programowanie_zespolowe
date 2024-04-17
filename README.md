# Programowanie_zespolowe: Comparly

## Specyfikacja wymagań:

- Działanie aplikacji:
  1. Chcemy żeby kiedy użytkownik wpisze nazwę produktu, wyświetlała
     się posortowana lista po cenach z odnośnikami do sklepów
  2. Wyświetlanie podglądowych zdjęć produktów
  3. Informacje o produktach
  4. Rejestracja i logowanie użytkowników
  5. Dodawanie przez użytkowników ulubionych produktów
- Widoki w aplikacji:
  1. Podstawowy widok, w którym użytkownik może wpisać w search bar
     produkt
  2. Widok po wpisaniu produktów - wyświetlana jest posortowana lista
     (zdjęcie, cena, sklep, link do sklepu) wyszukiwanego produktu w
     zależności od ceny. Mamy również zakładkę 'informacje' oraz 'opinie'
  3. W widoku 'informacje' wyświetlane są informacje o produkcie
     (pozyskane ze sklepu z najniższą ceną)
  4. W widoku opinie - wszystkie zebrane opinie ze wszystkich sklepów na
     temat tego produktu.
  5. Strona z logowaniem/rejestracją
  6. Strona z listą ulubionych produktów

## Wymagania technologiczne

- Python (backend)
- Baza danych - postgress
- Scaprowanie stro przy użyciu frameworka playwright
- React + typescript
- Repozytorium - Github
- Komunikator - discord

## Podział na moduły i określenie zależności

- Backend aplikacji:
  1. Wysyłanie zapytań o wyszukiwanym produkcie do zewnętrznych zasobów (sklepy internetowe np. Allegro, Amazon, ebay)
  2. Pogrupowanie danych (w formie Jsona - taki Json powinien zawierać nazwę produktu, cenę, nazwa sklepu, link do produktu, zdjęcie, opis produktu, lista opinii)
- Scrapowanie danych
- Moduł logowania i rejestracji użytkownika
- Moduł przechowywania informacji o użytkownikac (ulubione produkty)
- Frontend:
  1. Widok landing page ( strona powitalna na której jest search bar)
  2. Strona do logowania/rejestracji
  3. Strona z pogrupowanymi produktami
  4. Strona ze szczegółami o produkcie

## Sprecyzowanie zadań

- Szkielet projektu
- Stworzenie bazy danych (schemat)
- Stworzenie modułu do rejestracji i logowania
- Z jakich źródeł będą pozyskiwane te dane
- Tworzenie połączeń ze sklepami
- Zapisywanie ulubionych produktów użytkowników do bazy
- Opracowanie danych -> output w formie Jsona
- Bazowe komponenty na froncie
- Moduł stanowy obiektów
- Widoki
