f1 = (\x -> x - 2)
f2 = (\x y -> sqrt (x^2 + y^2))
f3 = (\x y z -> sqrt (x^2 + y^2 + z^2))

g1 = (\x -> 2 * x)
g2 = (\x -> x * 2)
g3 = (\x -> 2 ^ x)
g4 = (\x -> x ^ 2)
g5 = (\x -> 2 / x)
g6 = (\x -> x / 2)

abs_ =  (\x -> if x < 0 then -x else x)
const_ = (\x _ -> x)
id_ = (\x -> x)

f7 = (\x -> if x `mod` 2 == 0 then True else False )
f8 = (\x -> let y = sqrt x in 2 * y^3 * (y + 1) )
f9 = (\x -> if x == 1 then 3 else 0 )
