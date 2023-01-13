# About
This is a monorepo to add AI and math stuff. At the time being I am not actively working on this kind of stuff which I love. In this setting I am using this repo as a random thought and implementation repository. Here I can place interesting docs and implementation ...

## Best practices for programming data analysis/ML projects

Ok Data-scientists and ML experts. Your field is one of the most beautiful fields today but is you code as beautiful?  
During the last year I engaged a lot with machine learning or even simpler data analysis tasks. The biggest strangle was to find the best way to structure my code. Functions calling functions and data that produced only once to elaborate my way of thinking was the norm. And after days of coding and multiple experiments the code turned to spaghetti. The analysis results where obvious and presentable but the code was far away from that. I was not even able to reuse any routine from that particular task even in other close related cases. At that time I questioned the way that I was working and thinking as a software engineer I tried to investigate that particular problem of code completeness ...

### What coding stands for?
1. A way to "communicatte" with some programmable interface in order to automate some particular tasks
2. A way to communicate with other people related to a specific task
3. A way to complete and self explained way to instanciate someone's thoughts to be revisable in the future

And I personally believe that these should be the basic principles that should be applied to any programming experience scientific
or not. Especially principles 2 and 3 are quite important to scientific programming such the ML one.

But what are these principles analyzed to?
1. Write programs for people, not computers
2. Automate repetitive tasks
3. Make incremental changes do use git!
4. DRY (Don't repeat your selves even others)
5. Embrace mistakes
6. Do it in an agile way
   
   Agile is a software development practice that starts with the end in the mind. Running multiple development cycles with each cycle
   aiming to provide a minimum viable product. Each cycle should end uo with an enhanced program version. 
   In this context do not start by optimizing your code at once! ... 

7. Document design and purpose not mechanisms - domain based documentation
   Consider the guys that need to consume the code that you provide. Do they need to know about **python iterators** or **data loading** is what they are looking for. 
   This is not something that assist others but yourself as well. Think your self a couple of months later revisiting some project build for medical image processing. The starting point of revisiting the code is the final report that you produced. The manuscript is written utilizing medical imaging terms, while your code base documentation is based on python terminology. What a mess!

8. Collaborate
   Collaboration is the key asset of any successful project. Ideas that are communicated are becoming stronger and get instanciated in ease. 
   Multipeer code reviews will provide more concrete and well justified implementations. Extra will be removed while code complexity will decrease
   due to the simplicity that multiparty collaboration obeys.
