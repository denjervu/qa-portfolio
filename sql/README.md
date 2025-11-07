[⬅️ вернуться на главную](https://github.com/denjervu)

# SQL-запросы

# Задание 1

[Схема таблиц](https://sql-academy.org/ru/trainer/tasks/55)

Удалить компании, совершившие наименьшее количество рейсов.

```sql
WITH min_trips AS (
    SELECT name, COUNT(Trip.id) as trip_count
    FROM Company
    INNER JOIN Trip ON Company.id=Trip.company
    GROUP BY name
)
DELETE 
FROM Company
WHERE name IN (
    SELECT name 
    FROM min_trips
    WHERE trip_count = (SELECT(MIN(trip_count)) FROM min_trips)
)    
```

# Задание 2

[Сxема таблиц](https://sql-academy.org/ru/trainer/tasks/76)

Вывести имена всех пользователей сервиса бронирования жилья, а также два признака: является ли пользователь собственником какого-либо жилья (is_owner) и является ли пользователь арендатором (is_tenant). В случае наличия у пользователя признака необходимо вывести в соответствующее поле 1, иначе 0.

```sql
SELECT 
    u.name,
    CASE WHEN r.owner_id IS NULL THEN 0 ELSE 1 END AS is_owner,
    CASE WHEN res.user_id IS NULL THEN 0 ELSE 1 END AS is_tenant
FROM Users u
LEFT JOIN Rooms r ON u.id = r.owner_id
LEFT JOIN Reservations res ON u.id = res.user_id
GROUP BY u.id, u.name;
```

# Задание 3

[Схема таблиц](https://sql-academy.org/ru/trainer/tasks/27)

Узнайте, сколько было потрачено на каждую из групп товаров в 2005 году. Выведите название группы и потраченную на неё сумму. Если потраченная сумма равна нулю, т.е. товары из этой группы не покупались в 2005 году, то не выводите её.

```sql
WITH 2005_good_type_names AS (
    SELECT gt.good_type_name, SUM(unit_price * amount) AS costs
    FROM Payments p
    INNER JOIN Goods g ON p.good = g.good_id
    INNER JOIN GoodTypes gt ON gt.good_type_id = g.type
    WHERE YEAR(p.date) = 2005
    GROUP BY gt.good_type_name
)

SELECT good_type_name, costs
FROM 2005_good_type_names;
```