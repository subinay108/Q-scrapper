# Website URLs:
1. https://textbookplus.in/thank-you-maam-long-question-answer/
    - selector: div.entry-content
2. https://www.englishshyamsir.com/thank-you-maam-question-answer/
    - selector: div.entry-content, div.clear
3. https://edutricks.in/thank-you-maam-question-answers-descriptive-type/
    - selector: div.entry-content

# Define the problem
- input a URL and scrap the Quetion-Answer Text and then write it into a HTML file

# Steps to solve
- input a URL
- Extract domain using re r'^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)'
- Check whether the URL is in our list or not
- If URL is in our list then choose the selector
- If URL is not present in our list then ask for new selector or try the common selector
- Scrap the selected element and create a text file with html extension
- Name the file properly

# Steps for file naming
- Generate a random string of 10 characters
- If a file already exists with the same name in that folder then try different 

