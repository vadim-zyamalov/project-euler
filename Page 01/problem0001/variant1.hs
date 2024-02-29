solve :: Int -> Int
solve n = sum $ [x | x <- [1 .. n], x `mod` 3 == 0 || x `mod` 5 == 0]

main :: IO()
main = print $ solve 999
