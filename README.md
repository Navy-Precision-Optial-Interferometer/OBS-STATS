# OBS-STATS

## Current Status of Spreadsheet (made using observing_stats.ipynb/manual editing)

The current data I have collected in the spreadsheet is:

- UT date PER STARLOG HEADER (so sometimes a date is repeated multiple times)
- Observer (manually edited where no observer listed - taken from starlog)
- Total number of scans
- Seeing (Overall range for the night, manually recorded from ObsLogs night summary)
- Number of observations by TYPE (C, B, ., I, A, F, etc) and by WAY (2-6). (First determined by associating each starlog with the obsList that was "current" at that time, and then manually revised by looking at individual star/obsLogs)
- Scheduled nights - was someone scheduled for observing that night based on Sextans/Deputy/Confluence (Y/N), were any on-sky scans obtained that night (Y/N), relevant notes (technical issues, fire shutdown, etc.) (This data all manually gathered).

Current analytics:

- Time spent observing (calculated as time of last scan - time of first scan)
- Average scans per hour (Currently just total scans/time spent observing, no allowance for breaks due to weather, tech issues, etc., only calculated if >=2 scans but still some outlier values)
- Total number and maximum number of scans per observer
- Number of scans by TYPE (stellar, alp Lab, FTS, other)
- Number of scans by WAY (2-6)
- Number of scheduled nights, number of scheduled and on-sky nights, number of scheduled and not on sky nights, number of not scheduled but on sky nights, number of not scheduled and not on sky nights
- Specific notes on why we weren't on sky if applicable, as well as a single letter code system: "T" = Technical Issues, "W" = Weather, "E" = Engineering, and "M" = miscellaneous (holiday, observer sick/unavailable, etc) for charting purposes
- Scans per night over time
- 
Analytics TO-DO:

- Average number of nights on sky per week
- Average seeing?/ seeing over time (may require more granular seeing information scraping from logs)
- More precise scans per hour calculation
- How often FTS scans performed vs. how often spec translation required
- How many science targets were observed on a night out of those on the obslist? How many had a full minimum sequence of observations?
- How many science targets per week/month/year on average, out of total?


Possible Changes to Logging Procedures to Facilitate Analytics Gathering:

- Standardized logging of current seeing and final "seeing over the night"
- Record at end of obsLog what obsList was used/what way data was mostly recorded in
- Have javacon pull the CURRENTLY LOADED obslist upon startup rather than the most recent obslist
- If obslist changes during the night standardize the notation of that in the log so that can have the information when analyzing starlog

## Current Status of One Night Observing code

- Purpose of this is to refine the code used to perform the statistical analysis for 2020-2021 into something that can be used on a night to night basis to generate standardized reports, automate as much as possible/really dig down into what can be calculated with the logs in the current format and what requires changes
- Uses the StarLog, ObsLog, AND ObsList for a given night

### What it currently does
- Gets observer name from the first header in the ObsLog rather than the header of the StarLog since sometimes the StarLog is blank
- Parses the obslist to create a dictionary of star names, their type (., B, C, etc), and their group number.
- Parses the obslist to find the required photometric combinations and create a dictionary of the strings an observer may use in the comments to note these in the logs, to help check whether a "complete" observation of the star was made. For each science target and its calibrator, checks whether each of the photometrics was taken.
- Parses starlog: splits at each header, inserts an "X" for star type (., B, C, etc) if blank, and creates dictionary of obs number, obs type, the star names, the UT times, and observer comments
- Calculates time spent observing: splits log entries at points where observations are more than half an hour apart, then calculates the sum of the length of each chunk
- Calculates average scans per night by calculating average scans per hour for each chunk described above and then averages all of these together

### To-Do
- Report of how many science targets of the total were observed, how many scans for each/average scans per target, was a total sequence taken
- Pull seeing information over the night, report average?
- Consolidate all statistics into a single report - need to decide on format
