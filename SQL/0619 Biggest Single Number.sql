SELECT
    MAX(num) AS num
FROM
    (SELECT num
    FROM myNumbers
    GROUP BY num
    HAVING COUNT(*) = 1) AS t;