SELECT 
    OINV.FolioNum        AS NumeroNF,
    OINV.DocDate         AS DataNF,
    ODLN.DocNum          AS NumeroEntrega,
    ODLN.CardName        AS NomeCliente,
    DLN12.City           AS MunicipioEntrega,
    DLN12.State          AS EstadoEntrega
FROM OINV
INNER JOIN INV1 ON OINV.DocEntry = INV1.DocEntry
INNER JOIN ODLN ON INV1.BaseEntry = ODLN.DocEntry AND INV1.BaseType = 15 --entrega
LEFT JOIN DLN12 ON ODLN.DocEntry = DLN12.DocEntry
WHERE OINV.FolioNum = {nf};
