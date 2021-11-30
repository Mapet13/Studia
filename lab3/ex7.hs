onlyEven [] = []
onlyEven (x:xs)
 | even x = x : onlyEven xs
 | otherwise = onlyEven xs

filter' :: (a -> Bool) -> [a] -> [a]
filter' f = filterThat
    where filterThat [] = []
          filterThat (x:xs)
            | f x = x : filterThat xs
            | otherwise = filterThat xs
    
onlyEven1 = filter even