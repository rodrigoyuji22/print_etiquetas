SELECT DISTINCT
    T0.CardName as cliente,
    T0.NumAtCard as pc,
    T0.DocEntry as pv,
    T1.ItemCode as item_code,
    T1.Dscription as descricao,
    T2.BatchNum as lote,
    T1.SubCatNum as codigo_item_cliente,
    T2.Quantity as qtd
FROM ORDR T0
INNER JOIN RDR1 T1 ON T0.DocEntry = T1.DocEntry
INNER JOIN OIBT T2 ON T2.ItemCode = T1.ItemCode
WHERE T0.DocEntry = {pv_}
  {filtro_item_}
  AND T2.Quantity > 0
ORDER BY T1.ItemCode, T2.BatchNum;
