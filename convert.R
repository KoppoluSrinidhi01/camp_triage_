# Load the RData file
load("camp_triage/data/yourfile.RData")

# Check objects inside the RData file
ls()

# Suppose the dataset name printed is triage_data
write.csv(triage_data, "camp_triage/data/triage_data.csv", row.names = FALSE)