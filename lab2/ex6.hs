{-# LANGUAGE BangPatterns #-}

fib :: (Num a, Eq a) => a -> a
fib n =
  if n == 0 || n == 1
    then n
    else fib (n - 2) + fib (n - 1)

fibs = 0 : 1 : zipWith (+) fibs (tail fibs) :: [Int]

fib2 :: Int -> Int
fib2 n = fibs !! n

sum' :: Num a => [a] -> a
sum' [] = 0
sum' (x : xs) = x + sum' xs

prod' :: Num a => [a] -> a -- prod' [1,2,3] = 6
prod' [] = 0
prod' (x : xs) = x * prod' xs

length' :: [a] -> Int -- length' [1,1,1,1] = 4
length' [] = 0
length' (x : xs) = 1 + length' xs

or' :: [Bool] -> Bool -- or' [True, False, True] = True
or' [] = True
or' (x : xs) = x || or' xs

and' :: [Bool] -> Bool -- and' [True, False, True] = False
and' [] = True
and' (x : xs) = x && and' xs

elem' :: Eq a => a -> [a] -> Bool -- elem' 3 [1,2,3] = True
elem' n [] = False
elem' n (x : xs) = n == x || elem' n xs

doubleAll :: Num t => [t] -> [t] -- doubleAll [1,2] = [2,4]
doubleAll [] = []
doubleAll (x : xs) = (2 * x) : doubleAll xs

squareAll :: Num t => [t] -> [t] -- squareAll [2,3] = [4,9]
squareAll [] = []
squareAll (x : xs) = (x ^ 2) : doubleAll xs

selectEven :: Integral t => [t] -> [t] -- selectEven [1,2,3] = [2]
selectEven [] = []
selectEven (x : xs) = if even x then [] else x : selectEven xs

sum'2 :: Num a => [a] -> a
sum'2 xs = loop 0 xs
  where
    loop acc [] = acc
    loop acc (x : xs) = loop (x + acc) xs

sum'3 :: Num a => [a] -> a
sum'3 = loop 0
  where
    loop acc [] = acc
    loop acc (x : xs) = loop (x + acc) xs

prod'2 :: Num a => [a] -> a
prod'2 [] = 0
prod'2 tab = loop 1 tab
  where
    loop acc [] = 1
    loop acc (x : xs) = loop (acc * x) xs

length'2 :: [a] -> Int
length'2 = loop 0
  where
    loop acc [] = acc
    loop acc (x : xs) = loop (1 + acc) xs

sum'4 :: Num a => [a] -> a
sum'4 = loop 0
  where
    loop !acc [] = acc
    loop !acc (x : xs) = loop (x + acc) xs