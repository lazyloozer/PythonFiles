#wapp to read the content from the document Text1.txt:
'''f1=open("text2.txt",'r')
print(f1.read())'''
#wapp to write the content into the document text1.txt
'''f2=open('Text2.txt','w')
f2.write('Some content we are writing into text1.txt Document')
f2.close()'''
#Wapp to append the content'Hello from File Handling'into Text1.txt
f3=open('Text2.txt','a')
f3.write("Hello world")
f3.close();

#wapp to copy the content from Text1.txt to Text2.txt:

f4=open('text1.txt','r')
f5=open('Text2.txt','w')
for i in f4:
    f5.write(i)
f5.close()
