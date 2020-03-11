import datetime
last_id = 0

class Note():
    """
    memo, creation_date, tags

    """
    def __init__(self,memo,tags=""):
        """
        Initialize  a note with memo and optional separated
        tag, automaticaly setting the creating date and 
        the unique id.

        """
        self.memo = memo
        self.tags= tags

        self.creation_date = datetime.date.today()
        global last_id #for setting the unique vale to each note
        last_id += 1
        self.id = last_id
    

    def match(self, filter):
        """
        determining if the note matches with the filtered text
        return true if match or flase.

        """
        return filter in self.memo or filter in self.tags




class Notebook():
    '''
    It has collection of notes that can be 
    changed modified and tagged
    '''

    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=""):
        self.notes.append(Note(memo,tags))
    
    def modify_note(self, note_id, memo):
        """
        finding the note with givne id and chainging the 
        memo
        """
        for note in self.notes:
            if (note.id == note_id):
                note.memo = memo
                break
        
    def modify_tags(self, note_id, tags):
        """
        finding th note with given id and
        changing the tag
        """

        for note in self.notes:
            if(note.id == note_id):
                note.tags = tags

    def search(self,filter):
        """
        find all the notes that matches
        """
        return [note for note in self.notes if 
        note.match(filter)] 

    
    def _find_note(self, note_id):
        '''
        locate the note with given id
        '''
        for note in self.notes:
            if (note.id == note_id):
                return note
            return None  
    
    def modify_memo(self, note_id,memo):
        '''
        find the note ancchange the vlaues 
        of the memo
        '''
        self._find_note(note_id).memo=memo


class Menu():
    def __init__(self):
        self.notebook = Notebook()
        self.choices ={
            "1" :self.show_notes,
            "2" :self.search_notes,
            "3" :self.add_note,
            "4" :self.modify_note,
            "5" :self.quit
        }

    def display_menu(self):
        print("""Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit """)

    def run(self):
        """dispalying  the menu and running according to the
        chocies
        """
        while True:
            self.display_menu()
            choice = input("Enter an option")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("Not a valid choice")
            
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes 
        for note in notes:
            print("{0}: {1} \n{2}".format(
                note.id, note.tags, note.memo
            ))
    
    def search_notes(self):
        filter = input("search for ?")
        notes = self.notebook.search(filter)

    def add_note(self):
        memo = input("addtion Memo")
        self.notebook.new_note(memo)
        print("Notebon updated")
    

    def modify_note(self):
        id = input("Enter he id")
        memo = input("Enter memo")
        tags = input("Enter the tag")

        if memo:
            self.notebook.modify_memo(id,memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Will see you tomorrow")
        sys.exit(0)
if __name__ =='__main__':
    Menu().run()



        
            



