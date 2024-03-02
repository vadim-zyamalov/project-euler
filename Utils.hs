module Utils (
    enum,
    primes,
    fib,
    combinations,
    combinationsR,
    permutations,
    permutations'
    ) where

enum :: [a] -> [(Int, a)]
enum = zip [0..]

primes :: [Int]
primes = primes' [2..]
    where
        primes' (x:xs) = x : primes' (filter ((/=0) . flip mod x) xs)

fib :: [Int]
fib = 1 : 1 : zipWith (+) fib (tail fib)

combinations :: Int -> [a] -> [[a]]
combinations 0 _      = [[]]
combinations _ []     = []
combinations n (x:xs) = map (x :) (combinations (n - 1) xs) ++ combinations n xs

combinationsR :: Int -> [a] -> [[a]]
combinationsR 0 _           = [[]]
combinationsR _ []          = []
combinationsR n allx@(x:xs) = map (x :) (combinationsR (n - 1) allx) ++ combinationsR n xs

permutations :: [a] -> [[a]]
permutations xs = permutations' (length xs) xs

permutations' :: Int -> [a] -> [[a]]
permutations' 0 _  = [[]]
permutations' _ [] = []
permutations' n xs = concatMap (\(i, x) -> map (x :) (ps' i xs)) ixs
    where
        ixs = enum xs
        ps' i els = permutations' (n - 1) $ map snd $ filter (\(j, _) -> j /= i) ixs
