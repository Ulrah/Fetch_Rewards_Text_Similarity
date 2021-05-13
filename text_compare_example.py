
# Author: Jacob Blair Morris
# Date: 05/13/2021

'''
    This program is intended to demonstrate usage of Text_Compare class using a range of values for shingle_factor
'''

from text_compare import Text_Compare

samples = {
    "sample_1" : "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you.",
    "sample_2" : "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you.",
    "sample_3" : "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way.",
    "empty" : '',
    "dogs" : "My dogs love fetch rewards !", # should have 0.0 similarity, since "fetch rewards" != "Fetch Rewards" and "love" != "love."
    "garbage" : "sldkj;fs ABCD\nabcd  dkkdl dllfl"
}

# compares sample_1 to all samples (including itself), using a range of shingle_factors
for shingle_factor in range( 1, 4 ) :
    base_text = Text_Compare( samples["sample_1"], shingle_factor = shingle_factor )
    print( "\nUsing shingle_factor = " + str( shingle_factor ) + "..." )
    
    for sample_name in samples :
        similarity = base_text.compare( samples[sample_name] )
        print( "sample_1 vs " + sample_name + " : " + str( similarity ) )
