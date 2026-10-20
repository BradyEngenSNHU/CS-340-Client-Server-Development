# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        USER = username
        PASS = password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)]             

    def create(self, data):
        """ adds the specified document to the database
            :return: returns true if successful, else false
        """
        if data is not None: 
            try:
                insert_result = self.collection.insert_one(data)# I made the insert statement
            except:
                print("Error, could not create")
        else:                                                       
            raise Exception("Nothing to create, because data parameter is empty") 
            
        return insert_result.acknowledged

    
    def read(self, data):
        """ reads all documents that fit the input data
            :return: returns all the documents found as a list
        """
        if data is not None:
            read_result = self.collection.find(data)
            
        else:
            raise Exeption("Nothing to read, because data parameter is empty")
        
        return list(read_result)
    
    
    def update(self, findData, updateData):
        """ updates all documents with that match the first input 
            with the data provided in the second input
            :return: returns the amount of successful updates
        """
        if findData is not None and updateData is not None:
            try:
                update_result = self.collection.update_many(findData, {"$set": updateData})
            except:
                print("Error updating")
        else:
            raise Exception("Nothing to update, because a data parameter is empty")
            
        return update_result.modified_count
    

    def delete(self, data):
        """ deletes all documents that are found from the input data
            :return: returns the amount of documents deleted
        """
        if data is not None:
            try:
                delete_result = self.collection.delete_many(data)
            except:
                print("Error deleting")
        else:
            raise Exceptin("Nothing to delete, because data parameter is empty")
            
        return delete_result.deleted_count
    
    
    def test(self):
        print(self.collection.find_one())