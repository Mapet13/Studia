doubleElems []     = []
doubleElems (x:xs) = 2 * x : doubleElems xs

map' :: (a -> b) -> [a] -> [b]
map' f = mapIt
    where mapIt [] = []
          mapIt (x:xs) = f x : mapIt xs 

sqrElems = map (^2)   

evalFuncListAt :: a -> [a -> b] -> [b]
evalFuncListAt x = map ($x)