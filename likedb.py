import json

class LikeDB:
    def __init__(self, filename):
        self.filename = filename
        self.data = {
            'likes': {},
        }
        try:
            with open(filename, 'r') as f:
                self.data = json.load(f)
        except :
            with open(filename, 'w') as f:
                json.dump(self.data, f)
        # 

    def get_likes(self, user_id: int) -> list:
        """
        Returns a list of user_ids that the given user_id has liked
        
        args:
            user_id (int): The user_id of the user to get likes for

        returns:
            list: A list of user_ids that the given user_id has liked
        """

        pass

    def add_like(self,user_id:int,message_id:int) -> None:
        """
        Adds a like to the database and removes any dislikes

        args:
            user_id (int): The user_id of the user who liked the message
            message_id (int): The message_id of the message that was liked
        """

        pass

    def diselike(self,user_id:int,message_id:int) -> None:
        """
        Removes a like from the database and adds a dislike

        args:
            user_id (int): The user_id of the user who disliked the message
            message_id (int): The message_id of the message that was disliked
        """

        pass

like = LikeDB('like.json')

    
        