import Utils (combinationsR)

main :: IO()
main = print $ (!! 0) . map (\[a, b] -> a * b * (1000 - a - b)) $
    filter (\[a, b] -> (1000 - a - b)^ 2 == a^2 + b^2) $
    filter (\[a, b] -> 1000 - a - b > 0) $
    combinationsR 2 [1..500]
