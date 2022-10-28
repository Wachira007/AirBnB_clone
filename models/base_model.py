#!/usr/bin/python3
"""
defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


Class BaseModel:
    """
    defines all common attributes/methods for other classes
    """
    def __init__(self):
        """
        Instance initialization
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Instance string format"""
        temp = "[{}] {} {}"
        return .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dict containing all keys/values of __dict__ of the instance
        """
        
