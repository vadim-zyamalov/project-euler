fib :: [Int]
fib = 1 : 1 : zipWith (+) fib (tail fib)

main :: IO()
main = print $ sum $ filter even $ takeWhile (< 4_000_000) fib
