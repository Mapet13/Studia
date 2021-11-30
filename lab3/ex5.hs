import Data.List

sortDesc :: Ord a => [a] -> [a]
sortDesc = reverse . sort

are2FunsEqAt :: Eq a => (t -> a) -> (t -> a) -> [t] -> Bool
are2FunsEqAt f g = check
    where check [] = True
          check (x:xs) = f x == g x && check xs

infixl 9 >.>
(>.>) :: (a -> b) -> (b -> c) -> (a -> c)
g >.> f = f . g

composeFunList :: [a -> a] -> (a -> a)
composeFunList = foldr (.) id



