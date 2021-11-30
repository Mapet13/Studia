sqr x = x^2

funcFactory n = case n of
 1 -> id
 2 -> sqr
 3 -> (^3)
 4 -> \x -> x^4
 5 -> intFunc
 _ -> const n
 where
   intFunc x = x^5

expApproxUpTo :: Int -> Double -> Double
expApproxUpTo 0 _ = 1
expApproxUpTo n x = ((x^n) / (fromIntegral(factorial))) + (expApproxUpTo (n-1) x)
    where factorial = foldr (*) 1 [1..n]  

dfr :: (Double -> Double) -> Double -> (Double -> Double)
dfr f h = df
  where df x = (f(x + h) - f(x)) / h

dfc :: (Double -> Double) -> Double -> (Double -> Double)
dfc f h = df
  where df x = (f(x + h) - f(x - h)) / (2 * h)