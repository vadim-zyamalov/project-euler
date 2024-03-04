sqos :: Integer -> Integer
sqos n = (^2) $ n * (n + 1) `div` 2

sosq :: Integer -> Integer
sosq n = n * (n + 1) * (2 * n + 1) `div` 6

solve = sequence [sqos, negate . sosq]

main :: IO()
main = print $ sum . solve $ 100
