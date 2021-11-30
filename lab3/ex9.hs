sumWith g [] = 0
sumWith g (x : xs) = g x + sumWith g xs -- (+) (g x) (sumWith g xs)

prodWith g [] = 1
prodWith g (x : xs) = g x * prodWith g xs -- (*) (g x) (prodWith g xs)

sumWith' :: Num a => (a -> a) -> [a] -> a
sumWith' = go 0
  where
    go acc g [] = acc
    go acc g (x : xs) = go (g x + acc) g xs

prodWith' :: Num a => (a -> a) -> [a] -> a
prodWith' = go 1
  where
    go acc g [] = acc
    go acc g (x : xs) = go (g x * acc) g xs

foldr' :: (a -> b -> b) -> b -> [a] -> b
foldr' f = go
  where
    go acc [] = acc
    go acc (x : xs) = go (f x acc) xs

sumWith'' g = foldr' (\x acc -> g x + acc) 0

prodWith'' g = foldr' (\x acc -> g x * acc) 1

map' :: (a -> b) -> [a] -> [b]
map' f = foldl g []
  where
    g acc x = acc ++ [f x]

map'' :: (a -> b) -> [a] -> [b]
map'' f = foldr g []
  where
    g x acc = f x : acc