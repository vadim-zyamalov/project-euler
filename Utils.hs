module Utils (
    enum,
    primes,
    fib,
    combinations,
    combinationsR,
    permutations,
    permutations',
    gcd',
    lcm',
    gcdL,
    lcmL
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

gcd' :: Integral a => a -> a -> a
gcd' x 0 = x
gcd' x y = gcd' ay (ax `mod` ay)
    where
        ay = abs y
        ax = abs x

gcdL :: Integral a => [a] -> a
gcdL [x] = x
gcdL (x:y:xs) = gcdL (gcd x y : xs)

lcm' :: Integral a => a -> a -> a
lcm' x 0 = x
lcm' 0 x = x
lcm' x y = abs (x * y) `div` gcd' x y

lcmL :: Integral a => [a] -> a
lcmL [x] = x
lcmL (x:y:xs) = lcmL (lcm x y : xs)
