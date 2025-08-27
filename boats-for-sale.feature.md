# Feature: Boats for Sale on Craigslist
New Feature in the For Sale section on Craigslist

## Scenario 1: Navigate to Craigslist and verify the new ‘boats’ link is available in the For Sale section.
WHEN you navigate to miami.craigslist.org
THEN you see a ‘boats’ link that is available in the ‘for sale’ section

## Scenario 2: Navigate to the boats for sale section
GIVEN you have navigated to miami.craigslist.org
WHEN you click on the ‘boats’ link in the ‘for sale’ section
THEN you are directed to a page with boats for sale

## Scenario 3: Apply filter for 'Sailboat' type having been manufactured starting from year '2010'
GIVEN you have navigated to the boats for sale page
AND you have entered ‘2010’ in the ‘year manufactured’ (min) field
AND you have selected ‘boat type’ = 'sailboat'
WHEN you click on the 'apply' button on the left side of the screen (same general area where 'boat type' and 'year manufactured' are, but lower in the page)
THEN you should see results filtered accordingly (sailboats 2010 or newer)
AND you should see 14 results
