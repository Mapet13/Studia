-- [(i, j, k) | i <- [1..100], j <- [1..100], k <- [1..100], i^2 + j^2 == k^2 && i <= j && j <= k]

-- isPrime :: Integral t => t -> Bool
-- isPrime n = [i | i <- [2 .. n - 1], n `mod` i == 0] == []

-- foldr (\i acc -> acc + (if (isPrime i) then 1 else 0) ) 0 [2..10000]

primes :: [Int]
primes = eratoSieve [2 ..]
  where
    eratoSieve :: [Int] -> [Int]
    eratoSieve (p : xs) = p : eratoSieve [x | x <- xs, x `mod` p /= 0]

isPrime :: Int -> Bool
isPrime n = inPrimes n primes
  where
    inPrimes :: Int -> [Int] -> Bool
    inPrimes n (x : xs)
      | n < x = False
      | n == x = True
      | otherwise = inPrimes n xs

countPrimes :: Int -> Int
countPrimes n
  | n < 2 = 0
  | otherwise = foldr (\i acc -> acc + (if isPrime i then 1 else 0)) 0 [2 .. n]

allEqual :: Eq a => [a] -> Bool
allEqual [] = True
allEqual (x : xs) = eqWith x xs
  where
    eqWith :: Eq a => a -> [a] -> Bool
    eqWith x [] = True
    eqWith x (head : xs)
      | x == head = eqWith x xs
      | otherwise = False