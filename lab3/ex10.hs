isSortedAsc :: Ord a => [a] -> Bool
isSortedAsc xs = foldl (\acc (x, y) -> acc && (x <= y)) True (zip xs (tail xs))

everySecond :: [t] -> [t]
everySecond xs = map fst $ filter (\(_, x) -> odd x) $ zip xs [1 ..]