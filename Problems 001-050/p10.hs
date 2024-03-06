import Utils (primesTo)

main :: IO()
main = print $ sum $ primesTo 2_000_000
