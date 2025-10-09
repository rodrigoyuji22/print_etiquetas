SELECT 
    OINV.FolioNum           AS nf,
    T0.CardName             AS cliente,
    T0.NumAtCard            AS pc,
    T0.DocEntry             AS pv,
    T1.ItemCode             AS item_code,
    T1.Dscription           AS descricao,
    T1.SubCatNum            AS codigo_item_cliente,
    SUM(T1.Quantity)        AS qtd_total,
    STRING_AGG(T2.BatchNum, ',') AS lotes_disponiveis
FROM OINV
INNER JOIN INV1 ON OINV.DocEntry = INV1.DocEntry
INNER JOIN ORDR T0 ON INV1.BaseEntry = T0.DocEntry
INNER JOIN RDR1 T1 ON T1.DocEntry = T0.DocEntry AND T1.ItemCode = INV1.ItemCode
INNER JOIN OIBT T2 ON T2.ItemCode = T1.ItemCode
WHERE OINV.FolioNum = ?
  AND T2.Quantity > 0
GROUP BY 
    OINV.FolioNum,
    T0.CardName,
    T0.NumAtCard,
    T0.DocEntry,
    T1.ItemCode,
    T1.Dscription,
    T1.SubCatNum
ORDER BY 
    T1.ItemCode;
