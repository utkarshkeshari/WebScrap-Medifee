# WebScrap-Medifee
This Code fetches data from http://www.medifee.com/dc-in-new-delhi.
medifee has a list of diagnostic centers (City Wise) and what type of diagnostic test they perform along with their price and offer available.

Just run the medifee.py file. it collects all the diagnostic center listed on website and stores the Name Address & Phone Number in "Diagnostic Centers in Delhi.txt" Seperated by |.

Code also stores the link associated with each Diagnostic Center in "links.txt"

Which is used to fetch the the Diagnostic Test details.

For each Diagnostic Center a Separate file is created with the same ID as of Diagnostic Center in "Diagnostic Centers in Delhi.txt"

The details in every file is also separated by |

