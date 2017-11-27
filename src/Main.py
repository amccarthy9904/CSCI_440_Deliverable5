#TODO:
#write SQL Queries
#use queries on database
#store data from queries
#run analysis on data for each question
#visualize results
import Query
import Analysis

if __name__ == '__main__':
    query = Query.Query()
    results = query.run_queries()
    analizer = Analysis.Analyzer()
    for index in range(4):
        analizer.analize(results[index], index)