SELECT
ROUND(
    IFNULL(
    (SELECT COUNT(*)
    FROM (SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted) AS A)
    /
    (SELECT COUNT(*)
    FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) AS B),
    0)
, 2) AS accept_rate;