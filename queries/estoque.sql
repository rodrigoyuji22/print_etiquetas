SELECT DISTINCT 
    T0.ItemCode as item_code,
    T0.ItemName as descricao,
    T1.BatchNum as lote,
    T1.Quantity as qtd
FROM OITM T0
INNER JOIN OIBT T1 ON T1.ItemCode = T0.ItemCode
WHERE T1.Quantity > 0
    AND T0.ItemCode = ?
ORDER BY 
    T0.ItemCode,
    T1.BatchNum;