type Cache = [(Int, Int)]

fibEven :: Int -> Cache -> (Int, Cache)
fibEven 0 ch = (2, ch)
fibEven 1 ch = (8, ch)
fibEven n ch = case lookup n ch of
    Just r -> (r, ch)
    Nothing -> let (r0, ch0) = fibEven (n - 1) ch
                   (r1, ch1) = fibEven (n - 2) ch0
                   r = 4 * r0 + r1
              in (r, (n, r) : ch1)

seqFibEven :: Int -> Int -> Int -> Cache -> Int
seqFibEven n beg acc ch = let (nxt, nxtch) = fibEven beg ch
    in if nxt >= n
        then acc
        else seqFibEven n (beg + 1) (acc + nxt) nxtch

main :: IO()
main = print $ seqFibEven 4_000_000 0 0 []
