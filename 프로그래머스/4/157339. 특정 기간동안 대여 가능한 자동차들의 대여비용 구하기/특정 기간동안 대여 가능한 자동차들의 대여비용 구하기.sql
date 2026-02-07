WITH AVAILABLE_RENTAL_CARS AS (SELECT ca.car_id, ca.car_type, ca.daily_fee
                               FROM CAR_RENTAL_COMPANY_CAR ca
                                   LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY his
                                   ON ca.car_id = his.car_id
                                   AND his.start_date <= '2022-11-30'
                                   AND his.end_date >= '2022-11-01'
                                WHERE ca.car_type IN("세단", "SUV") AND his.car_id IS NULL)

SELECT rca.car_id,
       rca.car_type,
       FLOOR(rca.daily_fee * 30 * (100 - pl.discount_rate) / 100) AS FEE
FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN pl
    JOIN AVAILABLE_RENTAL_CARS rca
    ON pl.car_type = rca.car_type
WHERE pl.duration_type = "30일 이상"
    AND FLOOR(rca.daily_fee * 30 * (100 - pl.discount_rate) / 100) >= 500000
    AND FLOOR(rca.daily_fee * 30 * (100 - pl.discount_rate) / 100) < 2000000
ORDER BY FEE DESC, car_type ASC, car_id DESC;