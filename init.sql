/*Вывод Сессий*/
SELECT S.id, S.name_of_session, S.duration, T.type_of_equipment, S.price 
FROM Sessions S 
JOIN Technic T ON S.technique_id = T.id;

/*Вызов доступных услуг*/
SELECT * FROM services;

/*Вывод клиентов. В status_about_block: t - не забанен, f - забанен*/
SELECT * FROM clients;

/*Вывод техники*/
SELECT * FROM technic;

/*Вывод Заказов*/
SELECT O.id, C.full_name, Ss.name_of_session, Sc.name, O.date_of_order,
Sc.price + Ss.price AS Total_amoun
FROM Orders O 
INNER JOIN Clients C ON O.client_id = C.id
INNER JOIN Sessions Ss ON O.session_id = Ss.id
INNER JOIN Services Sc ON O.service_id = Sc.id;

