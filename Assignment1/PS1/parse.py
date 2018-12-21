import csv
import ID3

def parse(filename):
  '''
  takes a filename and returns attribute information and all the data in array of dictionaries
  '''
  # initialize variables

  out = []  
  csvfile = open(filename,'r')
  fileToRead = csv.reader(csvfile)

  headers = next(fileToRead)

  # iterate through rows of actual data
  for row in fileToRead:
    out.append(dict(zip(headers, row)))
  return out

if __name__ == "__main__":  
    data= parse("house_votes_84.data")
    tree = ID3.ID3(data, 0)
    if tree != None:
        ans = ID3.prune(tree, [dict(Age='mid', Competition='no', Type='software', Class='up'), 
                              dict(Age='mid', Competition='yes', Type='software', Class='down'),
                              dict(Age='old', Competition='yes', Type='software', Class='up')])
        ID3.print_root(tree,"\t")
        if ans != 'up':
            print("ID3 test failed.")
        else:
            print("ID3 test succeeded.")
    else:
        print("ID3 test failed -- no tree returned")
