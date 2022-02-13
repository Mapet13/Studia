data BinIntTree
  = EmptyIntBT
  | IntNodeBT Int BinIntTree BinIntTree

sumBinIntTree :: BinIntTree -> Int
sumBinIntTree EmptyIntBT = 0
sumBinIntTree (IntNodeBT n lt rt) = n + sumBinIntTree lt + sumBinIntTree rt

data BinTree a
  = EmptyBT
  | NodeBT a (BinTree a) (BinTree a)

sumBinTree :: (Num a) => BinTree a -> a
sumBinTree EmptyBT = 0
sumBinTree (NodeBT n lt rt) = n + sumBinTree lt + sumBinTree rt

data Expr a
  = Lit a -- literal/value a, e.g. Lit 2 = 2
  | Add (Expr a) (Expr a)

eval :: Num a => Expr a -> a
eval (Lit n) = n
eval (Add e1 e2) = eval e1 + eval e2

show' :: Show a => Expr a -> String
show' (Lit n) = show n
show' (Add e1 e2) = "(" ++ show' e1 ++ "+" ++ show' e2 ++ ")"

depthOfBT :: BinTree a -> Int -- głębokość drzewa binarnego
depthOfBT EmptyBT = 0
depthOfBT (NodeBT _ lt rt) = 1 + depthOfBT lt + depthOfBT rt

flattenBtPre :: BinTree a -> [a] -- napisać trzy wersje: preorder, inorder, postorder
flattenBtPre EmptyBT = []
flattenBtPre (NodeBT node lt rt) = [node] ++ flattenBtPre lt ++ flattenBtPre rt

flattenBtIn :: BinTree a -> [a] -- napisać trzy wersje: preorder, inorder, postorder
flattenBtIn EmptyBT = []
flattenBtIn (NodeBT node lt rt) = flattenBtIn lt ++ [node] ++ flattenBtIn rt

flattenBtPost :: BinTree a -> [a] -- napisać trzy wersje: preorder, inorder, postorder
flattenBtPost EmptyBT = []
flattenBtPost (NodeBT node lt rt) = flattenBtPost lt ++ flattenBtPost rt ++ [node]

mapBT :: (a -> b) -> BinTree a -> BinTree b -- funkcja map dla drzewa binarnego
mapBT _ EmptyBT = EmptyBT
mapBT f (NodeBT value lt bt) = NodeBT (f value) (mapBT f lt) (mapBT f bt)

insert :: Ord a => a -> BinTree a -> BinTree a
insert val EmptyBT = NodeBT val EmptyBT EmptyBT
insert val (NodeBT node lt rt)
  | val < node = NodeBT node (insert val lt) rt
  | otherwise = NodeBT node lt (insert val rt)

list2BST :: Ord a => [a] -> BinTree a
list2BST = l2BT EmptyBT
  where
    l2BT bt [] = bt
    l2BT bt (x : xs) = l2BT (insert x bt) xs

occurs :: Eq a => a -> BinTree a -> Int
occurs _ EmptyBT = 0
occurs x (NodeBT node lt rt) = count + occurs x lt + occurs x rt
  where
    count = if x == node then 1 else 0

elemOf :: Eq a => a -> BinTree a -> Bool
elemOf _ EmptyBT = False
elemOf x (NodeBT node lt rt)
  | x == node = True
  | otherwise = elemOf x lt || elemOf x rt

reflect :: BinTree a -> BinTree a
reflect EmptyBT = EmptyBT
reflect (NodeBT node lt rt) = NodeBT node rt lt

minElemOf :: Ord a => BinTree a -> a
minElemOf EmptyBT = error "No elements in that BT!"
minElemOf (NodeBT node lt rt) = min (minFrom lt) (minFrom rt)
  where
    minFrom EmptyBT = node
    minFrom bt = min node (minElemOf bt)

maxElemOf :: Ord a => BinTree a -> a
maxElemOf EmptyBT = error "No elements in that BT!"
maxElemOf (NodeBT node lt rt) = max (maxFrom lt) (maxFrom rt)
  where
    maxFrom EmptyBT = node
    maxFrom bt = max node (maxElemOf bt)

foldBinTree :: (a -> b -> b -> b) -> b -> BinTree a -> b
foldBinTree _ start EmptyBT = start
foldBinTree f start (NodeBT node lt rt) =
  f node (foldBinTree f start lt) (foldBinTree f start rt)


  