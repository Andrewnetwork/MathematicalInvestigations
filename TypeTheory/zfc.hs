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
    Conditions: 
    We are working with lists here, not sets. Our algorithms assume that our lists obey the properties of sets. In that 
    there are no duplicates and order doesn't matter. So if you provide a list that is not a set, don't expect it to work. 
    Proving equality over ordered lists is more complicated than it is for sets. (Why?)
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

{--
    Discussion. 

    In listEq we took in two functions and 
        returned False if they were of different length, 
        otherwise mapped and element-wise equvalence over the zipped lists (enforcing a one to one corespondence),
        and folded the list with and so all equalities must terminate in True for the lists to be equal and False for them not to be.
    
    The listEq function uses the equality between two elements in the computation. We can, however, avoid invoking the notion of equality at all. 
    I do this in the next function listEq'. 
    
--}

-- Without equality. 
listEq' [] [] = True
listEq' [l1] [] = False
listEq' [] [l2] = False
listEq' l1 l2 = (elem (head l1) l1 && (elem (head l1) l2)) && (listEq' (tail l1) (tail l2) )

{--
    Discussion. 

    Here in listEq' we do not invoke the notion of element equality at all. We simply use the "isElementOf" operation and build up a list of boolean cases 
    which are and'ed over, and equate to checking that if an element is in l1 it implies it is in an emlement in l2. We will now use this function
    on a set of small lists and illustrate each step in the logic. 
--}

-- listEq' [1,2,3] [3,3,3]
-- 1: (elem 1 [1,2,3]) && (elem 1 [3,3,3]) = (1 && 0) = 0
-- 2: (elem 2 [2,3]) && (elem 2 [3,3])     = (1 && 0) = 0
-- 3: (elem 3 [3]) && (elem 3 [3])         = (1 && 1) = 1
-- 4: 0 && 0 && 1 && (Base Case)