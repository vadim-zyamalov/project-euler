primes :: [Int]
primes = primes' [2..]
    where
        primes' (x:xs) = x : primes' (filter ((/=0) . flip mod x) xs)


solve :: Int -> [Int] -> Int
solve n [] = n
solve n (p:ps)
    | n == p = n
    | n `mod` p == 0 = solve (n `div` p) primes
    | otherwise = solve n ps

main :: IO()
main = print $ solve 600_851_475_143 primes
