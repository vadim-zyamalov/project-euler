type Cache = [(Int, Int)]

fib :: Int -> Cache -> (Int, Cache)
fib 0 ch = (1, ch)
fib 1 ch = (1, ch)
fib n ch = case lookup n ch of
    Just r -> (r, ch)
    Nothing -> let (r0, ch0) = fib (n - 1) ch
                   (r1, ch1) = fib (n - 2) ch0
                   r = r0 + r1
               in (r, (n, r) : ch1)

seqFib :: Int -> Int -> Int -> Cache -> Int
seqFib n beg acc ch = let (nxt, nxtch) = fib beg ch
    in (if nxt >= n
        then acc
        else if even nxt
            then seqFib n (beg + 1) (acc + nxt) nxtch
            else seqFib n (beg + 1) acc nxtch)

main :: IO()
main = print $ seqFib 4_000_000 0 0 []
