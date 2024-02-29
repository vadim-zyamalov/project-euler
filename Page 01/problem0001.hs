solve :: Int -> Int
solve n = sum $ [x | x <- [1 .. n], x `mod` 3 == 0 || x `mod` 5 == 0]

solveFast :: Int -> Int
solveFast n = let
    n3 = n `div` 3
    n5 = n `div` 5
    n15 = n `div` 15
    s3 = 3 * (n3 + 1) * n3 `div` 2
    s5 = 5 * (n5 + 1) * n5 `div` 2
    s15 = 15 * (n15 + 1) * n15 `div` 2
    in s3 + s5 - s15


main :: IO()
main = print $ solveFast 999
