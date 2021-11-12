fst2Eq :: Eq a => [a] -> Bool
fst2Eq (x : y : _) | x == y = True
fst2Eq _ = False

fst2Div :: (Eq a, Integral a) => [a] -> Bool
fst2Div (x : y : _) | y `mod` x == 0 = True
fst2Div _ = False

f_and_3_Div :: (Eq a, Integral a) => [a] -> Bool
f_and_3_Div (x : _ : y : _) | y `mod` x == 0 = True
f_and_3_Div _ = False
