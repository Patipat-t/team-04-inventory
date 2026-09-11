-- 1. รายงาน Top 5 E-Book ที่ทำรายได้สูงสุด (JOIN & GROUP BY)
SELECT 
    e.ebook_id,
    e.title,
    COUNT(oi.order_id) AS total_orders_sold,
    SUM(oi.price * oi.quantity) AS total_revenue
FROM ebooks e
JOIN order_items oi ON e.ebook_id = oi.ebook_id
JOIN orders o ON oi.order_id = o.order_id
WHERE o.status = 'confirmed'
GROUP BY e.ebook_id, e.title
ORDER BY total_revenue DESC
LIMIT 5;

-- 2. รายงานสรุปยอดขายประจำเดือน (Aggregate & Grouping)
SELECT 
    DATE_FORMAT(o.created_at, '%Y-%m') AS sales_month,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(o.total_amount) AS monthly_revenue
FROM orders o
WHERE o.status = 'confirmed'
GROUP BY sales_month
ORDER BY sales_month DESC;

-- 3. รายงานผู้ใช้งานที่มีสิทธิ์ดาวน์โหลด E-Book มากที่สุด (Complex JOIN)
SELECT 
    u.user_id,
    u.email,
    COUNT(dl.link_id) AS total_downloads
FROM users u
JOIN orders o ON u.user_id = o.user_id
JOIN download_links dl ON o.order_id = dl.order_id
WHERE dl.is_used = TRUE
GROUP BY u.user_id, u.email
ORDER BY total_downloads DESC;