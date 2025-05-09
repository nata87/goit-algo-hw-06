# Домашнє завдання №6: Графи

## 📘 Опис проєкту
Цей проєкт ілюструє роботу з графами в Python за допомогою бібліотеки `networkx` і містить три завдання:

1. **Створення та аналіз графа реальної мережі** (транспортна мережа міста).
2. **Реалізація пошуку в глибину (DFS) та пошуку в ширину (BFS)**.
3. **Реалізація алгоритму Дейкстри для знаходження найкоротших шляхів у графі**.

---

##  Завдання 1: Побудова графа
- Побудовано граф транспортної мережі міста з вершинами (зупинками) та ребрами (дорогами).
- Візуалізовано граф з підписами та виконано аналіз (кількість вершин, ребер, ступінь кожної вершини).

##  Запуск коду
Переконайтесь, що у вас встановлена бібліотека:

```bash
pip install networkx matplotlib
```
```bash
python task1.py 
```

---

##  Завдання 2: DFS та BFS
- Реалізовано пошук у глибину та пошук у ширину.
- Пошук починається з вершини "Центральна Площа".
- Надруковано шляхи, знайдені кожним із алгоритмів.

##  Запуск коду

```bash
python task2.py 
```

###  Висновки (DFS і BFS)

- **DFS (пошук у глибину)** досліджує шлях якнайдалі від початкової вершини, перш ніж повернутись і дослідити інші варіанти. Через це шлях, знайдений DFS, часто не є найкоротшим у сенсі кількості кроків.
- **BFS (пошук у ширину)** натомість обстежує граф пошарово — спершу всі сусіди, потім сусіди їхніх сусідів тощо. Завдяки цьому BFS завжди знаходить шлях з найменшою кількістю ребер.
- У випадку **незважених графів**, як у цьому завданні, **BFS зазвичай кращий**, якщо потрібно знайти оптимальний (найкоротший) маршрут.

---

##  Завдання 3: Алгоритм Дейкстри
- До графа додано ваги ребер (довжина дороги в км).
- Обчислено найкоротші шляхи від "Центральна Площа" до кожної вершини.
- Виведено шлях та його довжину для кожної пари вершин.

##  Запуск коду

```bash
python task3.py 
```

---

##  Результати (скріншот)

 файл із фактичними результатами:
[ task1_result.PNG](./task1_result.PNG)




