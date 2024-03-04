f :: Integer -> Integer -> Integer
f n k = f' (n - k) n n 0
    where
        f' 0 acc _ _ = acc
        f' nk acc lst i = case nk `mod` 2 of
            0 -> f' nk' acc lst i'
            1 -> f' nk' acc' nxt i'
            where
                nxt = lst - 2^i
                acc' = acc + nxt
                nk' = nk `div` 2
                i' = i + 1

main :: IO()
main = print $ f (toInteger 10^17) (toInteger 9^17)
