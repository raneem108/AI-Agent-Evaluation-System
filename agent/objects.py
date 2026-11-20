from pydantic import BaseModel, Field

class Answer(BaseModel):#the answer structure
    answer:str = Field(description= "the answer that is needed for the question")
    conversation:bool = Field(description="This is an indicator to know if the conversation"\
                              "should still continue or no. if the agent has made the decision about the refund this should be False"
                              "if the conersation still need more talk then it's true", default=True)

class PurchaseItem(BaseModel):
    name:str =Field(description="name of the item puchased")

