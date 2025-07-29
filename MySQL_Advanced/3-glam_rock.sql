-- Script to list all bands with Glam rock as their main style, ranked by longevity
-- Calculates lifespan using formed and split attributes
-- If split is NULL (band still active), uses current year (2022)

SELECT 
    band_name,
    -- Calculate lifespan: if split is NULL, use 2022 as current year
    (IFNULL(split, 2022) - formed) AS lifespan
FROM 
    metal_bands
WHERE 
    -- Filter for bands with Glam rock as main style
    FIND_IN_SET('Glam rock', IFNULL(style, '')) > 0
ORDER BY 
    -- Order by lifespan descending (longest career first)
    lifespan DESC;
