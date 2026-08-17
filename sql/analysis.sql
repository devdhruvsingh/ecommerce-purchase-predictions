-- E-Commerce Purchase Prediction
-- SQL Business Analysis

-- 1. DATASET OVERVIEW
-- ============================================================

-- Total number of sessions

SELECT COUNT(*) AS total_sessions
FROM online_shoppers;


-- Total purchasing sessions

SELECT COUNT(*) AS purchasing_sessions
FROM online_shoppers
WHERE Revenue = 1;


-- Total non-purchasing sessions

SELECT COUNT(*) AS non_purchasing_sessions
FROM online_shoppers
WHERE Revenue = 0;


-- Overall purchase rate

SELECT
    ROUND(
        SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS purchase_rate_percentage
FROM online_shoppers;

-- What is our overall purchase/ conversion rate?

SELECT COUNT(*) AS total_sessions, SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) AS purchases,
ROUND(
    SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) * 100.0/ COUNT(*), 2
) AS purchase_rate_percentage
FROM online_shoppers;

-- which visitor type has the highest purchase rate?

SELECT
    VisitorType,
    COUNT(*) AS total_sessions,
    SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) AS purchases,
    ROUND(
        SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS purchase_rate_percentage
FROM online_shoppers
GROUP BY VisitorType
ORDER BY purchase_rate_percentage DESC;


-- Which months have the highest and lowest purchase rates?

SELECT
    Month,
    COUNT(*) AS total_sessions,
    SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) AS purchases,
    ROUND(
        SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS purchase_rate_percentage
FROM online_shoppers
GROUP BY Month
ORDER BY purchase_rate_percentage DESC;


-- Which traffic sources generate the highest purchase rate?
SELECT
    TrafficType,
    COUNT(*) AS total_sessions,
    SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) AS purchases,
    ROUND(
        SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS purchase_rate_percentage
FROM online_shoppers
GROUP BY TrafficType
ORDER BY purchase_rate_percentage DESC;

-- Which regions have the highgest purchase rates?

SELECT
    Region,
    COUNT(*) AS total_sessions,
    SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) AS purchases,
    ROUND(
        SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS purchase_rate_percentage
FROM online_shoppers
GROUP BY Region
ORDER BY purchase_rate_percentage DESC;


-- Do purchasers show higher website engagement?
SELECT
    Revenue,
    COUNT(*) AS sessions,
    ROUND(AVG(ProductRelated), 2) AS avg_product_pages,
    ROUND(AVG(ProductRelated_Duration), 2) AS avg_product_duration,
    ROUND(AVG(TotalDuration), 2) AS avg_total_duration,
    ROUND(AVG(TotalPages), 2) AS avg_total_pages
FROM online_shoppers
GROUP BY Revenue;

-- What do highly engaged sessions look like?
WITH engagement AS (
    SELECT
        *,
        ProductRelated + Informational + Administrative AS total_pages
    FROM online_shoppers
)

SELECT
    Revenue,
    COUNT(*) AS sessions,
    ROUND(AVG(total_pages), 2) AS avg_pages,
    ROUND(AVG(TotalDuration), 2) AS avg_duration
FROM engagement
GROUP BY Revenue;