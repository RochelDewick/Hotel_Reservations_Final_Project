--Query 1
WITH top_agent AS
(
SELECT TOP (1)
r.agent agent, 
COUNT(r.agent) AS agent_bookings
FROM Reservation r
INNER JOIN  guest g 
ON r.GuestId = g.GuestId
GROUP BY r.agent, g.country
HAVING   g.country = 'GBR'
ORDER BY agent_bookings DESC)

SELECT TOP (10)
r.*, g.*
FROM top_agent
LEFT JOIN RESERVATION r ON top_agent.agent = r.agent
LEFT JOIN Guest g ON r.GuestId = g.GuestId
WHERE g.country = 'GBR';

--Query 2
SELECT *
FROM Reservation r
INNER JOIN Guest g ON g.GuestId = r.GuestId
WHERE (YEAR(r.arrival_date) = '2015')
 AND (r.adr BETWEEN 80 AND 90)
AND (r.is_canceled != 1);

--Query 3
SELECT AVG(r.stays_in_weekend_nights+ r.stays_in_week_nights) nights,
g.children children
FROM Guest g
INNER JOIN Reservation r ON g.GuestId = R.GuestId
GROUP BY children
ORDER BY children

--Bonus Query:  Average ADR per country
SELECT g.country country,
	   AVG(r.ADR) avg_rate
FROM Guest g
INNER JOIN Reservation r ON g.GuestId = R.GuestId
GROUP BY country
ORDER BY avg_rate; 