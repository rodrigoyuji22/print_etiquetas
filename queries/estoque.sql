SELECT 
    T0.ItemCode AS item_code,
    T0.ItemName AS descricao,
    STRING_AGG(T1.BatchNum, ',') AS lotes_disponiveis
FROM OITM AS T0
INNER JOIN OIBT AS T1 ON T1.ItemCode = T0.ItemCode
WHERE 
    T1.Quantity > 0
    AND T0.ItemCode LIKE ?
GROUP BY 
    T0.ItemCode,
    T0.ItemName
ORDER BY 
    T0.ItemCode;