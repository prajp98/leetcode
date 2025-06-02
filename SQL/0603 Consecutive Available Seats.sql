SELECT DISTINCT c1.seat_id
FROM cinema c1
JOIN cinema c2
  on ABS(c1.seat_id - c2.seat_id) = 1
    and c1.free = 1 and c2.free = 1
ORDER BY c1.seat_id;