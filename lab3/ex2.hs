sum' :: Num a => [a] -> a
sum' []     = 0
sum'(x:xs) = x + sum' xs

sumSqrt' :: Floating a => [a] -> a
sumSqrt' [] = 0
sumSqrt' (x:xs) = (sqrt x) + (sumSqrt' xs)  

sumWith :: (Num a, Num b) => (a -> b) -> [a] -> b
sumWith _ [] = 0
sumWith f (x:xs) = (f x) + (sumWith f xs) 

sum1    = sumWith id
sumSqr  = sumWith (^2) 
sumCube = sumWith (^3)
sumAbs  = sumWith abs
listLength = sumWith (\_ -> 1)

prod' :: Num a => [a] -> a
prod' []     = 1
prod' (x:xs) = x * (prod' xs)

prodWith :: (Num a, Num b) => (a -> b) -> [a] -> b
prodWith _ [] = 1
prodWith f (x:xs) = (f x) * (prodWith f xs)

prod     = prodWith id
prodSqr  = prodWith (^2)
prodCube = prodWith (^3)
prodAbs  = prodWith abs

accumulate :: Num a => (a -> b) -> (b -> b -> b) ->  b -> [a] -> b
accumulate f b start = acc 
    where acc [] = start 
          acc (x:xs) = b (f x) (acc xs)

sumSqrt = sumWith sqrt
prodSqrt = prodWith sqrt