library(dplyr)

# Download file from URL and store the filenames in temporary character strings
download.file("http://www.ssa.gov/oact/babynames/state/namesbystate.zip",
              temp <- tempfile())

# Unzip the downloaded file in babies directory, overwrite if already exists
unzip(temp,
      files = NULL ,
      exdir = "babies",
      overwrite = TRUE)

# Collect data read from each Text file
collectData <-
  do.call(rbind, lapply(list.files( # Rbind combines data by rows
    path = "babies",                # Lapply outputs the names of the list of files
    pattern = "*.TXT",
    full.names = TRUE
  ),

  function(e) {
    dataFrame <- read.table(e, header = FALSE, sep = ",")
  }))

# Set the column names in collectData object
colnames(collectData) = c("State", "Sex", "Year", "Name", "Occurences")

# CollectData of Name and Occurences column
dataFrame = collectData[, 4:5]

# Tests character objects
dataFrame$Name = as.character(dataFrame$Name)

# Group collected data by Name
groupData = group_by(dataFrame, Name)
#summaryData <- data.frame(aggregate(dataFrame, by = list(dataFrame$Name, dataFrame$Occurences), FUN = max))

# Add occurences of all names and collect them in a data frame
summaryData = data.frame(summarize(groupData, sum(Occurences)))

# Sort with Occurences of names in descending order
arrangeData = arrange(summaryData, desc(summaryData$sum.Occurences))

# Print the result
print(paste("Most popular baby name is:", arrangeData$Name[1], "with", arrangeData$sum.Occurences[1], "occurences"))
