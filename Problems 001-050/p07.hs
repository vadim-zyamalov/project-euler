import Utils (primes)

main :: IO()
main = print $ primes !! 10_000
