import json
#Create Like counting class
class LikeDB:
    def init(self, db_path):
        #Initialize the database
        #Open the database file if it exists, otherwise create a new database file
        self.db_path = db_path
        try:
            with open(db_path, 'r') as f:
                self.db = json.load(f)
        except FileNotFoundError:
            self.db = {}
            #Save the database to the database file
            with open(db_path, 'w') as f:
                json.dump(self.db, f, indent=4)
    
    def starting(self,chat_id,photo_id):
        if not (f'l{chat_id}' in self.db[photo_id].keys()):
            self.db[photo_id][f'l{chat_id}']={'likes':0,'dislikes':0}
        return None

    def save(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.db, f, indent=4)
    
    def all_likes(self,photo_id):
        """Counts all users likes
        returns
            all users likes
        """
        n=self.db[photo_id]['likes']
        return n
        
    def all_dislikes(self,photo_id):
        """Counts all users dislikes
        returns
            all users dislikes
        """
        n=self.db[photo_id]['dislikes']
        return n
    
    def pop_like(self,chat_id,photo_id):
        self.db[photo_id]['likes']=self.db[photo_id]['likes']-1
        self.db[photo_id][f'l{chat_id}']['likes']=0
        return None
    
    def pop_dislike(self,chat_id,photo_id):
        self.db[photo_id]['dislikes']=self.db[photo_id]['dislikes']-1
        self.db[photo_id][f'l{chat_id}']['dislikes']=0
        return None
        
        
    #Add a like to the database
    def add_like(self,user_id,photo_id)->dict:
        '''
        Add a like to the database
        args:
            user_id: The user id of the user who liked the post
        returns:
            The number of likes and dislikes for the post
        '''
        self.db[photo_id]['likes']+=1
        self.db[photo_id][f'l{user_id}']['likes']=1
        self.db[photo_id][f'l{user_id}']['dislikes']=0

  
    #Add a dislike to the database
    def add_dislike(self,user_id,photo_id)->dict:
        '''
        Add a dislike to the database
        args:
            user_id: The user id of the user who disliked the post
        returns:
            The number of likes and dislikes for the post
        '''
        self.db[photo_id]['dislikes']+=1
        self.db[photo_id][f'l{user_id}']['likes']=0
        self.db[photo_id][f'l{user_id}']['dislikes']=1


    def get_l_d(self,user_id,photo_id):
        return [self.db[photo_id][f'l{user_id}']['likes'],self.db[photo_id][f'l{user_id}']['dislikes']]

    def get_img(self,photo_id):
        if photo_id in self.db.keys():
            return None 
        else:
            self.db[photo_id]={}
            self.db[photo_id]={'likes':0,'dislikes':0}