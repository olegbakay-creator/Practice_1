```mermaid
graph TD
    %% Стилизация узлов
    classDef top fill:#2c3e50,stroke:#34495e,stroke-width:3px,color:#fff
    classDef management fill:#3498db,stroke:#2980b9,stroke-width:2px,color:#fff
    classDef prorector fill:#9b59b6,stroke:#8e44ad,stroke-width:2px,color:#fff
    classDef faculty fill:#27ae60,stroke:#229954,stroke-width:2px,color:#fff
    classDef regional fill:#e67e22,stroke:#d35400,stroke-width:2px,color:#fff

    %% Высшее руководство
    PRESIDENT["<b>ПРЕЗИДЕНТ</b><br/>Лобов Вадим Георгиевич"]:::top
    CEO["<b>ГЕНЕРАЛЬНЫЙ ДИРЕКТОР</b><br/>Нестеров Максим Сергеевич"]:::top
    RECTOR["<b>РЕКТОР</b><br/>Васильев Артем Игоревич"]:::top

    PRESIDENT --> RECTOR
    CEO --> RECTOR

    %% Проректоры
    PRO1["<b>Проректор по образовательной деятельности</b><br/>Упоров С.А."]:::prorector
    PRO2["<b>Проректор по СПО и школьному образованию</b><br/>Бельченко Н.В."]:::prorector
    PRO3["<b>Проректор по региональному развитию</b><br/>Ерофеев М.В."]:::prorector
    PRO4["<b>Проректор по финансовому мониторингу</b><br/>Платов А.В."]:::prorector
    PRO5["<b>Проректор по организации приема</b><br/>Кузнецов И.М."]:::prorector
    PRO6["<b>Проректор по исследовательской деятельности</b><br/>Полихина Н.А."]:::prorector
    PRO7["<b>Проректор по молодежной политике</b><br/>Романов М.В."]:::prorector
    PRO8["<b>Проректор по просветительской деятельности</b><br/>Хитрова О.О."]:::prorector
    PRO9["<b>Проректор по патриотическому воспитанию</b><br/>Кудинов М.В."]:::prorector
    PRO10["<b>Проректор</b><br/>Семкина Т.А."]:::prorector
    PRO11["<b>Проректор по общим вопросам</b><br/>Хитров А.В."]:::prorector

    RECTOR --> PRO1
    RECTOR --> PRO2
    RECTOR --> PRO3
    RECTOR --> PRO4
    RECTOR --> PRO5
    RECTOR --> PRO6
    RECTOR --> PRO7
    RECTOR --> PRO8
    RECTOR --> PRO9
    RECTOR --> PRO10
    RECTOR --> PRO11

    %% Факультеты
    FAC1["<b>Факультет информационных технологий</b><br/>Декан: Захаров А.В."]:::faculty
    FAC2["<b>Факультет менеджмента</b><br/>Декан: Гузырь В.В."]:::faculty
    FAC3["<b>Факультет экономики</b><br/>Декан: Кухаренко О."]:::faculty
    FAC4["<b>Факультет театра, кино и ТВ</b><br/>Декан: Наумцева Н.А."]:::faculty
    FAC5["<b>Факультет туризма</b>"]:::faculty
    FAC6["<b>Факультет дизайна</b>"]:::faculty
    FAC7["<b>Факультет психологии</b>"]:::faculty
    FAC8["<b>Факультет бизнеса</b>"]:::faculty
    FAC9["<b>Юридический факультет</b>"]:::faculty
    FAC10["<b>Факультет ГМУ</b>"]:::faculty

    PRO1 --> FAC1
    PRO1 --> FAC2
    PRO1 --> FAC3
    PRO1 --> FAC4
    PRO1 --> FAC5
    PRO1 --> FAC6
    PRO1 --> FAC7
    PRO1 --> FAC8
    PRO1 --> FAC9
    PRO1 --> FAC10

    %% Региональные представительства
    REG1["<b>Региональные представительства</b><br/>40+ филиалов в России и СНГ"]:::regional
    PRO3 --> REG1

    %% Поддержка
    SUPPORT1["<b>Департамент маркетинга</b>"]:::management
    SUPPORT2["<b>IT-департамент</b>"]:::management
    SUPPORT3["<b>Центр развития карьеры</b>"]:::management
    SUPPORT4["<b>Приемная комиссия</b>"]:::management

    CEO --> SUPPORT1
    CEO --> SUPPORT2
    PRO5 --> SUPPORT4
    PRO7 --> SUPPORT3

    %% Стили для связей
    linkStyle default stroke:#34495e,stroke-width:2px
    ```
    