
-- 16.2
-- Word Frequencies
--
-- Design a method to find the frequency of occurrences of any given
-- word in a book. What if we were running this algorithm multiple
-- times?
--


import qualified Data.List


sol1 book =
    id
    . map (\ x -> (head x, length x))
    . Data.List.groupBy (==)
    . Data.List.sort
    . words
    $ book

