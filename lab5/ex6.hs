{-# LANGUAGE DeriveFunctor #-}

newtype Box a = MkBox a deriving (Show, Functor)

data MyList a
  = EmptyList
  | Cons a (MyList a)
  deriving (Show, Functor)

data BinTree a
  = EmptyBT
  | NodeBT a (BinTree a) (BinTree a)
  deriving (Show)

instance Functor BinTree where
  fmap _ EmptyBT = EmptyBT
  fmap f (NodeBT root left right) = NodeBT (f root) (fmap f left) (fmap f right)