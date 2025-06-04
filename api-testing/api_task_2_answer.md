Решение к заданию 2 Petstore.

| №  | Метод   | Запрос                       | Статус-код | Описание по документации         | Действия для получения                                                        |
|----|---------|------------------------------|------------|----------------------------------|-------------------------------------------------------------------------------|
| 1  | POST    | ADD A NEW PET                | 405        | Invalid input                    | Использовал другой метод - GET                                                |
| 2  | PUT     | UPDATE A PET                 | 400        | Invalid ID supplied              | Удалил часть в body                                                         |
| 3  | PUT     | UPDATE A PET                 | 404        | Pet not found                    | Добавил в адрес запроса несуществующий endpoint (`/pets` вместо `/pet`)       |
| 4  | PUT     | UPDATE A PET                 | 405        | Validation exception             | Использовал другой метод - GET                                                |
| 5  | GET     | SEARCH A PET BY STATUS       | 400        | Invalid status value             | Добавил заголовок с невалидным значением (`Content-Length: -10`)              |
| 6  | GET     | SEARCH A PET BY ID           | 400        | Invalid ID supplied              | Добавил заголовок с невалидным значением (`Content-Length: -10`)              |
| 7  | GET     | SEARCH A PET BY ID           | 404        | Pet not found                    | Использовал специфичный ID (`-2`)                                             |
| 8  | POST    | UPDATE A PET BY FORM         | 405        | Invalid input                    | Использовал другой метод - PUT                                                |
| 9  | DELETE  | DELETE A PET                 | 400        | Invalid ID supplied              | Добавил заголовок с невалидным значением (`Content-Length: -10`)              |
| 10 | POST    | PLACE AN ORDER FOR A PET     | 400        | Invalid Order                    | Добавил заголовок с невалидным значением (`Content-Length: -10`)              |
| 11 | GET     | SEARCH ORDER BY ID           | 400        | Invalid Order                    | Добавил заголовок с невалидным значением (`Content-Length: -10`)              |
| 12 | DELETE  | DELETE ORDER                 | 400        | Invalid Order                    | Добавил заголовок с невалидным значением (`Content-Length: -10`)              |
| 13 | GET     | GET USER BY USERNAME         | 400        | Invalid username supplied        | Добавил заголовок с невалидным значением (`Content-Length: -10`)              |
| 14 | PUT     | UPDATE USER                  | 400        | Invalid user supplied            | Добавил заголовок с невалидным значением (`Content-Length: -10`)              |
| 15 | DELETE  | DELETE USER                  | 400        | Invalid username supplied        | Добавил заголовок с невалидным значением (`Content-Length: -10`)              |
| 16 | GET     | LOG IN USER                  | 400        | Invalid username/password        | Добавил заголовок с невалидным значением (`Content-Length: -10`)              |

