from collections import deque

def person_is_seller(person):
    if person[-1] == 'm':
        return(True)

def search(name):
    searched = []
    search_queue = deque()
    search_queue += graph[name]
    while search_queue:
        person = search_queue.popleft() 
        if not person in searched:
            if person_is_seller(person):
                print(person, 'is а mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

graph = {'you': ['Sara', 'Thomas', 'Lisam'], 'Sara': [], 'Thomas': [], 'Lisam':[]}
search('you')