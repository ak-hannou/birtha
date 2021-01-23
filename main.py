from overview import Overview
from interactions import Interactions
from reviews import Reviews
drugOverview = Overview("https://www.drugs.com/yasmin.html", "yasmin")
drugOverview.buildOverview()

drugInteraction = Interactions("https://www.drugs.com/drug-interactions/drospirenone-ethinyl-estradiol,yasmin.html", "yasmin")
drugInteraction.buildInteractions()

drugReviews = Reviews("https://www.drugs.com/comments/drospirenone-ethinyl-estradiol/yasmin.html","yasmin")
drugReviews.buildReviews()