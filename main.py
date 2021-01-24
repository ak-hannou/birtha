from overview import Overview
from interactions import Interactions
from reviews import Reviews
import shutil 

name = "ortho micronor"
drugOverview = Overview("https://www.drugs.com/mtm/ortho-micronor.html", name)
drugOverview.buildOverview()

drugInteraction = Interactions("https://www.drugs.com/drug-interactions/norethindrone,ortho-micronor.html", name)
drugInteraction.buildInteractions()

drugReviews = Reviews("https://www.drugs.com/comments/norethindrone/ortho-micronor.html",name)
drugReviews.buildReviews()

shutil.move(name+'.txt', 'minipills')