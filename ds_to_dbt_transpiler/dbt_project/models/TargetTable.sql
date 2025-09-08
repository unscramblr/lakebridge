
SELECT
    ID AS ID,\n    Name AS NewName
FROM {{ ref('stg_SourceTable') }}
