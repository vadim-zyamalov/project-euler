import Utils ( combinationsR )

isPalyndrome :: Int -> Bool
isPalyndrome n = n == revN n 0
    where
        revN 0 acc = acc
        revN x acc = revN nx nacc
            where
                nx = x `div` 10
                d = x `mod` 10
                nacc = 10 * acc + d

solve :: Int
solve = maximum . filter isPalyndrome . map product . combinationsR 2 $ [999,998..100]

main :: IO()
main = print solve
