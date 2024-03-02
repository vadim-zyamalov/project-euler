import Utils ( combinationsR )

isPalyndrome :: Int -> Bool
isPalyndrome n = s == rs
    where
        s = show n
        rs = reverse s

solve :: Int
solve = maximum . filter isPalyndrome . map product . combinationsR 2 $ [999,998..100]

main :: IO()
main = print $ solve
