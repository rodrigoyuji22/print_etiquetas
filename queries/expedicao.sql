SELECT 
    T0.CardName AS cliente,
    T0.NumAtCard AS pc,
    T0.DocEntry AS pv,
    T1.ItemCode AS item_code,
    T1.Dscription AS descricao,
    T1.SubCatNum AS codigo_item_cliente,
    SUM(T1.Quantity) AS qtd_total,
    STRING_AGG(T2.BatchNum, ',') AS lotes_disponiveis
FROM ORDR T0
INNER JOIN RDR1 T1 ON T0.DocEntry = T1.DocEntry
INNER JOIN OIBT T2 ON T2.ItemCode = T1.ItemCode
WHERE T0.DocEntry = ?
  AND T2.Quantity > 0
GROUP BY 
    T0.CardName,
    T0.NumAtCard,
    T0.DocEntry,
    T1.ItemCode,
    T1.Dscription,
    T1.SubCatNum
ORDER BY 
    T1.ItemCode;
