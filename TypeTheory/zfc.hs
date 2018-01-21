{--
    zfc.hs 
    Andrew Ribeiro 
    January 2018
    MIT Licence

    This file contains a series of functions that aim to impelment the axioms of 
    Zermelo–Fraenkel set theory in Haskell. They are true to the form of the ZFC axioms in 
    that only operations allowed in the set theoretic formulation are allowed in the functions
    implemented here. 
--}
{--
    As an example, let's begin with the axiom of extensionality, which is a type of equality between two 
    sets by proving they have the same elements. There is a bit of a lie in saying eqality, as we can 
    define this propery by pure logic. As we will see, this is one of the first striking things we can 
    implement in Haskell with some great fidelity. 
--}
{--
    # Axiom of extensionality
    Two sets are equal (are the same set) if they have the same elements.
--}

-- With Equality. 
elmEq (x,y) = x == y

listEq l1 l2
    | ( (length l1) /= (length l2) ) = False 
    | otherwise = foldr (&&) True (map elmEq (zip l1 l2))

-- Without equality. 
listEq' [] [] = True
listEq' [l1] [] = False
listEq' [] [l2] = False
listEq' l1 l2 = (elem (head l1) l1 && (elem (head l1) l2)) && (listEq' (tail l1) (tail l2) )

{--
    Discussion. 

    
--}