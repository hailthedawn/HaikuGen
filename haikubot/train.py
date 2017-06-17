#builds the model from existing data
import inspect,os
import markovify
from textstat.textstat import textstat

#Read files from directory
#Add their contents to a single string
#Make a model from this string
#generate first sentence from this model

#
#"C:\CS Stuff\HaikuGen\\tests\Wordsworth.txt"
class train():
    dir=os.path.dirname(os.path.dirname(os.path.abspath(inspect.stack()[0][1])))

    def __init__(self,line_limits=[5,7,5],file1=os.path.join(dir,"tests\Macbeth-Shakespeare.txt"),file2=os.path.join(dir,"tests\Wordsworth.txt")):
        self.line_limits=line_limits
        self.file1=file1
        self.file2=file2


    def main(self):
        f1 = open(self.file1)
        text = f1.read()

        f2 = open(self.file2)
        text += f2.read()

        textModel = markovify.NewlineText(text)
        haiku=""
        for i in range(0,3):
            while True:
                sent=textModel.make_sentence()
                if(not sent==None) and (textstat.syllable_count(sent)<self.line_limits[i]):
                    haiku+=sent+"\n"
                    break

        print(haiku)

if __name__=="__main__":
    train.main(train())